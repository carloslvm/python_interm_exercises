#!/usr/bin/env python3

# Most Popular Java Projects on GitHub

import requests
import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS

# Make an API call and store the response
url = "https://api.github.com/search/repositories?q=language:java&sort=stars"

req = requests.get(url)
print("Status Code: ", req.status_code) # Checking access

# Store API response in a variable
response_dict = req.json()
print("Total repositories:", response_dict['total_count'])

# Explore information about the repositories
repo_dicts = response_dict['items']
#print("Repositories returned:", len(repo_dicts))
print("Number of items:", len(repo_dicts))
#names, stars =[],[]
projects, plot_dicts = [], []
for repo_dict in repo_dicts:
    projects.append(repo_dict['name'])
    #stars.append(repo_dict['stargazers_count'])
    
    plot_dict = {
            'value':repo_dict['stargazers_count'],
            'label':str(repo_dict['description']),
            'xlink':repo_dict['html_url'],
            }

    plot_dicts.append(plot_dict)


# Visualization
my_style = LS('#333366', base_style=LCS)
#chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)

# Chart configuration
my_config = pygal.Config()
my_config.x_label_rotation = 45
my_config.show_legend = False
my_config.title_font_size = 24
my_config.label_font_size = 14
my_config.major_label_font_size = 18
my_config.truncate_label = 15
my_config.show_y_guides = False
my_config.width = 1000


chart = pygal.Bar(style=my_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most-Starred Java Projects on Github'
chart.x_labels = projects
chart.add('Stars and Description', plot_dicts)
chart.render_to_file('java_repos.svg')


# First repository
#repo_dict = repo_dicts[0]
#print("\nKeys:", len(repo_dict))
#for key in sorted(repo_dict.keys()):
#    print(key)

#print("\nSelected information about each repository:")
#
#for repo_dict in repo_dicts:
#    print('Name:', repo_dict['name'])
#    print('Owner:', repo_dict['owner']['login'])
#    print('Stars:', repo_dict['stargazers_count'])
#    print('Repository:', repo_dict['html_url'])
#    print('Created:', repo_dict['created_at'])
#    print('Updated:', repo_dict['updated_at'])
#    print('Description:', repo_dict['description'])
