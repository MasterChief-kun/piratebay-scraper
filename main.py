from selenium import webdriver
from bs4 import BeautifulSoup as bs

options = webdriver.ChromeOptions()
options.headless = True
game_name = input("Please enter name of the game: ")
game_name = game_name.replace(' ', '+')
link = "https://piratebay.ml/search.php?q=" + game_name + '&cat=401'
print('Headless Chrome Initialised')
driver = webdriver.Chrome(options=options)
driver.get(link)
content = driver.page_source
soup = bs(content, 'html.parser')
game_entry = soup.find('li', attrs={'class':'list-entry'})
span = game_entry.find('span', attrs={'class':'item-icons'})
link = span.find('a').get('href')
print(link) 
