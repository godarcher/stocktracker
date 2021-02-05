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

    