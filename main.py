from weather import *

system = WeatherForecastingSystem()

location = "Maceio" 

option = int(input("Welcome to Harp, your weather forecast app, would you like to lookup the weather in your location or another?\n0 - My location\n1 - Another place\n"))

if(option):
    location = input("Qual localização desejada?\n")
    
print("Lugar escolhido " + location)

weather_update = system.get_weather_update(location)

option = int(input("Would you tell us how the weather is in your location?\n1 - Yes\n0 - No\n"))

if(option):
    report = input("How is the weather right now in your location?")
    system.feedback_system.submit_report(location, report)


climate_trend = system.analytics.analyze_trends(system.historical_data.history)