import os
from bs4 import BeautifulSoup as bs

html = open('evilcorp.html')
soup = bs(html, 'html.parser')

new_title = soup.new_tag("title")
new_title.string = "Evil Corp - Stealing your money every day"
soup.title.replace_with(new_title)

name_found = soup.find("span", {"class": "name"})
replaced_block = soup.find("p")
new_block = soup.new_tag("h1")
new_block.string = f'{name_found.text}, you are hacked!'
replaced_block.replace_with(new_block)

with open("script.js", "r") as sf:
    new_script = soup.new_tag("script")
    new_script.string = sf.read()
    soup.head.append(new_script)

soup.a['href'] = soup.a['href'].replace('E_Corp','Fsociety')
soup.a.string = soup.a.string.replace('Evil Corp','Fsociety')

with open("evilcorp_hacked.html", "w") as f:
    f.write(str(soup))

