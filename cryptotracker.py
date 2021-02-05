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

#this functions finds a price of a given crypto currency by parsing a google search
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

#this function notifies the user if a certain crypto_kind goes above a specific treshold
def notifier_crypto(crypto_kind, tresholdup, tresholddown):
    notify = ToastNotifier()
    while True:
        time.sleep(17)
        crypto_price = price_finder(crypto_kind).split(": ")[-1]
        if crypto_price >= tresholdup:
            winsound.Beep(frequency=2700, duration=10000)
            notify.show_toast(f"{crypto_kind} is above set treshold!",
                f"Current price of {crypto_kind} is {crypto_price}", duration=60)
        elif crypto_price <= tresholddown: 
            winsound.Beep(frequency=2700, duration=10000)
            notify.show_toast(f"{crypto_kind} is below set treshold!",
                f"Current price of {crypto_kind} is {crypto_price}", duration=60)
        else:
            continue

###########
#MAIN CODE#
###########
print(price_finder("bitcoin"))
notifier_crypto("bitcoin", "32000", "10000")
