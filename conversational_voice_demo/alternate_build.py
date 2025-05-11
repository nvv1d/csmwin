"""
Simpler direct build script for PyInstaller in case PyBuilder has issues.
Run this directly with Python to build the executable without PyBuilder.
"""

import os
import sys
import subprocess
import shutil

def ensure_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    # Ensure we have the necessary directories
    ensure_dir("dist")
    
    # Get the path to the main script
    main_module = os.path.join("src", "main", "python", "conversational_voice_demo", "app.py")
    
    if not os.path.exists(main_module):
        print(f"Error: Main module not found at {main_module}")
        return 1
    
    # Run PyInstaller directly
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", "ConversationalVoiceDemo",
        main_module
    ]
    
    print(f"Running command: {' '.join(cmd)}")
    result = subprocess.run(cmd)
    
    if result.returncode != 0:
        print("Error: PyInstaller failed to build the executable")
        return 1
    
    # Success message
    print("\nBuild completed successfully!")
    print(f"Executable created at: dist/ConversationalVoiceDemo.exe")
    return 0

if __name__ == "__main__":
    sys.exit(main())