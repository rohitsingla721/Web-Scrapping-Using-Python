# scrapping - APIs / HTML using bs4
# install
# pip install requests
# pip install html5lib
# pip install bs4
# step get  HTML ,PARSE HTML, TREE TRAVERSAL HTML
import requests
from bs4 import BeautifulSoup 
# step 1 Get the html
url="https://codewithharry.com"
r = requests.get(url)
htmlcontent=r.content
# print(htmlcontent)
# Step 2 Parse the html
soup=BeautifulSoup(htmlcontent,'html.parser')
#print(soup.prettify())
# step 3 HTML tree traversal
title=soup.title
# get title of html page
print(title)
paragraph=soup.find_all('p')
print(paragraph)