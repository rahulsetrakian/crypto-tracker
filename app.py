__author__ = 'Rahul Setrakian'

import requests
from bs4 import BeautifulSoup
from os import system
from time import sleep

try:
    sys = system

    # code for parsing the price of crypto

    def price_of_crypto():
        sys('cls')
        try:
            select_crypto = input('Please write the name of crypto(in lowercase): ')
            url = "https://coinmarketcap.com/currencies/"+select_crypto+'/'
            req = requests.get(url)
            content = req.content
            soup = BeautifulSoup(content, 'html.parser')
            web_element = soup.find("div", {"class": "heading"}).text
            if str(web_element) == 'Links':
                print('Valid Option.')
        except AttributeError:
                print("Invalid Option.")
                sleep(2)
                price_of_crypto()
        web_element = soup.find("div", {"class": "priceValue"})
        usd = float(web_element.text[1:].replace(',',''))
        req = requests.get("https://markets.businessinsider.com/currencies/usd-inr")
        content = req.content
        soup = BeautifulSoup(content, "html.parser")
        web_element = soup.find("span", {"class": "price-section__current-value"})
        inr = web_element.text.split('.')
        inr_mod = float(inr[0])
        price = usd * inr_mod
        sys('cls')
        price = "The price of {} is {} ₹".format(select_crypto, price)
        print(price.upper())
        return price

    def price_of_crypto_in_realtime():
        sys('cls')
        select_crypto = input('Please write the name of crypto(in lowercase): ')
        var = 1
        while var == 1:
            try:
                url = "https://coinmarketcap.com/currencies/"+select_crypto+'/'
                req = requests.get(url)
                content = req.content
                soup = BeautifulSoup(content, 'html.parser')
                web_element = soup.find("div", {"class": "heading"}).text
                if str(web_element) == 'Links':
                    print('Valid Option.')
            except AttributeError:
                print("Invalid Option.")
                sleep(2)
                price_of_crypto_in_realtime()
            web_element = soup.find("div", {"class": "priceValue"})
            usd = float(web_element.text[1:].replace(',',''))
            req = requests.get("https://markets.businessinsider.com/currencies/usd-inr")
            content = req.content
            soup = BeautifulSoup(content, "html.parser")
            web_element = soup.find("span", {"class": "price-section__current-value"})
            inr = web_element.text.split('.')
            inr_mod = float(inr[0])
            price = usd * inr_mod
            sys('cls')
            price = "The price of {} is {} ₹".format(select_crypto, price)
            print(price.upper())
            print('To close the program press (CTRL + C).')
            sleep(5)
            sys('cls')
        return price


    def choose_option():
        intro = open('logo.txt','r')
        description = '\n\n\nThis program track the real-time price of cryptocurrencies. \n \n [1.] Live Price Tracking \n\n [2.] Get Me Latest Price' 
        sys('cls')
        print(intro.read(),description)
        anwser = input("\nSelect option: ")
        if anwser == '1':
            sys("cls")
            print("Initiating Live Tracking.")
            price_of_crypto_in_realtime()
        elif anwser == '2':
            sys("cls")
            print("Getting The Live Price.")
            price_of_crypto()
            
        else:
            print('Invalid Option.')
            sleep(2)
            choose_option()


    choose_option()

except KeyboardInterrupt:
    exit()