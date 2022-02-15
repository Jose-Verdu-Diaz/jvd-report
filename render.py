import os

from jinja2 import Environment, FileSystemLoader

from bs4 import BeautifulSoup


env = Environment(loader = FileSystemLoader('jvd-report'))

input_file = 'index.html'
output_file = 'output.html'

template = env.get_template(input_file)

rendered = template.render()
soup = BeautifulSoup(rendered, 'html.parser')

# Add Title
title = soup.find('h1', {'id': 'title'}).extract()
soup.find('h1', {'id': 'report_title'}).append(title.text)
soup.find('title').append(title.text)
soup.find('a', {'id': 'title_link'}).append(title.text)

# Add Table of Contents
index_div_ul = soup.find('div', {'id': 'index_div'}).find('ul')
index_div_ul['class'] = index_div_ul('class', []) + ['list-unstyled', 'components mb-5']
nav_sidebar = soup.find('nav', {'id': 'sidebar'})
nav_sidebar.append(index_div_ul)

# Remove Input Prompt
for div in soup.find_all("div", {'class':['jp-InputPrompt', 'jp-InputArea-prompt']}): div.decompose()

# Remove Output Prompt
for div in soup.find_all("div", {'class':['jp-OutputPrompt', 'jp-OutputArea-prompt']}): div.decompose()


rendered = soup.prettify(formatter=None)

# write the result to disk in index.html
with open(output_file, 'w') as ofile:
    ofile.write(rendered)
