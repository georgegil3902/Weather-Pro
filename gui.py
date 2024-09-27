from PySide6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLabel, 
                               QToolButton, QLineEdit, QFrame)
from PySide6.QtCore import QRect, QSize, Qt
from PySide6.QtGui import QPixmap, QIcon
import sys

class WeatherProGui(object):
    def setupUi(self, application):
        # Set up main window
        application.setObjectName("application")
        application.resize(1200, 700)

        # Main background widget
        self.background = QWidget(application)
        self.background.setGeometry(QRect(0, 0, 1200, 700))
        self.background.setStyleSheet("""
            background-color: #0b131f;
            border-radius: 20px;
            box-shadow: 0 0 10px rgba(255, 255, 255, 0.5);
        """)

        # Initialize storage for forecast days and hourly forecasts
        self.forecast_days = {}
        self.hourly_forecasts = {}

        # Create components
        self.create_navigation()
        self.create_forecast()
        self.create_todays_forecast()
        self.create_air_conditions()
        self.create_main_elements()

        # Translate UI elements
        self.retranslateUi(application)

    def create_navigation(self):
        """Create navigation buttons with icons on the left."""
        self.navigation = QFrame(self.background)
        self.navigation.setGeometry(QRect(20, 20, 80, 660))
        self.navigation.setStyleSheet("background-color: #202b3b;")

        # App icon
        self.app_icon = QLabel(self.navigation)
        self.app_icon.setGeometry(QRect(15, 25, 50, 50))
        app_icon_pixmap = QPixmap("assets/icons/app.png")
        self.app_icon.setPixmap(app_icon_pixmap.scaled(50, 50, Qt.KeepAspectRatio))

        # Define common style for tool buttons
        tool_button_style = """
            QToolButton {
                text-align: center;
                font-size: 12px;
            }
        """

        # Weather button
        self.weather_button = QToolButton(self.navigation)
        self.weather_button.setGeometry(QRect(0, 150, 80, 80))
        self.weather_button.setIcon(QIcon("assets/icons/weather.png"))
        self.weather_button.setIconSize(QSize(50, 50))
        self.weather_button.setText("Weather")
        self.weather_button.setStyleSheet(tool_button_style)
        self.weather_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # Cities button
        self.cities_button = QToolButton(self.navigation)
        self.cities_button.setGeometry(QRect(0, 250, 80, 80))
        self.cities_button.setIcon(QIcon("assets/icons/city.png"))
        self.cities_button.setIconSize(QSize(40, 40))
        self.cities_button.setText("Cities")
        self.cities_button.setStyleSheet(tool_button_style)
        self.cities_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

        # Settings button
        self.settings_button = QToolButton(self.navigation)
        self.settings_button.setGeometry(QRect(0, 350, 80, 80))
        self.settings_button.setIcon(QIcon("assets/icons/settings.png"))
        self.settings_button.setIconSize(QSize(40, 40))
        self.settings_button.setText("Settings")
        self.settings_button.setStyleSheet(tool_button_style)
        self.settings_button.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)

    def create_forecast(self):
        """Create the 7-day forecast section on the right."""
        self.forecast_frame = QFrame(self.background)
        self.forecast_frame.setGeometry(QRect(880, 80, 300, 600))
        self.forecast_frame.setStyleSheet("background-color: #202b3b;")

        self.forecast_label = QLabel("7-Day Forecast", self.forecast_frame)
        self.forecast_label.setGeometry(QRect(20, 15, 150, 20))

        self.forecast_layout = QVBoxLayout(self.forecast_frame)

        # Add forecast days dynamically and store them in a dictionary
        for i in range(1, 8):
            self.add_forecast_day(i)

    def add_forecast_day(self, day_number):
        """Adds layout for each day in the forecast section and stores the references."""
        day_layout = QHBoxLayout()

        # Create and store forecast elements
        day_label = QLabel(f"Day {day_number}", self.forecast_frame)
        condition_label = QLabel("Sunny", self.forecast_frame)
        temperature_label = QLabel("36/22", self.forecast_frame)

        # Store these labels in the forecast_days dictionary for future modification
        self.forecast_days[day_number] = {
            "day_label": day_label,
            "condition_label": condition_label,
            "temperature_label": temperature_label
        }

        # Add them to the layout
        day_layout.addWidget(day_label)
        day_layout.addWidget(condition_label)
        day_layout.addWidget(temperature_label)
        self.forecast_layout.addLayout(day_layout)

    def create_todays_forecast(self):
        """Create today's forecast section in the middle."""
        self.todays_forecast_frame = QFrame(self.background)
        self.todays_forecast_frame.setGeometry(QRect(120, 330, 740, 160))
        self.todays_forecast_frame.setStyleSheet("background-color:#202b3b;")

        self.todays_forecast_label = QLabel("Today's Forecast", self.todays_forecast_frame)
        self.todays_forecast_label.setGeometry(QRect(20, 15, 150, 20))

        self.todays_forecast_layout = QHBoxLayout(self.todays_forecast_frame)

        # Add hourly forecast using loop and store in a dictionary
        for i in range(1, 7):
            self.add_hourly_forecast(i)

    def add_hourly_forecast(self, hour_number):
        """Adds layout for hourly forecast data and stores references for dynamic updates."""
        hourly_layout = QVBoxLayout()

        time_label = QLabel(f"{6 * hour_number}:00 AM", self.todays_forecast_frame)
        condition_label = QLabel("Clear", self.todays_forecast_frame)
        temperature_label = QLabel(f"{25 + hour_number}°C", self.todays_forecast_frame)

        # Store these labels for future updates
        self.hourly_forecasts[hour_number] = {
            "time_label": time_label,
            "condition_label": condition_label,
            "temperature_label": temperature_label
        }

        # Add widgets to the layout
        hourly_layout.addWidget(time_label)
        hourly_layout.addWidget(condition_label)
        hourly_layout.addWidget(temperature_label)
        self.todays_forecast_layout.addLayout(hourly_layout)

    def create_air_conditions(self):
        """Create air conditions section at the bottom."""
        self.air_conditions_frame = QFrame(self.background)
        self.air_conditions_frame.setGeometry(QRect(120, 510, 740, 170))
        self.air_conditions_frame.setStyleSheet("background-color: #202b3b;")

        self.air_conditions_label = QLabel("Air Conditions", self.air_conditions_frame)
        self.air_conditions_label.setGeometry(QRect(20, 15, 150, 20))

        # Add air condition details
        self.add_air_condition("Real Feel", "30°C", 50, 110, "thermometer_icon.png")
        self.add_air_condition("Chance of Rain", "10%", 200, 110, "rain_icon.png")
        self.add_air_condition("Wind", "5 km/h", 350, 110, "wind_icon.png")
        self.add_air_condition("UV Index", "3", 500, 110, "uv_icon.png")

    def add_air_condition(self, label_text, value_text, x, y, icon_name):
        """Adds a label and icon for air condition metrics."""
        icon_label = QLabel(self.air_conditions_frame)
        icon_label.setGeometry(QRect(x - 30, y, 21, 21))
        icon_label.setPixmap(QPixmap(f"assets/icons/{icon_name}"))

        label = QLabel(label_text, self.air_conditions_frame)
        label.setGeometry(QRect(x, y, 120, 20))
        value = QLabel(value_text, self.air_conditions_frame)
        value.setGeometry(QRect(x, y + 30, 100, 20))

        # Optionally, you can store these labels if you need to update them later.

    def create_main_elements(self):
        """Create current weather section at the top."""
        self.current_city = QLabel("Berlin", self.background)
        self.current_city.setGeometry(QRect(150, 110, 300, 50))
        self.current_city.setStyleSheet("font-size: 30px; font-weight: bold;")

        self.current_condition = QLabel("Sunny", self.background)
        self.current_condition.setGeometry(QRect(640, 100, 200, 200))

        self.current_temperature = QLabel("36°C", self.background)
        self.current_temperature.setGeometry(QRect(150, 230, 150, 50))

        # City input field
        self.city_input = QLineEdit(self.background)
        self.city_input.setGeometry(QRect(120, 20, 740, 50))
        self.city_input.setStyleSheet("background-color: #202b3b;")

    def retranslateUi(self, application):
        application.setWindowTitle("Weather Pro")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    WeatherPro = QWidget()
    ui = WeatherProGui()
    ui.setupUi(WeatherPro)
    WeatherPro.show()
    sys.exit(app.exec())
