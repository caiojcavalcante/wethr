import random
import datetime

class WeatherService:
    def __init__(self, service_name):
        self.service_name = service_name

# Weather Data Collection
class WeatherDataCollector(WeatherService):
    def __init__(self):
        super().__init__("Weather Data Collector")
        self.weather_sources = ["API1", "API2", "API3"]  #TODO
    
    def collect_data(self, location):
        # Simulate weather data collection from various sources.
        weather_data = {
            "temperature": random.uniform(-10, 40),
            "humidity": random.randint(20, 90),
            "wind_speed": random.uniform(0, 20),
            "condition": random.choice(["Sunny", "Rainy", "Cloudy", "Snowy", "Windy"])
        }
        print(f"[{self.service_name}] Data collected for {location}: {weather_data}")
        return weather_data

# Forecast Generation
class WeatherForecaster(WeatherService):
    def __init__(self):
        super().__init__("Weather Forecaster")

    def generate_forecast(self, current_data):
        # Generate a forecast based on current conditions.
        forecast = {
            "tomorrow": random.choice(["Sunny", "Rainy", "Cloudy"]),
            "week_ahead": random.choice(["Mostly Sunny", "Scattered Showers", "Stormy"]),
            "long_term": random.choice(["Warming Trend", "Cooling Trend", "Stable"])
        }
        print(f"[{self.service_name}] Forecast generated: {forecast}")
        return forecast

# User Location Services
class UserLocationService(WeatherService):
    def __init__(self):
        super().__init__("User Location Service")

    def get_weather_for_location(self, location, weather_collector, forecaster):
        # Fetch weather data and forecast for a given location.
        current_weather = weather_collector.collect_data(location)
        forecast = forecaster.generate_forecast(current_weather)
        return {"current_weather": current_weather, "forecast": forecast}

# Alert System for Severe Weather
class WeatherAlertSystem(WeatherService):
    def __init__(self):
        super().__init__("Weather Alert System")

    def check_for_alerts(self, weather_data):
        # Check if severe weather alerts need to be issued.
        if weather_data["condition"] in ["Stormy", "Snowy"] or weather_data["wind_speed"] > 15:
            alert_message = f"Severe Weather Alert: {weather_data['condition']} with strong winds!"
            print(f"[{self.service_name}] {alert_message}")
            return alert_message
        return "No severe weather alerts."

# Historical Weather Data
class HistoricalWeatherData(WeatherService):
    def __init__(self):
        super().__init__("Historical Weather Data")
        self.history = {}
        #TODO FETCH DATA

    def store_weather_data(self, location, data):
        # Store weather data for a location.
        date = datetime.date.today().isoformat()
        if location not in self.history:
            self.history[location] = {}
        self.history[location][date] = data
        print(f"[{self.service_name}] Data stored for {location} on {date}.")

    def get_historical_data(self, location, date):
        # Retrieve historical weather data for a location.
        return self.history.get(location, {}).get(date, "No data available.")

# Climate Analytics and Reporting
class ClimateAnalytics(WeatherService):
    def __init__(self):
        super().__init__("Climate Analytics")

    def analyze_trends(self, historical_data):
        # Analyze climate trends from historical data.
        trend = random.choice(["Warming", "Cooling", "Stable"])
        print(f"[{self.service_name}] Climate trend analysis: {trend}")
        return trend

# User Feedback System
class UserFeedbackSystem(WeatherService):
    def __init__(self):
        super().__init__("User Feedback System")
        self.reports = []

    def submit_report(self, location, report):
        # Allow users to report local weather conditions.
        self.reports.append({"location": location, "report": report})
        print(f"[{self.service_name}] User report submitted: {report}")

# Main system integration
class WeatherForecastingSystem:
    def __init__(self):
        self.weather_collector = WeatherDataCollector()
        self.forecaster = WeatherForecaster()
        self.user_location_service = UserLocationService()
        self.alert_system = WeatherAlertSystem()
        self.historical_data = HistoricalWeatherData()
        self.analytics = ClimateAnalytics()
        self.feedback_system = UserFeedbackSystem()

    def get_weather_update(self, location):
        # Get complete weather update.
        weather_info = self.user_location_service.get_weather_for_location(location, self.weather_collector, self.forecaster)
        alert = self.alert_system.check_for_alerts(weather_info["current_weather"])
        self.historical_data.store_weather_data(location, weather_info["current_weather"])
        
        return {"weather_info": weather_info, "alert": alert}
