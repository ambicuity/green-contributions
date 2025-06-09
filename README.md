# 🟩 Green Contributions Automator

This repository hosts a simple automation script designed to maintain a consistent daily contribution streak on GitHub. More than just 
keeping the contribution graph green, this project incorporates a "fun" element by dynamically fetching and committing interesting 
programming quotes or insights daily.

## 🌟 Purpose

The primary goals of this project are:
* To demonstrate and practice setting up `cron` jobs on a Linux server.
* To automate Git commit and push operations.
* To playfully "green up" the GitHub contribution graph.
* To build a cumulative log of interesting programming quotes and insights over time.

## ✨ How it Works

The core of this project is a shell script (`daily_commit.sh`) that runs on a remote server via a `cron` job.

1.  **Daily Execution**: A `cron` job is scheduled to run the `daily_commit.sh` script once every day at midnight (00:00 server time).
2.  **Content Generation**: The script uses `curl` to fetch a random programming quote from a public API (e.g., 
`programming-quotes-api.herokuapp.com`).
3.  **File Update**: The fetched quote, along with a timestamp, is appended to `daily_insight.md`.
4.  **Git Operations**:
    * The `daily_insight.md` file is added to the Git staging area.
    * A new commit is created with a descriptive message (including an emoji!).
    * The changes are pushed to this GitHub repository (`master` branch).
5.  **Logging**: All output from the cron job (including script messages and errors) is redirected to `cron.log` for easy monitoring and 
debugging.

## 🚀 Setup & Installation (for your own server)

If you'd like to set up a similar automation, here's a high-level overview of the steps:

1.  **Clone this repository** (or create a new one) on your server:
    ```bash
    git clone [https://github.com/ambicuity/green-contributions.git](https://github.com/ambicuity/green-contributions.git)
    cd green-contributions
    ```
2.  **Configure Git Identity**:
    ```bash
    git config --global user.email "your_email@example.com"
    git config --global user.name "Your Name"
    ```
3.  **Create a GitHub Personal Access Token (PAT)**:
    * Go to GitHub `Settings > Developer settings > Personal access tokens > Tokens (classic)`.
    * Generate a new token with `repo` scope. **Copy the token immediately!**
4.  **Update Remote URL with PAT**:
    ```bash
    git remote remove origin
    git remote add origin 
[https://oauth2:YOUR_PERSONAL_ACCESS_TOKEN@github.com/YOUR_USERNAME/YOUR_REPO_NAME.git](https://oauth2:YOUR_PERSONAL_ACCESS_TOKEN@github.com/YOUR_USERNAME/YOUR_REPO_NAME.git)
    ```
    Replace `YOUR_PERSONAL_ACCESS_TOKEN`, `YOUR_USERNAME`, and `YOUR_REPO_NAME`.
5.  **Create/Modify `daily_commit.sh`**: Ensure the `REPO_PATH` is correct for your server. This repository includes the script ready 
for use.
    ```bash
    nano daily_commit.sh
    # (Copy content from this project's daily_commit.sh)
    ```
6.  **Make script executable**:
    ```bash
    chmod +x daily_commit.sh
    ```
7.  **Set up the Cron Job**:
    ```bash
    crontab -e
    ```
    Add the following line (adjusting the path if necessary):
    ```cron
    0 0 * * * /home/YOUR_SERVER_USERNAME/green-contributions/daily_commit.sh >> /home/YOUR_SERVER_USERNAME/green-contributions/cron.log 
2>&1
    ```
    Remember to replace `/home/YOUR_SERVER_USERNAME/green-contributions` with the actual path on your server.
8.  **Perform Initial Push**:
    ```bash
    echo "# Daily Programming Insights" > daily_insight.md
    git add daily_insight.md
    git commit -m "Initial setup for daily programming insights log"
    git push origin master
    ```

## 📜 Daily Insights Log

Check `daily_insight.md` in this repository to see the accumulating collection of programming quotes and thoughts!

---
