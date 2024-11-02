#Run this Code in Google Colab and Generate your Personal Token for Github API and feel free to suggest any improvements
import requests
import csv
import re
import time

# GitHub token for authentication
GITHUB_TOKEN = 'your_github_token'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Step 1: Fetch users in Shanghai with over 200 followers
def fetch_users(location='Shanghai', min_followers=200):
    users = []
    url = f'https://api.github.com/search/users?q=location:{location}+followers:>{min_followers}&per_page=100'
    
    while url:
        response = requests.get(url, headers=HEADERS)
        if response.status_code == 200:
            data = response.json()
            users.extend(data['items'])
            url = response.links.get('next', {}).get('url')  
            time.sleep(1) 
        else:
            print(f"Error fetching users: {response.status_code}")
            break
    return users

# Step 2: Fetch each user's additional data and their repositories
def fetch_user_details_and_repos(username, max_repos=500):
    # Fetch user details
    user_url = f'https://api.github.com/users/{username}'
    user_data = requests.get(user_url, headers=HEADERS).json()
    
    # Fetch user's repositories (up to max_repos, sorted by most recently pushed)
    repos_url = f'https://api.github.com/users/{username}/repos?sort=pushed&per_page=100'
    repos = []
    while repos_url and len(repos) < max_repos:
        response = requests.get(repos_url, headers=HEADERS)
        if response.status_code == 200:
            repos.extend(response.json())
            repos_url = response.links.get('next', {}).get('url')
            time.sleep(1)  # Avoid rate limiting
        else:
            print(f"Error fetching repositories for {username}: {response.status_code}")
            break
    return user_data, repos[:max_repos]

# Step 3: Clean and process company names
def clean_company_name(company):
    if company:
        company = company.strip()
        company = re.sub(r'^@', '', company, count=1)
        return company.upper()
    return ""

# Step 4: Write user data to users.csv
def save_users_to_csv(users_data, filename='users.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'name', 'company', 'location', 'email', 'hireable', 'bio', 
                         'public_repos', 'followers', 'following', 'created_at'])
        
        for user in users_data:
            writer.writerow([
                user.get('login', ''), user.get('name', ''), clean_company_name(user.get('company', '')), 
                user.get('location', ''), user.get('email', ''), str(user.get('hireable', '')).lower(),
                user.get('bio', ''), user.get('public_repos', ''), user.get('followers', ''), 
                user.get('following', ''), user.get('created_at', '')
            ])

# Step 5: Read user logins from users.csv
def read_user_logins(filename='users.csv', max_users=500):
    logins = []
    with open(filename, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for i, row in enumerate(reader):
            if i < max_users:
                logins.append(row['login'])
            else:
                break
    return logins

# Step 6: Write repositories data to repositories.csv
def save_repositories_to_csv(user_logins, filename='repositories.csv'):
    with open(filename, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['login', 'full_name', 'created_at', 'stargazers_count', 'watchers_count',
                         'language', 'has_projects', 'has_wiki', 'license_name'])

        for username in user_logins:
            _, repos = fetch_user_details_and_repos(username)
            for repo in repos:
                license_name = repo.get('license', {}).get('key', '')
                writer.writerow([
                    username, repo['full_name'], repo.get('created_at', ''),
                    repo.get('stargazers_count', ''), repo.get('watchers_count', ''),
                    repo.get('language', ''), str(repo.get('has_projects', '')).lower(),
                    str(repo.get('has_wiki', '')).lower(), license_name
                ])


def main():
    # Step 1: Fetch and save users in Shanghai with over 200 followers
    users_data = fetch_users()
    save_users_to_csv(users_data)
    print("User data saved to users.csv")
    
    # Step 2: Read user logins from users.csv and save their repositories to repositories.csv
    user_logins = read_user_logins()
    save_repositories_to_csv(user_logins)
    print("Repository data saved to repositories.csv")

if __name__ == "__main__":
    main()
