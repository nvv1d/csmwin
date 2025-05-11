import unittest
from unittest.mock import patch, MagicMock

# Simple test case for the app
class AppTests(unittest.TestCase):
    
    @patch('sesame_voice_app.app.QApplication')
    @patch('sesame_voice_app.app.SesameVoiceDemoApp')
    def test_main_creates_application(self, mock_app_class, mock_qapp):
        # Import the module
        from sesame_voice_app.app import main
        
        # Mock the sys.argv
        with patch('sys.argv', ['app.py']):
            # Call the main function
            main()
            
            # Assert that QApplication was created
            mock_qapp.assert_called_once()
            
            # Assert that the app window was created and shown
            mock_app_instance = mock_app_class.return_value
            mock_app_instance.show.assert_called_once()
            
            # Assert that exec_ was called
            mock_qapp_instance = mock_qapp.return_value
            mock_qapp_instance.exec_.assert_called_once()
            
    # Test the SesameVoiceDemoApp class
    @patch('sesame_voice_app.app.QMainWindow')
    @patch('sesame_voice_app.app.QWebEngineView')
    def test_app_initialization(self, mock_web_view, mock_main_window):
        from sesame_voice_app.app import SesameVoiceDemoApp
        
        # Create an instance of the app
        app = SesameVoiceDemoApp()
        
        # Verify that the window title is set correctly
        self.assertEqual(app.windowTitle(), "Sesame Voice Demo")
        
        # Verify that the web view loads the correct URL
        mock_web_view_instance = mock_web_view.return_value
        mock_web_view_instance.load.assert_called_once()
        
if __name__ == '__main__':
    unittest.main()
