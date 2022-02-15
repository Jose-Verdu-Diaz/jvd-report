import os

from jinja2 import Environment, FileSystemLoader

from bs4 import BeautifulSoup


env = Environment(loader = FileSystemLoader('jvd-report'))

input_file = 'index.html'
output_file = 'output.html'

template = env.get_template(input_file)

rendered = template.render()
soup = BeautifulSoup(rendered, 'html.parser')

index_div_ul = soup.find('div', {'id': 'index_div'}).find('ul')
index_div_ul['class'] = index_div_ul('class', []) + ['list-unstyled', 'components mb-5']

nav_sidebar = soup.find('nav', {'id': 'sidebar'})
nav_sidebar.append(index_div_ul)


rendered = soup.prettify(formatter=None)

# write the result to disk in index.html
with open(f'jvd-report/{output_file}', 'w') as ofile:
    ofile.write(rendered)
