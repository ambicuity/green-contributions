# 🟩 Green Contributions Automator (Weather Edition)

This repository hosts a simple automation script designed to maintain a consistent daily contribution streak on GitHub. More than just keeping the contribution graph green, this project incorporates a "fun" element by dynamically fetching and committing **daily weather reports**.

## 🌟 Purpose

The primary goals of this project are:
* To demonstrate and practice setting up `cron` jobs on a Linux server.
* To automate Git commit and push operations.
* To playfully "green up" the GitHub contribution graph.
* To build a cumulative log of **daily weather information** over time.

## ✨ How it Works

The core of this project is a shell script (`run_weather_automation.sh`) that runs on a remote server via a `cron` job.

1.  **Daily Execution**: A `cron` job is scheduled to run the `run_weather_automation.sh` script twice every day (at midnight and noon server time).
2.  **Content Generation**: The script executes a Python script (`weather_report.py`) that uses a weather API (e.g., OpenWeatherMap) to fetch current weather conditions for a specified location (e.g., Boston, US).
3.  **File Update**: The fetched weather data, along with a timestamp, is appended to `daily_weather_report.md`.
4.  **Git Operations**:
    * The `daily_weather_report.md` file (and potentially `weather_script_log`) is added to the Git staging area.
    * A new commit is created with a descriptive message (including an emoji!).
    * The changes are pushed to this GitHub repository (`master` branch).
5.  **Logging**: All output from the cron job (including script messages and errors) is redirected to `cron_weather.log` for easy monitoring and debugging. A separate `weather_script_log` also tracks successful generation.

## 🚀 Setup & Installation (for your own Namecheap server)

If you'd like to set up a similar automation on a Namecheap shared hosting server, here's a high-level overview of the steps we followed:

1.  **Clone this repository** on your server via SSH:
    ```bash
    git clone [https://github.com/ambicuity/green-contributions.git](https://github.com/ambicuity/green-contributions.git)
    cd green-contributions
    ```
2.  **Configure Git Identity (Crucial for GitHub Contributions):**
    Ensure the email used here is **added and VERIFIED** on your GitHub account, otherwise contributions won't show on your profile graph.
    ```bash
    git config --global user.email "your_github_verified_email@example.com"
    git config --global user.name "Your Name"
    ```
3.  **Set up Python Environment (via cPanel):**
    * Log in to **cPanel**.
    * Go to **"Setup Python App"**.
    * Click "CREATE APPLICATION".
    * Select your **Python version** (e.g., Python 3.9).
    * Set **Application Root** to `/home/YOUR_CPANEL_USERNAME/green-contributions`.
    * Click "CREATE".
    * Once created, note the "Enter to virtual environment" command (e.g., `source /home/YOUR_CPANEL_USERNAME/virtualenv/green-contributions/3.6/bin/activate`). This is your virtual environment path.
4.  **Install Python Dependencies:**
    * SSH into your server.
    * Navigate to your project: `cd /home/YOUR_CPANEL_USERNAME/green-contributions`
    * Activate the Namecheap-provided virtual environment (using the path from step 3):
        ```bash
        source /home/YOUR_CPANEL_USERNAME/virtualenv/green-contributions/3.6/bin/activate
        ```
    * Install required libraries:
        ```bash
        pip install -r requirements.txt
        ```
5.  **Configure `weather_report.py`:**
    * Open `weather_report.py` and replace placeholder API keys, `CITY`, and `COUNTRY_CODE` with your desired values.
6.  **Update `run_weather_automation.sh`:**
    * Open `run_weather_automation.sh` (e.g., `nano run_weather_automation.sh`).
    * Ensure the `source` command at the beginning uses the **exact virtual environment path** noted in step 3.
    * Make the script executable: `chmod +x run_weather_automation.sh`
7.  **Set up the Cron Job (via cPanel):**
    * Go to cPanel's **"Cron Jobs"** section.
    * Set the schedule (e.g., "Twice Per Day" or `0 0,12 * * *`).
    * For the **Command**, use:
        ```bash
        /bin/bash -c "cd /home/YOUR_CPANEL_USERNAME/green-contributions && source /home/YOUR_CPANEL_USERNAME/virtualenv/green-contributions/3.6/bin/activate && ./run_weather_automation.sh >> /home/YOUR_CPANEL_USERNAME/green-contributions/cron_weather.log 2>&1"
        ```
        Remember to replace `YOUR_CPANEL_USERNAME` with your actual cPanel username.

## 📜 Daily Weather Report Log

Check `daily_weather_report.md` in this repository to see the accumulating collection of daily weather information!
