"""
This class contains implementations of email sending notifications

@author a.k
"""
from api.EmailCredentials import EmailCredentials
from api.WatchedProduct import Product
import requests, smtplib
from bs4 import BeautifulSoup
from decimal import Decimal
from email.mime.text import MIMEText
from re import sub


class WatchService(object):
    def __init__(self, product: Product, creds: EmailCredentials):
        self.watched_product = product
        self.email_creds = creds

        self.page = requests.get(product.get_prod_url(), headers=WatchService.query_user_agent_headers())  # make call
        soup_tmp = BeautifulSoup(self.page.content, 'html.parser')
        self.soup = BeautifulSoup(soup_tmp.prettify(), 'html.parser')
        self.title = self.soup.find(id='productTitle').get_text().strip()
        price = sub(r'[^\d.]', '', (self.soup.find(id='priceblock_ourprice').get_text()))
        self.conv_price = Decimal(price.strip())

    def check_price(self):
        if self.conv_price < self.watched_product.get_watched_price():
            self.send_email()

    def send_email(self):
        server = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(self.email_creds.get_e_uname(), self.email_creds.get_e_pw())
        server.set_debuglevel(1)
        body = "Good day!\nHere is your product: " + self.watched_product.get_prod_url()
        msg = MIMEText(body)
        sender = self.email_creds.get_e_address()  # Send to self
        recipients = self.email_creds.get_e_address()
        msg['Subject'] = "Your: " + self.title + " Is now $" + str(self.conv_price) + "!"
        msg['From'] = sender
        msg['To'] = recipients
        server.sendmail(sender, recipients.split(','), msg.as_string())
        print("Sent!")

    @staticmethod
    def query_user_agent_headers() -> dict:
        header = {'User-Agent': input(
            "Please enter your user agent header. This can be found by searching ""what's my user agent"": ")}
        return header
