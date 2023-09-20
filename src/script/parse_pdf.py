import requests
import pandas as pd
from bs4 import BeautifulSoup
from tabula import read_pdf
import weasyprint
# https://doc.courtbouillon.org/weasyprint/stable/first_steps.html#installation
# import ssl
# ssl._create_default_https_context = ssl._create_unverified_context


def download_pdf(url, filename):
    menue_page = requests.get(url)
    with open(filename, 'wb+') as f:
        f.write(menue_page.content)

def parse_pdf(filename):
    df = read_pdf(filename, pages='1', lattice=True , multiple_tables=True)[0]
    # TODO sanitize and prep df (remove the  nulls and shit)
    #       ~ look into data frame flattening
    print(df)
    print(df.columns)

def website_to_pdf(url, outfile):
    pdf = weasyprint.HTML(url).write_pdf()
    open(outfile, 'wb').write(pdf)


def download_website(url, filename):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    with open(filename, "wb+") as f:
        f.write(page.content)

download_website("https://dining-caltech-edu.my.canva.site/browne-comfort-equation", "comfort.html")