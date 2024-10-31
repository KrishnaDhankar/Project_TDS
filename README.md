# GitHub Users and Repositories Analysis

- **Data Scraping Approach**: Leveraged GitHub's REST API to gather information on users in Shanghai with over 200 followers and details on their repositories.
- **Interesting Finding**: A surprising number of users have high follower counts but lower engagement with their repositories, indicating more observational than active contributions.
- **Developer Insight**: Active contributions to open-source projects can significantly enhance visibility and professional networking within the developer community.

### How the Script Works

1. **Data Collection**: The script utilizes GitHub's REST API to identify and collect user data for accounts with over 200 followers in Shanghai.
2. **User and Repository Data**: For each identified user, the script retrieves profile details and up to 500 of their most recent repositories.
3. **Data Cleaning and CSV Export**: The data undergoes cleaning, with company names standardized to remove extraneous symbols, and is then exported into `users.csv` and `repositories.csv` for analysis.

### Files in the Repository

- **users.csv**: Contains details on GitHub users, including login, name, company, location, email, bio, repository count, and follower/following statistics.
- **repositories.csv**: Includes repository details like the repository name, creation date, star count, watcher count, primary language, and license type.
- **script.py**: The Python script used for fetching, cleaning, and exporting the GitHub data.

### Usage

To replicate the data collection, use your own GitHub Personal Access Token by replacing the placeholder in `script.py` with your token, then run the script in a Python environment.

--- 

This `README.md` provides a clear overview of the project, including what was done, insights from the analysis, and recommendations for developers. Let me know if you'd like any additional sections or details!
