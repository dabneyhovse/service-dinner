import requests
import pandas as pd

from bs4 import BeautifulSoup
from tabula import read_pdf

# File path shit
TEMP_FILE = "temp.pdf"
DIR = "./temp/"
FULL_PATH = DIR+TEMP_FILE

# Menu link text
LINK_TEXT = "This Week's Specials!"
URL = "https://dining.caltech.edu/where-to-eat-"

# load page and focus on dining hall
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="browne-dining-hall-a2962b99")

# sift through the links for what we want
links = results.find_all("a")
# link = filter(lambda L : L.text.strip() == LINK_TEXT, links)
link = [L.text for L in links ]#if L.text.strip() == LINK_TEXT]
print(len(link))

print(link[0])
menue_url = "https://dining.caltech.edu"+link["href"]

menue_page = requests.get(menue_url)
with open(FULL_PATH, 'wb+') as f:
    f.write(menue_page.content)

df = read_pdf(FULL_PATH, pages='1', lattice=True , multiple_tables=True)[0]
print(df)

# TODO sanitize and prep df (remove the  nulls and shit)
#       ~ look into data frame flattening

print(df.columns)




# def download_pdf(url):
#     menue_page = requests.get(url)
#     with open(FULL_PATH, 'wb+') as f:
#         f.write(menue_page.content)

# def parse_pdf():
#     df = read_pdf(FULL_PATH, pages='1', lattice=True , multiple_tables=True)[0]
#     # TODO sanitize and prep df (remove the  nulls and shit)
#     #       ~ look into data frame flattening
#     print(df)
#     print(df.columns)
