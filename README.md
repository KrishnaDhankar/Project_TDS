
# GitHub Users and Repositories Analysis

- **Data Scraping Approach**: I utilized GitHub's REST API to dive deep into the vibrant developer community in Shanghai, targeting users with over 200 followers to understand their activity and projects.
  
- **Interesting Finding**: It was surprising to discover that many developers in Shanghai are avid followers of popular repositories but contribute less frequently. This suggests that while they are engaged, there is room for deeper involvement.

- **Developer Insight**: I recommend that developers actively engage with open-source projects and contribute to discussions. This not only enhances their visibility in the community but also provides invaluable learning experiences and networking opportunities.

### How the Script Works

1. **Data Collection**: The script connects to GitHub's REST API to identify users in Shanghai who have a following of more than 200. This helps spotlight active community members.
2. **User and Repository Data**: For each identified user, I fetched their public profile and their most recent repositories—capping at 500—to get a comprehensive view of their contributions and interests.
3. **Data Cleaning and CSV Export**: The collected data was cleaned to ensure consistency, especially in company names, and then exported into two CSV files—`users.csv` and `repositories.csv`—for easy analysis.

### Files in the Repository

- **users.csv**: This file captures essential details about GitHub users, such as their usernames, names, companies, locations, email addresses, short bios, and statistics on their repositories and followers.
- **repositories.csv**: Here, you'll find detailed information about each user’s repositories, including repository names, creation dates, star and watcher counts, programming languages, and license types.
- **script.py**: This is the heart of the project—the Python script that orchestrates the data fetching, cleaning, and exporting processes.

### Conclusion

By analyzing this data, we gain insights not just into the users but also the broader trends within the developer community in Shanghai. Encouraging active participation in projects could foster collaboration and innovation.

---
