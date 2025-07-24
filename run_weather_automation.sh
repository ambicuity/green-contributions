#!/bin/bash

# Green Contributions Weather Automation Script
# This script generates weather reports and commits them to maintain GitHub contributions

# Configuration - Update these paths as needed for your environment
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
VENV_ACTIVATE_SCRIPT="/home/YOUR_CPANEL_USERNAME/virtualenv/green-contributions/3.6/bin/activate"
WEATHER_SCRIPT="weather_report.py"
WEATHER_REPORT_FILE="daily_weather_report.md"
SCRIPT_LOG_FILE="weather_script.log"

# Change to script directory
cd "$SCRIPT_DIR" || exit 1

# Function to log messages
log_message() {
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] $1"
}

log_message "Starting weather automation script..."

# Activate virtual environment if the activation script exists
if [ -f "$VENV_ACTIVATE_SCRIPT" ]; then
    log_message "Activating virtual environment..."
    source "$VENV_ACTIVATE_SCRIPT"
    if [ $? -eq 0 ]; then
        log_message "Virtual environment activated successfully"
    else
        log_message "Warning: Failed to activate virtual environment"
    fi
else
    log_message "Virtual environment activation script not found at: $VENV_ACTIVATE_SCRIPT"
    log_message "Continuing with system Python..."
fi

# Check if Python script exists
if [ ! -f "$WEATHER_SCRIPT" ]; then
    log_message "Error: Weather script not found: $WEATHER_SCRIPT"
    exit 1
fi

# Make sure the Python script is executable
chmod +x "$WEATHER_SCRIPT"

# Run the weather report generation
log_message "Generating weather report..."
python3 "$WEATHER_SCRIPT"

if [ $? -eq 0 ]; then
    log_message "Weather report generated successfully"
else
    log_message "Error: Failed to generate weather report"
    exit 1
fi

# Check if weather report file was created/updated
if [ ! -f "$WEATHER_REPORT_FILE" ]; then
    log_message "Error: Weather report file not found after generation"
    exit 1
fi

# Git operations
log_message "Starting Git operations..."

# Add the weather report file to Git
git add "$WEATHER_REPORT_FILE"
if [ $? -eq 0 ]; then
    log_message "Added weather report file to Git staging area"
else
    log_message "Warning: Failed to add weather report file to Git"
fi

# Add the script log file to Git (optional)
if [ -f "$SCRIPT_LOG_FILE" ]; then
    git add "$SCRIPT_LOG_FILE"
    if [ $? -eq 0 ]; then
        log_message "Added script log file to Git staging area"
    else
        log_message "Warning: Failed to add script log file to Git"
    fi
fi

# Check if there are changes to commit
if git diff --cached --quiet; then
    log_message "No changes to commit"
    exit 0
fi

# Create commit with descriptive message
COMMIT_DATE=$(date '+%Y-%m-%d')
COMMIT_TIME=$(date '+%H:%M')
COMMIT_MSG="🌤️ Daily weather update for $COMMIT_DATE at $COMMIT_TIME"

git commit -m "$COMMIT_MSG"
if [ $? -eq 0 ]; then
    log_message "Git commit created successfully: $COMMIT_MSG"
else
    log_message "Error: Failed to create Git commit"
    exit 1
fi

# Push changes to remote repository
log_message "Pushing changes to remote repository..."
git push origin main 2>/dev/null || git push origin master 2>/dev/null

if [ $? -eq 0 ]; then
    log_message "Changes pushed successfully to remote repository"
else
    log_message "Error: Failed to push changes to remote repository"
    # Don't exit with error here, as the commit was successful locally
fi

log_message "Weather automation script completed successfully"