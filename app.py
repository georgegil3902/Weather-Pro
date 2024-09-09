from weather import Weather
from gui import GuiApp
import sys
from PyQt6.QtWidgets import QApplication

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    # Initialize weather API module
    weather = Weather()
    
    # Initialize GUI and pass the weather instance
    weather_app = GuiApp(weather)
    weather_app.show()
    
    sys.exit(app.exec())
