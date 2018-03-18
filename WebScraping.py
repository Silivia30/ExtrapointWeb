#!/usr/bin/env python

#import libraries
import urllib.request
from bs4 import BeautifulSoup;
import smtplib
import sys

# url 'https://www.packtpub.com/packt/offers/free-learning/'

class WebScraping(object):

    def book_search(self):
        html = self.web('https://www.packtpub.com/packt/offers/free-learning/')
        book = self.parse(html)
        msg = self.message(book)

        #user gmail
        userID = sys.argv[1]
        userPWD = sys.argv[2]

        #list of email_id to send the mail
        li = ["silivia30@gmail.com", "gvidalviles@gmail.com"]
        try:
            for i in li:
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(userID, userPWD)
                s.sendmail(userID, i, msg)
                s.quit()
        except:
            print("invalid user or password")

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
        book_info["Title"] = info[1].text.strip()
        book_info["Description"] = info[2].text.strip()
        book_info["Sub_description"] = info[3].text.strip()
        return book_info

    def message(self, book_info):
        msg = "\nFREE BOOK TODAY: \n" + str(book_info["Title"]) + "\n \n" + "DESCRIPTION: \n" + str(book_info["Description"]) + "\n" + "[" + str(book_info["Sub_description"]) + "]\n \nGET IT: https://www.packtpub.com/packt/offers/free-learning"
        return msg

if __name__ == "__main__":
    if len (sys.argv)!=3 :
        print("Insert gmail user and password")
    else :
        webScraping = WebScraping()
        webScraping.book_search()