import requests
import csv
import time

# GitHub token for authentication
GITHUB_TOKEN = 'Enter your own'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Step 1: Read user logins from the existing users.csv
def read_user_logins(filename='users.csv', max_users=500):
    logins = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            if i < max_users:  # Only get the first 500 users
                logins.append(row['login'])
            else:
                break
    return logins

# Step 2: Fetch up to 500 repositories for each user login
def fetch_user_repositories(username, max_repos=500):
    repos = []
    repos_url = f'https://api.github.com/users/{username}/repos?sort=pushed&per_page=100'

    while repos_url and len(repos) < max_repos:
        response = requests.get(repos_url, headers=HEADERS)
        if response.status_code == 200:
            repos.extend(response.json())
            repos_url = response.links.get('next', {}).get('url')
            time.sleep(1)  # Avoid rate limiting
        else:
            print(f"Error fetching repositories for {username}: {response.status_code}")
            break

    return repos[:max_repos]  # Ensure it doesn't exceed 500 repositories

# Step 3: Write repositories data to repositories.csv
def save_repositories_to_csv(user_logins, filename='repositories.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count',
                         'language', 'has_projects', 'has_wiki', 'license_name'])

        for username in user_logins:
            repos = fetch_user_repositories(username)
            for repo in repos:
                license_name = repo.get('license').get('key') if repo.get('license') else ''
                writer.writerow([
                    username, repo['full_name'], repo.get('created_at', ''),
                    repo.get('stargazers_count', ''), repo.get('watchers_count', ''),
                    repo.get('language', ''), str(repo.get('has_projects', '')).lower(),
                    str(repo.get('has_wiki', '')).lower(), license_name
                ])

# Main function to execute the code
def main():
    user_logins = read_user_logins()  # Read first 500 user logins from users.csv
    save_repositories_to_csv(user_logins)  # Generate repositories.csv

if __name__ == "__main__":
    main()
