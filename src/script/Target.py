import requests
import mimetypes
import pandas as pd
import re
from urllib.parse import urljoin


import asyncio
from pyppeteer import launch

from bs4 import BeautifulSoup

DEFAULT_MESSAGE = "Could not locate the item on dining.caltech.edu, perhaps there were changes to their site"

class Target:
    def __init__(self, key, text, page_url):
        self.key = key
        self.text = text
        self.page_url = page_url
        self.url = None
        self.text_full = DEFAULT_MESSAGE

    def __str__(self) -> str:
        return f"Target(\n\tkey='{self.key}',\n\ttext='{self.text}',\n\tpage_url='{self.page_url}',\n\turl='{self.url}',\n\ttext_full='{self.text_full}'\n\t)"

    def scrape(self):
        '''
        GET the page_url, load into bs4 and
        scrape for the information we want to fill out
        '''
        page = requests.get(self.page_url)
        soup = BeautifulSoup(page.content, "html.parser")

        self.find_element(soup)


    def find_element(self, soup):
        '''
        Find element on the page that has the given text in it

        we search for it like this, as its easiest to maintain
        in the case of a style change on the dining.caltech.edu
        website.

        If theres a change you just have to change the target text

        No need to do annoying per link scraping to find things
        '''
        res = soup.find(string=re.compile(self.text))
        if res is not None:
            self.text_full = res.text
            self.find_parent_link(res)

    def find_parent_link(self, text_elem):
        '''
        Traverse upwards to check if this element is contained
        in a link (a tag)
        '''
        curr = text_elem

        res = curr.findParent(name="a")
        if res is not None:
            self.url = res["href"]
            # make any relative "/document" paths absolute
            self.url = urljoin("https://dining.caltech.edu/", self.url)

    def check_type(self):
        response = requests.get(self.url)
        content_type = response.headers['content-type']
        extension = mimetypes.guess_extension(content_type)
        return extension

    async def screenshot(self):
        if self.url is None:
            # todo copy over a error image or smth
            return
        if self.check_type() == ".pdf":
            # pupeteer doesnt like loading pdfs for screenshots
            # just download and process pdf normally
            return

        # open headless browser and go to the page
        browser = await launch({"autoClose":False})
        page = await browser.newPage()

        # aribtrary size until it actually gets the entire thing
        scale = 1.3
        await page.setViewport({ 'width': int(1280 * scale), 'height': int(720*scale) });
        await page.goto(self.url, {
            "waitUntil": 'networkidle2'
        })

        # take screenshot and leave
        await page.screenshot({'path': f'public/images/{self.key}.png', "fullPage": True})
        await browser.close()