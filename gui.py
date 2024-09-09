from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

class GuiApp(QWidget):
    def __init__(self, weather_instance):
        super().__init__()
        
        self.weather_instance = weather_instance  # Use the weather instance passed from app.py
        
        # Set up the window
        self.setWindowTitle("Weather Pro")
        self.setStyleSheet("background-color: #2C3E50;")  # Dark navy blue background
        self.setGeometry(100, 100, 400, 400)
        
        # Main layout
        layout = QVBoxLayout()

        # Title label
        title_label = QLabel("Weather Pro")
        title_label.setFont(QFont("Helvetica", 24, QFont.Weight.Bold))
        title_label.setStyleSheet("color: white;")
        title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(title_label)

        # City input field
        # city_label = QLabel("Enter city:")
        # city_label.setFont(QFont("Helvetica", 14))
        # city_label.setStyleSheet("color: white;")
        # layout.addWidget(city_label)

        self.search_city = QLineEdit()
        self.search_city.setPlaceholderText("Search City")
        self.search_city.setFont(QFont("Helvetica", 14))
        self.search_city.setStyleSheet("background-color: #BDC3C7; padding: 5px; border-radius: 5px;")
        layout.addWidget(self.search_city)

        # Get Weather Button
        get_weather_button = QPushButton("Get Weather")
        get_weather_button.setFont(QFont("Helvetica", 14))
        get_weather_button.setStyleSheet("""
            background-color: #1ABC9C;
            color: white;
            padding: 10px;
            border: none;
            border-radius: 10px;
        """)
        get_weather_button.clicked.connect(self.get_weather)
        layout.addWidget(get_weather_button)

        # Result Label
        self.result_label = QLabel("")
        self.result_label.setFont(QFont("Helvetica", 16))
        self.result_label.setStyleSheet("color: white; background-color: #34495E; padding: 10px;")
        self.result_label.setFixedHeight(150)
        layout.addWidget(self.result_label)

        # Set layout
        self.setLayout(layout)

    def get_weather(self):
        city = self.search_city.text()
        if not city:
            QMessageBox.critical(self, "Error", "Please enter a city.")
            return
        
        try:
            weather_data = self.weather_instance.get_weather(place=city)
            self.display_weather(weather_data)
        except Exception as e:
            QMessageBox.critical(self, "Error", f"Failed to retrieve weather data: {e}")

    def display_weather(self, weather_data):
        self.result_label.setText(f"City: {weather_data['location']['city']}\n"
                                  f"Temperature: {weather_data['temperaure_in_celcius']}°C\n"
                                  f"Humidity: {weather_data['humidity']}%\n"
                                  f"Condition: {weather_data['condition']}")
