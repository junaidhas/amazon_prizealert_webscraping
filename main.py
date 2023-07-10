from bs4 import BeautifulSoup
import lxml

import requests
import smtplib

URL = "https://AN AMAZON PRODUCT link"
AMAZON_HEADERS = {
    "User-Agent":"Defined",
    "Accept-Language":"en-US,en;q=0.9"
}

EMAIL = "learnerpython97@gmail.com"
PASSWORD = "APP_PASSWORD"

response = requests.get(URL,headers=AMAZON_HEADERS)
AMAZON_html = response.text

soup = BeautifulSoup(AMAZON_html,"lxml")
# print(soup)

current_price = float(soup.find(name="span",class_="a-offscreen").text.strip("$"))

print(current_price)
print(type(current_price))

# I was checking a asics running shoes , Its current prize is 69$ CA, 
# I cross checked the shoe on camelcamelcamel.com website, 
# this shoe usually costs 100-130$ in last 16 months
# get an email, whenever this shoes proze is less than 80 $

BUY_PRIZE = 80

if current_price < BUY_PRIZE:
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(EMAIL,PASSWORD)
        connection.sendmail(
            from_addr=EMAIL,
            to_addrs=EMAIL,
            msg=f"subject: Asics running shoe prize alert \n\n ASICS Men's GT-1000 9 Running Shoes is now CA${current_price}, HURRY UP!!!".encode("utf-8")
        )
    #when using for the first time you will get smtplib.SMTPAuthenticationError
    # to avoid it activate two step verifaction in the google account
    # then search for APP password in the search bar, select other app --> then copy the pwd and paste in place of the password here
    # add port = 857 and .encode("UTF-8")
