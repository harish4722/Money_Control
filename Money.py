from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QMainWindow, QWidget
from PySide6.QtGui import QIcon
import sys

class MainWindow(QMainWindow, QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Money Control")
        self.setFixedSize(500, 500)
        self.setGeometry(100, 100, 400, 300)
        self.setWindowIcon(QIcon("ICON.png"))
        
        self.is_dark_mode = True
        
        # Initialize the window in dark mode
        self.setStyleSheet("background-color : black; color: white;")
        
        # Create button
        self.button = QPushButton("Dark Mode", self)
        self.button.setFixedSize(100, 100)
        self.button.clicked.connect(self.toggle_mode)
        
        # Set up the layout
        layout = QVBoxLayout()
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def toggle_mode(self):
        if self.is_dark_mode:
            self.light_mode()
        else:
            self.dark_mode()
        self.is_dark_mode = not self.is_dark_mode  
    
    def dark_mode(self):
        self.setStyleSheet("background-color : black; color: white;")  
        self.button.setText("Light Mode")  
    
    def light_mode(self):
        self.setStyleSheet("background-color : white; color: black;")  
        self.button.setText("Dark Mode") 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
