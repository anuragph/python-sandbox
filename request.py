import requests
import json
from datetime import datetime

# Get projects from GitLab:
# gitlab_response = requests.get('https://gitlab.com/api/v4/users/dwt1/projects')
# project_list = gitlab_response.json()

# for project in project_list:
#   print(f'Project Name: {project.get("name")}\nProject URL: {project.get("web_url")}\n')


# Get repositories list from GitHub API
github_response = requests.get('https://api.github.com/users/anuragph/repos')
repo_list = github_response.json()

for repo in repo_list:
  print(f'Repo Name: {repo["name"]}\nRepo link: {repo["html_url"]}\n')


# Get available vaccination centers using Co-WIN API
pincode = 110001
today_date = datetime.today().strftime('%d-%m-%Y')
cowin_response = requests.get(f'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByPin?pincode={pincode}&date={today_date}')

data = cowin_response.json() # dictionary
centers = data['sessions'] # list of dictionaries

for center in centers:
  center_name = center['name']
  print(center_name)