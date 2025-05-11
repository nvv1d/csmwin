from pybuilder.core import use_plugin, init, Author, task
import os
import subprocess
import sys
import shutil

use_plugin("python.core")
use_plugin("python.unittest")
use_plugin("python.install_dependencies")
use_plugin("python.flake8")
use_plugin("python.coverage")
use_plugin("python.distutils")

name = "conversational_voice_demo"
version = "1.0.0"
summary = "Desktop application to view Conversational Voice Demo"
description = """
A simple desktop application that opens only the Conversational Voice Demo section from the 
Sesame Research website "Crossing the Uncanny Valley of Voice".
"""

authors = [Author("Your Name", "your.email@example.com")]
license = "MIT"
url = "https://github.com/yourusername/conversational_voice_demo"

default_task = ["clean", "analyze", "publish"]

@init
def set_properties(project):
    project.depends_on("PyQt5")
    project.depends_on("PyQtWebEngine")
    project.depends_on("pyinstaller")
    
    # Set source directory
    project.set_property("dir_source_main_python", "src/main/python")
    project.set_property("dir_source_unittest_python", "src/unittest/python")
    
    # Skip certain checks for the demo
    project.set_property("flake8_break_build", False)
    project.set_property("coverage_break_build", False)

@task
def create_executable(project):
    """Creates an executable using PyInstaller"""
    # Get the directory where setup.py would be generated
    target_dir = project.expand_path("$dir_dist")
    
    # Ensure the target directory exists
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # Path to the main script
    main_module = os.path.join(
        project.expand_path("$dir_dist"),
        project.name,
        "app.py"
    )
    
    # Check if the file exists
    if not os.path.exists(main_module):
        print(f"Main module not found at {main_module}")
        # First build the distribution package
        # Instead of calling build_distutils_package directly, we'll run the publish task
        from pybuilder.reactor import Reactor
        reactor = Reactor(project)
        reactor.execute_task('publish')
        
        # Check again after building
        if not os.path.exists(main_module):
            print(f"Failed to build main module at {main_module}")
            return
    
    # Copy the pyinstaller spec file if it exists
    spec_file = os.path.join(project.basedir, "conversational_voice_demo.spec")
    if os.path.exists(spec_file):
        shutil.copy(spec_file, target_dir)
    
    # Change to the target directory to run PyInstaller
    original_dir = os.getcwd()
    os.chdir(target_dir)
    
    try:
        # Run PyInstaller
        cmd = [
            "pyinstaller",
            "--onefile",
            "--windowed",
            "--name", "ConversationalVoiceDemo",
            main_module
        ]
        
        print(f"Running command: {' '.join(cmd)}")
        subprocess.run(cmd, check=True)
        
        # Move the executable to the dist directory of the project
        exe_name = "ConversationalVoiceDemo.exe" if sys.platform == "win32" else "ConversationalVoiceDemo"
        exe_path = os.path.join(target_dir, "dist", exe_name)
        final_exe_path = os.path.join(project.basedir, "dist", exe_name)
        
        # Ensure the final directory exists
        os.makedirs(os.path.dirname(final_exe_path), exist_ok=True)
        
        # Copy the executable
        if os.path.exists(exe_path):
            shutil.copy(exe_path, final_exe_path)
            print(f"Executable created at: {final_exe_path}")
        else:
            print(f"Executable not found at: {exe_path}")
    
    finally:
        # Change back to the original directory
        os.chdir(original_dir)