@echo off
echo Installing required dependencies...
pip install PyQt5 PyQtWebEngine pyinstaller

echo.
echo Building ConversationalVoiceDemo.exe...
pyinstaller --onefile --windowed --name ConversationalVoiceDemo src\main\python\conversational_voice_demo\app.py

echo.
echo Build process complete! 
echo If successful, you can find the executable at: dist\ConversationalVoiceDemo.exe
echo.
pause