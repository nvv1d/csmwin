import sys
from PyQt5.QtCore import QUrl, Qt, QTimer, QSize
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QProgressBar
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEnginePage, QWebEngineSettings
from PyQt5.QtGui import QIcon

class SesameVoiceDemoApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        # Set window properties - adjusted to match the demo section size
        self.setWindowTitle("Conversational Voice Demo")
        self.setGeometry(100, 100, 700, 500)
        self.setFixedSize(700, 500)  # Fix the size to prevent resizing
        
        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        layout.setContentsMargins(0, 0, 0, 0)
        
        # Add loading progress bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setTextVisible(False)
        self.progress_bar.setMaximumHeight(3)
        layout.addWidget(self.progress_bar)
        
        # Create web view with proper settings
        self.web_view = QWebEngineView()
        layout.addWidget(self.web_view)
        
        # Create custom page with proper permissions
        self.page = CustomWebPage(self)
        self.web_view.setPage(self.page)
        
        # Configure settings to allow microphone access
        settings = self.web_view.settings()
        settings.setAttribute(QWebEngineSettings.JavascriptEnabled, True)
        settings.setAttribute(QWebEngineSettings.LocalStorageEnabled, True)
        settings.setAttribute(QWebEngineSettings.AutoLoadImages, True)
        settings.setAttribute(QWebEngineSettings.PluginsEnabled, True)
        
        # The most important setting for microphone access
        settings.setAttribute(QWebEngineSettings.JavascriptCanAccessClipboard, True)
        
        # Connect signals for loading progress
        self.page.loadProgress.connect(self.progress_bar.setValue)
        self.page.loadFinished.connect(self.on_load_finished)
        
        # Load the target URL directly to the demo section
        target_url = "https://www.sesame.com/research/crossing_the_uncanny_valley_of_voice#demo"
        self.web_view.load(QUrl(target_url))

    def on_load_finished(self, ok):
        if ok:
            # Hide progress bar after loading
            self.progress_bar.hide()
            
            # Use a longer delay to ensure the page is fully loaded and rendered
            QTimer.singleShot(2500, self.focus_on_demo)
            
            # Grant microphone permissions
            self.grant_microphone_permissions()
            
    def grant_microphone_permissions(self):
        # JavaScript to auto-accept microphone permission
        grant_script = """
        navigator.mediaDevices.getUserMedia({ audio: true })
            .then(function(stream) {
                console.log('Microphone access granted');
                // Keep the stream alive to maintain permissions
                window.microphoneStream = stream;
            })
            .catch(function(err) {
                console.log('Error getting microphone access: ' + err);
            });
        """
        self.page.runJavaScript(grant_script)
            
    def focus_on_demo(self):
        # More robust script to isolate and display only the conversational voice demo section
        isolate_script = """
        (function() {
            try {
                // First attempt to find demo section using ID
                let demoSection = document.getElementById('demo');
                if (!demoSection) {
                    console.log('Demo section not found by ID');
                    return false;
                }
                
                // Find the conversational demo section - multiple approaches for robustness
                let conversationalSection = null;
                
                // Method 1: Look for heading with "Conversational voice demo" text
                const headers = demoSection.querySelectorAll('h2, h3');
                for (const header of headers) {
                    if (header.innerText.toLowerCase().includes('conversational voice demo')) {
                        conversationalSection = header.closest('div[class*="container"], section, article, div');
                        if (conversationalSection) break;
                    }
                }
                
                // Method 2: Look for audio players within the demo section if Method 1 failed
                if (!conversationalSection) {
                    const audioPlayers = demoSection.querySelectorAll('audio, [class*="player"], [class*="audio"]');
                    if (audioPlayers.length) {
                        conversationalSection = audioPlayers[0].closest('div[class*="container"], section, article, div');
                    }
                }
                
                // Method 3: Look for elements with "Maya" and "Miles" if other methods failed
                if (!conversationalSection) {
                    const allElements = demoSection.querySelectorAll('*');
                    for (const el of allElements) {
                        if ((el.innerText.includes('Maya') || el.innerText.includes('Miles')) && 
                            (el.innerText.includes('voice') || el.innerText.includes('conversation'))) {
                            conversationalSection = el.closest('div[class*="container"], section, article, div');
                            if (conversationalSection) break;
                        }
                    }
                }
                
                // If we found the section, isolate and display it
                if (conversationalSection) {
                    // Save original styles to maintain appearance
                    const computedStyle = window.getComputedStyle(conversationalSection);
                    const originalStyles = {
                        padding: computedStyle.padding,
                        margin: computedStyle.margin,
                        background: computedStyle.background,
                        color: computedStyle.color,
                        fontFamily: computedStyle.fontFamily
                    };
                    
                    // Clean the body and add only our section
                    document.body.innerHTML = '';
                    document.body.appendChild(conversationalSection);
                    
                    // Apply styling to both the section and body
                    document.body.style.cssText = 'margin: 0; padding: 20px; background-color: #ffffff; height: 100vh; overflow-y: auto;';
                    conversationalSection.style.cssText = `
                        display: block;
                        width: 100%;
                        max-width: 650px;
                        margin: 0 auto;
                        padding: ${originalStyles.padding || '20px'};
                        background: ${originalStyles.background || '#ffffff'};
                        color: ${originalStyles.color || '#000000'};
                        font-family: ${originalStyles.fontFamily || 'inherit'};
                    `;
                    
                    // Make sure all audio elements are visible and controls are enabled
                    const audioElements = document.querySelectorAll('audio');
                    audioElements.forEach(audio => {
                        audio.controls = true;
                        audio.style.display = 'block';
                        audio.style.width = '100%';
                        audio.style.marginBottom = '10px';
                    });
                    
                    console.log('Successfully isolated conversational demo section');
                    return true;
                } else {
                    // If we couldn't isolate the section, at least scroll to the demo
                    demoSection.scrollIntoView({behavior: 'smooth', block: 'start'});
                    console.log('Could not isolate section, scrolled to demo instead');
                    return false;
                }
            } catch (e) {
                console.error('Error in focus_on_demo:', e);
                return false;
            }
        })();
        """
        self.page.runJavaScript(isolate_script)


class CustomWebPage(QWebEnginePage):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Set the feature permission for microphone to granted by default
        self.featurePermissionRequested.connect(self.handleFeaturePermission)
        
    def handleFeaturePermission(self, origin, feature):
        # Auto-grant microphone permission when requested
        from PyQt5.QtWebEngineWidgets import QWebEnginePage
        if feature == QWebEnginePage.MediaAudioCapture:
            self.setFeaturePermission(origin, feature, QWebEnginePage.PermissionGrantedByUser)
        else:
            self.setFeaturePermission(origin, feature, QWebEnginePage.PermissionDeniedByUser)
    
    def javaScriptConsoleMessage(self, level, message, line, source):
        # Uncomment for debugging
        # print(f"JS [{level}] Line {line}: {message}")
        pass


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("Conversational Voice Demo")
    
    # Create and show the main window
    window = SesameVoiceDemoApp()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
