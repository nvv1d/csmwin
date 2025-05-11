# Detailed File Structure and Setup Guide

## Complete File Structure

```
conversational_voice_demo/
│
├── build.py                          # PyBuilder build file
├── conversational_voice_demo.spec    # PyInstaller spec file
├── build_app.bat                     # Simple batch file for direct building
├── alternate_build.py                # Alternative Python build script
├── project_setup.bat                 # Script to create directory structure
│
├── SIMPLE_BUILD_GUIDE.md             # Guide for alternative build methods
├── README.md                         # Main project documentation
├── FILE_STRUCTURE.md                 # Basic file structure overview
├── DETAILED_FILE_STRUCTURE.md        # This file with detailed information
│
├── src/
│   ├── main/
│   │   └── python/
│   │       └── conversational_voice_demo/
│   │           ├── __init__.py       # Package initialization
│   │           └── app.py            # Main application code
│   │
│   └── unittest/
│       └── python/
│           └── conversational_voice_demo/
│               ├── __init__.py       # Test package initialization
│               └── app_tests.py      # Application test cases
│
└── dist/                             # Contains the final executable
    └── ConversationalVoiceDemo.exe   # The application executable
```

## File Contents Overview

### Main Application Files

1. **`src/main/python/conversational_voice_demo/app.py`**
   - Primary application code
   - Creates PyQt5 window with WebEngine view
   - Loads the Sesame voice demo and isolates just the conversational demo section
   - Sets window size to 700x500 to match the required layout

2. **`src/main/python/conversational_voice_demo/__init__.py`**
   - Package initialization
   - Contains version information and basic package documentation

### Build System Files

3. **`build.py`**
   - PyBuilder configuration file
   - Defines project metadata and dependencies
   - Contains custom tasks for building the executable

4. **`conversational_voice_demo.spec`**
   - PyInstaller specification file
   - Contains configuration for creating the standalone executable

5. **`build_app.bat`**
   - Simple Windows batch file
   - Installs dependencies and builds the application
   - Provides the easiest build method for Windows users

6. **`alternate_build.py`**
   - Pure Python alternative to PyBuilder
   - Directly calls PyInstaller to build the application
   - Useful if PyBuilder has compatibility issues

7. **`project_setup.bat`**
   - Creates the initial directory structure
   - Sets up empty __init__.py files
   - Helps with initial project setup

### Test Files

8. **`src/unittest/python/conversational_voice_demo/app_tests.py`**
   - Unit tests for the application
   - Tests basic application functionality
   - Uses mock objects to test without actual web content

9. **`src/unittest/python/conversational_voice_demo/__init__.py`**
   - Test package initialization file

### Documentation Files

10. **`README.md`**
    - Project overview and primary documentation
    - Installation and usage instructions
    - General project information

11. **`SIMPLE_BUILD_GUIDE.md`**
    - Alternative build instructions
    - Troubleshooting information for build issues
    - Step-by-step build process

12. **`FILE_STRUCTURE.md`**
    - Basic file structure overview
    - Quick reference for project organization

13. **`DETAILED_FILE_STRUCTURE.md`**
    - This file
    - Comprehensive description of all project files
    - More detailed information about each file's purpose

## Setting Up the Project from Scratch

1. **Create the directory structure:**
   - Run `project_setup.bat` or manually create the directories
   - Ensure all __init__.py files are created

2. **Copy source files to appropriate locations:**
   - Place app.py in src/main/python/conversational_voice_demo/
   - Place app_tests.py in src/unittest/python/conversational_voice_demo/
   - Place build files in the root directory

3. **Build the application:**
   - Option 1: Run `build_app.bat` (simplest method)
   - Option 2: Run `python alternate_build.py` 
   - Option 3: Use PyBuilder with `pyb create_executable`

4. **Run the application:**
   - Execute dist/ConversationalVoiceDemo.exe
