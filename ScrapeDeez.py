from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://oldschool.runescape.com').text
# print(html_text)

soup = BeautifulSoup(html_text, 'lxml')
update = soup.find('article', class_='news-article')
print(update)
href = update.find('a', href=True).get("href")
print(href)

article_text = requests.get(href).text
soup2 = BeautifulSoup(article_text, 'lxml')
print(article_text)

paragraphs = soup2.findAll('p')
updates = href
# file = open('file.txt', 'w', encoding='utf-8')
# for tag in paragraphs:
#    updates.append(tag.text.strip())

# print(updates)
