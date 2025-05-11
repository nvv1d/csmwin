# Quick Start Guide

## Fastest Way to Build and Run the App

If you just want to build and run the application as quickly as possible:

### Step 1: Set up the project
Double-click on `project_setup.bat` to create the directory structure.

### Step 2: Copy the source files
Ensure all source files are in their correct locations:
- `app.py` → src/main/python/conversational_voice_demo/
- All build files in the root directory

### Step 3: Build the executable
Double-click on `build_app.bat` and wait for the process to complete.

### Step 4: Run the application
Once built, find and run `ConversationalVoiceDemo.exe` in the `dist` folder.

## Files Required for Minimal Build

If you want the absolute minimum files needed to build the app:

1. Directory structure:
   ```
   conversational_voice_demo/
   ├── src/main/python/conversational_voice_demo/
   │   ├── __init__.py
   │   └── app.py
   └── build_app.bat  
   ```

2. Only need two key files:
   - `src/main/python/conversational_voice_demo/app.py` - Contains the application code
   - `build_app.bat` - Handles the build process

3. Run `build_app.bat` and it will:
   - Install required dependencies
   - Package the app as an executable
   - Create the .exe file in a dist folder

That's it! The batch file handles everything else automatically.
