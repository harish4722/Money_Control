from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QMainWindow, QWidget
from PySide6.QtGui import QIcon, QPixmap, QPainter, QColor
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
        self.button = QPushButton(self)
        self.button.setFixedSize(60, 60)  # Size of the button
        self.button.setStyleSheet("border-radius: 30px; border: none;")  # Makes the button circular
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
        self.set_icon_color("moon_dark_mode_night_mode_icon_190939.png", QColor(255, 255, 255))  # white color for dark mode
    
    def light_mode(self):
        self.setStyleSheet("background-color : white; color: black;")  
        self.set_icon_color("moon_dark_mode_night_mode_icon_190939.png", QColor(0, 0, 0))  # black color for light mode

    def set_icon_color(self, icon_path, color):
        pixmap = QPixmap(icon_path)
        painter = QPainter(pixmap)
        painter.setCompositionMode(QPainter.CompositionMode_SourceIn)
        painter.fillRect(pixmap.rect(), color)  # Fill the icon with the color
        painter.end()
        
        self.button.setIcon(QIcon(pixmap))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()  
    sys.exit(app.exec())
