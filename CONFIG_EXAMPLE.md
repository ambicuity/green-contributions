# Configuration Example for Weather Automation

This file provides examples of how to configure the weather automation system.

## API Key Setup

1. **Get OpenWeatherMap API Key:**
   - Visit: https://openweathermap.org/api
   - Sign up for a free account
   - Generate your API key

2. **Configure the API Key:**
   - Open `weather_report.py`
   - Replace `"YOUR_OPENWEATHERMAP_API_KEY"` with your actual API key
   - Optionally, change the CITY and COUNTRY_CODE variables

3. **Virtual Environment Path:**
   - Update the `VENV_ACTIVATE_SCRIPT` path in `run_weather_automation.sh`
   - Replace `/home/YOUR_CPANEL_USERNAME/virtualenv/green-contributions/3.6/bin/activate`
   - With your actual virtual environment path

## Security Note

**Important:** Never commit your actual API key to the repository. The .gitignore file is configured to exclude common secret files.