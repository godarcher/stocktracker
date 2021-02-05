##############
#DEPENDENCIES#
##############

import time
import requests
import winsound

from bs4 import BeautifulSoup
from win10toast import ToastNotifier

###########
#FUNCTIONS#
###########

def price_finder(crypto_kind):
    #we create a google query url with the crypto input
    gurl =  "https://www.google.com/search?q=" + crypto_kind + "+price"

    #we fetch in html
    HTML = requests.get(gurl)

    #we use bs4 to parse the HTML content
    soup = BeautifulSoup(HTML.text, "html.parser")

    price = soup.find("div", attrs={"class": "BNeawe iBp4i AP7Wnd"}).find("div",
                             attrs={'class':'BNeawe iBp4i AP7Wnd'}).text.split(" ")
    
    return str(f"{crypto_kind}: {price[0]}")