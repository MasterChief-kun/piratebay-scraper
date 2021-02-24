from selenium import webdriver
from bs4 import BeautifulSoup as bs
from prettytable import PrettyTable
import webbrowser

options = webdriver.FirefoxOptions()
options.headless = True
tv_show = input('Do you want to download a movie or a TV Show(movie/tv/others): ')
if tv_show == 'movie':
    query = input('Please enter name of the movie: ')
    link = 'https://piratebay.ml/search.php?q=' + query.replace(' ', '+') + '&cat=201'
elif tv_show == 'tv':
    query = input('Please enter name of the TV Show: ')
    link = 'https://piratebay.ml/search.php?q=' + query.replace(' ', '+') + '&cat=205'
elif tv_show == 'others':
    query = input('Please enter name of the thing: ')
    link = 'https://piratebay.ml/search.php?q=' + query.replace(' ', '+')
driver = webdriver.Firefox(options=options)
driver.get(link)
content = driver.page_source
soup = bs(content, 'html.parser')
ol = soup.find('ol', attrs={'id':'torrents'})
all_items = ol.find_all('li', attrs={'class':'list-entry'})
table = PrettyTable()
table.field_names = ['S. No.', 'Name', 'Size']
count = 1
links = []
table.add_row([0, 'Exit', ''])
for x in all_items:
    temp = x.find('span', attrs={'class': 'list-item item-name item-title'})
    name = temp.find('a').get_text()
    size = x.find('span', attrs={'class': 'list-item item-size'}).get_text()
    table.add_row([count, name, size])
    temp = x.find('span', attrs={'class': 'item-icons'})
    link = temp.find('a').get('href')
    links.append(link)
    count = count + 1
print(table)
choice = int(input('Please enter number corresponding to your choice: ')) - 1
if choice == -1:
    exit()
else:
    chosen_link = links[choice]
    webbrowser.open(chosen_link, new=2)
