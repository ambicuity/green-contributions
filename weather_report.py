#!/usr/bin/env python3
"""
Weather Report Generator for Green Contributions Automator
Fetches current weather data from OpenWeatherMap API and appends to daily report.
"""

import requests
import json
from datetime import datetime
import os
import sys

# Configuration - Replace with your actual values
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"  # Get from: https://openweathermap.org/api
CITY = "Boston"
COUNTRY_CODE = "US"
UNITS = "imperial"  # Options: standard, metric, imperial

# File paths
WEATHER_REPORT_FILE = "daily_weather_report.md"
SCRIPT_LOG_FILE = "weather_script.log"

def log_message(message):
    """Log a message with timestamp to the script log file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_entry = f"[{timestamp}] {message}\n"
    
    try:
        with open(SCRIPT_LOG_FILE, "a") as log_file:
            log_file.write(log_entry)
    except Exception as e:
        print(f"Error writing to log file: {e}")

def fetch_weather_data():
    """Fetch current weather data from OpenWeatherMap API."""
    if API_KEY == "YOUR_OPENWEATHERMAP_API_KEY":
        error_msg = "Error: Please set your OpenWeatherMap API key in weather_report.py"
        print(error_msg)
        log_message(error_msg)
        sys.exit(1)
    
    url = f"http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": f"{CITY},{COUNTRY_CODE}",
        "appid": API_KEY,
        "units": UNITS
    }
    
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        error_msg = f"Error fetching weather data: {e}"
        print(error_msg)
        log_message(error_msg)
        sys.exit(1)

def format_weather_report(weather_data):
    """Format weather data into markdown report."""
    date_str = datetime.now().strftime("%Y-%m-%d")
    
    # Extract relevant data
    location = f"{weather_data['name']}, {COUNTRY_CODE}"
    condition = weather_data['weather'][0]['description'].title()
    temp = weather_data['main']['temp']
    feels_like = weather_data['main']['feels_like']
    humidity = weather_data['main']['humidity']
    wind_speed = weather_data['wind']['speed']
    
    # Format temperature unit
    temp_unit = "°F" if UNITS == "imperial" else "°C" if UNITS == "metric" else "K"
    
    # Create formatted report
    report = f"""## 🗓️ Weather Report for {date_str}

- **Location:** {location}
- **Condition:** {condition}
- **Temperature:** {temp}{temp_unit} (Feels like: {feels_like}{temp_unit})
- **Humidity:** {humidity}%
- **Wind Speed:** {wind_speed} {'mph' if UNITS == 'imperial' else 'm/s'}

---
"""
    return report

def append_weather_report(report):
    """Append weather report to the daily report file."""
    try:
        with open(WEATHER_REPORT_FILE, "a") as report_file:
            report_file.write(report)
        return True
    except Exception as e:
        error_msg = f"Error writing weather report: {e}"
        print(error_msg)
        log_message(error_msg)
        return False

def main():
    """Main function to generate and append weather report."""
    try:
        # Fetch weather data
        weather_data = fetch_weather_data()
        
        # Format the report
        report = format_weather_report(weather_data)
        
        # Append to file
        if append_weather_report(report):
            date_str = datetime.now().strftime("%Y-%m-%d")
            success_msg = f"Successfully generated and appended weather report for {date_str}"
            print(success_msg)
            log_message(success_msg)
        else:
            sys.exit(1)
            
    except Exception as e:
        error_msg = f"Unexpected error in main: {e}"
        print(error_msg)
        log_message(error_msg)
        sys.exit(1)

if __name__ == "__main__":
    main()