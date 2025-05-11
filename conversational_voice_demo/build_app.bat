@echo off
echo ===================================================
echo Building Conversational Voice Demo Application
echo ===================================================

echo.
echo Step 1: Checking Python installation...
python --version
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Python not found or not in PATH.
    echo Please install Python and try again.
    pause
    exit /b 1
)

echo.
echo Step 2: Creating required directories if they don't exist...
if not exist "src\main\python\conversational_voice_demo" (
    mkdir "src\main\python\conversational_voice_demo"
)

echo.
echo Step 3: Installing required dependencies...
echo This may take a few minutes depending on your internet connection.
pip install PyQt5 PyQtWebEngine pyinstaller
if %ERRORLEVEL% NEQ 0 (
    echo ERROR: Failed to install dependencies.
    echo Please check your internet connection or try running as administrator.
    pause
    exit /b 1
)

echo.
echo Step 4: Ensuring __init__.py exists...
echo # Conversational Voice Demo App package > "src\main\python\conversational_voice_demo\__init__.py"
echo __version__ = "1.0.0" >> "src\main\python\conversational_voice_demo\__init__.py"

echo.
echo Step 5: Building executable...
pyinstaller --onefile --windowed --name ConversationalVoiceDemo --clean ^
    --add-data "src\main\python\conversational_voice_demo\__init__.py;conversational_voice_demo" ^
    src\main\python\conversational_voice_demo\app.py

if %ERRORLEVEL% NEQ 0 (
    echo.
    echo ERROR: PyInstaller failed to build the application.
    echo Please check the output above for more details.
    pause
    exit /b 1
)

echo.
echo ===================================================
echo BUILD SUCCESSFUL!
echo ===================================================
echo.
echo The executable has been created at: dist\ConversationalVoiceDemo.exe
echo.
echo NOTE: When you run the application, you may need to allow microphone access
echo       if prompted by your operating system.
echo.
pause
