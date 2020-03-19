#!/usr/bin/env python3

# Working with Hacker News API

import pygal
from pygal.style import LightColorizedStyle as LCS, LightenStyle as LS
import requests
from operator import itemgetter

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print("Status code:", r.status_code)

# Process information about each submission
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:30]:
    url = ('https://hacker-news.firebaseio.com/v0/item/' 
        + str(submission_id) + '.json')
    submission_r = requests.get(url)
    print('Status code:', submission_r.status_code)
    response_dict = submission_r.json()

    submission_dict = {
            'title':response_dict['title'],
            'link':'https://news.ycombinator.com/item?id=' 
            + str(submission_id),
            'comments':response_dict.get('descendants', 0)
            }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
        reverse=True)

titles, plot_bar = [], []
for submission_dict in submission_dicts:
    #print("\nTitle:", submission_dict["title"])
    titles.append(submission_dict["title"])
    #print("Discussion link:", submission_dict['link'])
    #print("Comments:", submission_dict['comments'])
    
    bar_data = {
            'value':submission_dict['comments'],
            'label':submission_dict['title'],
            'xlink':submission_dict['link'],
            }
    plot_bar.append(bar_data)


# Visualization
chart_style = LS('#BB1E31', base_style=LCS)

chart_config = pygal.Config()
chart_config.x_label_rotation = 45
chart_config.show_legend = False
chart_config.title_font_size = 24
chart_config.label_font_size = 14
chart_config.major_label_font_size = 18
chart_config.truncate_label = 15
chart_config.show_y_guides = False
chart_config.width = 1000

chart = pygal.Bar(style=chart_style, x_label_rotation=45, show_legend=False)
chart.title = 'Most Commented Articles On Hacker News'
chart.x_labels = titles
chart.add('', plot_bar)
chart.render_to_file('hnews.svg')
