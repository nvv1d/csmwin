import sys
from PyQt5.QtCore import QUrl, Qt, QTimer
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage
from PyQt5.QtGui import QIcon

class SesameVoiceDemoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window properties - adjusted to match the screenshot dimensions
        self.setWindowTitle("Conversational Voice Demo")
        self.setGeometry(100, 100, 700, 500)  # Adjusted to match the demo section size
        self.setFixedSize(700, 500)  # Fix the size to prevent resizing
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)  # Remove margins for a cleaner view
        
        # Create web view
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        
        # Create custom page to handle JavaScript
        self.page = CustomWebPage(self)
        self.web_view.setPage(self.page)
        
        # Load the target URL directly to the demo section
        target_url = "https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice#demo"
        self.web_view.load(QUrl(target_url))
        
        # Set up a timer to scroll to the demo section after page load
        self.web_view.loadFinished.connect(self.on_load_finished)

    def on_load_finished(self, ok):
        if ok:
            # After page is loaded, focus on the conversational voice demo section only
            self.focus_on_demo()
            
    def focus_on_demo(self):
        # Use JavaScript to isolate and display only the conversational voice demo section
        isolate_script = """
        (function() {
            // Hide everything initially
            document.querySelectorAll('body > *').forEach(function(el) {
                el.style.display = 'none';
            });
            
            // Find the conversational voice demo element
            var demoElement = document.getElementById('demo');
            if (demoElement) {
                // Find the conversational voice demo section specifically
                var conversationalDemo = demoElement.querySelector('div:has(h2:contains("Conversational voice demo"))');
                if (!conversationalDemo) {
                    // Fallback to find the h2 first, then its parent container
                    var demoHeader = Array.from(demoElement.querySelectorAll('h2')).find(h => h.textContent.includes('Conversational voice demo'));
                    if (demoHeader) {
                        conversationalDemo = demoHeader.closest('div[class*="container"]');
                    }
                }
                
                if (conversationalDemo) {
                    // Display only this section
                    conversationalDemo.style.display = 'block';
                    document.body.innerHTML = '';
                    document.body.appendChild(conversationalDemo);
                    document.body.style.backgroundColor = '#ffffff';
                    document.body.style.margin = '0';
                    document.body.style.padding = '0';
                    return true;
                }
            }
            
            // If we couldn't find or isolate the demo, at least scroll to it
            var demoElement = document.getElementById('demo');
            if (demoElement) {
                demoElement.scrollIntoView({behavior: 'smooth', block: 'start'});
            }
            return false;
        })();
        """
        # Execute after a delay to ensure the page is fully rendered
        QTimer.singleShot(1500, lambda: self.page.runJavaScript(isolate_script))


class CustomWebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        
    def javaScriptConsoleMessage(self, level, message, line, source):
        # Optional: Handle JavaScript console messages for debugging
        pass


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Sesame Voice Demo")
    
    window = SesameVoiceDemoApp()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()