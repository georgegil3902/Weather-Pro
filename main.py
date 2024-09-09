import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit, 
                             QPushButton, QVBoxLayout, QMessageBox)
from PyQt6.QtGui import QFont
from PyQt6.QtCore import Qt

# Dummy weather data function
def get_weather():
    city = city_input.text()
    if not city:
        QMessageBox.critical(window, "Error", "Please enter a city.")
        return

    # Replace this with real weather data fetching logic
    weather_data = {
        "temperature": "22°C",
        "humidity": "60%",
        "condition": "Partly Cloudy"
    }

    result_label.setText(f"City: {city}\n"
                         f"Temperature: {weather_data['temperature']}\n"
                         f"Humidity: {weather_data['humidity']}\n"
                         f"Condition: {weather_data['condition']}")

# Set up the main window
app = QApplication(sys.argv)
window = QWidget()
window.setWindowTitle("Weather Pro")
window.setStyleSheet("background-color: #2C3E50;")  # Dark navy blue background

# Main layout
layout = QVBoxLayout()

# Title Label
title_label = QLabel("Weather Pro")
title_label.setFont(QFont("Helvetica", 24, QFont.Weight.Bold))
title_label.setStyleSheet("color: white;")
title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
layout.addWidget(title_label)

# City input field
city_label = QLabel("Enter city:")
city_label.setFont(QFont("Helvetica", 14))
city_label.setStyleSheet("color: white;")
layout.addWidget(city_label)

city_input = QLineEdit()
city_input.setFont(QFont("Helvetica", 14))
city_input.setStyleSheet("background-color: #BDC3C7; padding: 5px; border-radius: 5px;")
layout.addWidget(city_input)

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
get_weather_button.clicked.connect(get_weather)
layout.addWidget(get_weather_button)

# Result Label
result_label = QLabel("")
result_label.setFont(QFont("Helvetica", 16))
result_label.setStyleSheet("color: white; background-color: #34495E; padding: 10px;")
result_label.setAlignment(Qt.AlignmentFlag.AlignTop)
result_label.setFixedHeight(150)
layout.addWidget(result_label)

# Set the layout for the window
window.setLayout(layout)
window.setGeometry(100, 100, 400, 400)
window.show()

# Run the application
sys.exit(app.exec())
