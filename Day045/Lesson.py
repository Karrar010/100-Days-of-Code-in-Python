# %%
# from beautifulsoup4 import BeautifulSoup
from bs4 import BeautifulSoup
import requests

# with requests.get('https://www.example.com') as response:
#     soup = BeautifulSoup(response.content, 'html.parser')
#     print(soup.prettify())

with open('website.html') as file:
    content = file.read()
    soup = BeautifulSoup(content, 'html.parser')
    print(soup.prettify())
# %%
print(soup.title) # This print the first title in the HTML file
# %%
print(soup.title.string)
# %%
print(soup.title.name)
# %%
all_anchor_tags = soup.find_all('a') # This will find all the links in the HTML file
print(all_anchor_tags) 
# %%
for tag in all_anchor_tags:
    print(tag.getText()) # This will print the text of each link
    print(tag.get('href')) # This will print the href attribute of each link
# %%
heading = soup.find('h1', id = 'name')
print(heading) # This will find the h1 tags in id called 'name' in the HTML file
# %%
h3_heading = soup.find_all('h3', class_ = 'heading')
print(h3_heading) # This will find all the h3 tags in class called 'heading' in the HTML file
# %%
name = soup.select('#name') # This will find the id called 'name' in the HTML file
print(name) # This will print the id called 'name' in the HTML file
# %%
company_url = soup.select_one(selector='p a') # This will find the first p tag in the HTML file
print(company_url) # This will print the first p tag in the HTML file
# %%

