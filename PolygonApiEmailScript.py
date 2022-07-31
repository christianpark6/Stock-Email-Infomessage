import requests
import smtplib as smtp
from email.mime.text import MIMEText
##Below are defining variables that will be necessary for requesting the information from polygon.io.
##These include things like the api key, base url, and having the user input the ticker symbol and date of interest.
API_KEY = 'API KEY' ##Retrieve API Key From Polygon.io which you can obtain for free by signing up.
BASE_URL = 'https://api.polygon.io/v1/open-close'
ticker = input("Enter stock ticker: ")
DATE = input("Enter Date in year-month-date: ")

##This request line helps request the information based on information you would put in including what ticker symbol you input and the date.
requests_url = f'{BASE_URL}/{ticker}/{DATE}?adjusted=true&apiKey={API_KEY}'
response = requests.get(requests_url)

##This if statement helps allow the information to get stored to a .json file which we labeled as data.
##If the status code is 200 (meaning success) the information pulled using the Web api will get stored into variables.
##If the status code is not 200, the program will just print "Error"
if response.status_code == 200:
    data = response.json()
    Date = data['from']
    Symbol = data['symbol']
    PriceOpen = data['open']
    PriceClose = data['close']
    PriceHigh = data['high']
    PriceLow = data['low']

else:
    print("Error")

##Below is setting up  and sending the email.
recipient = input('Type In Recipient Email here: ')
server = smtp.SMTP_SSL("smtp.gmail.com", 465)
serverEmail = "Enter your email here"
serverPw = "Enter your password here"
server.login(serverEmail, serverPw)
subject = "Daily Stock Update"
body = f'Date: {Date} \nTicker: {Symbol}  \nOpen Price: {PriceOpen} \nClosing Price: {PriceClose} \nHigh Price: {PriceHigh} \nLow Price: {PriceLow}'
message = f'Subject: {subject}\n\n{body}'
server.sendmail(serverEmail, recipient, message)
server.quit()