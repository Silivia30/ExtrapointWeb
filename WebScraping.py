#!/usr/bin/env python

#import libraries
import urllib.request
from bs4 import BeautifulSoup;

# url 'https://www.packtpub.com/packt/offers/free-learning/'

class WebScraping(object):

    def book_search(self):
        html = self.web('https://www.packtpub.com/packt/offers/free-learning/')
        book = self.parse(html)

    def web(self, webpage):
        page = urllib.request.urlopen(webpage)
        html = page.read()
        page.close()
        return html

    def parse(self, html):
        book_info = {}
        soup = BeautifulSoup(html, "html.parser")
        soup = soup.find("div", class_="dotd-main-book-summary")
        info = soup.find_all("div")
        book_info["Tittle"] = info[1].text.strip()
        book_info["Description"] = info[2].text.strip()
        return book_info

    def message(self, book_info):
        msg = ""
        return msg

if __name__ == "__main__":
    webScraping = WebScraping()
    webScraping.book_search()