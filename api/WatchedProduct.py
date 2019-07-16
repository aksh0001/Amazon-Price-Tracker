"""
Class containing information about a watched product

@author a.k
"""
from decimal import Decimal


class Product(object):
    def __init__(self, prod_url: str, price: Decimal):
        self.product_url = prod_url
        self.watched_price = price

    def get_prod_url(self) -> str:
        return self.product_url

    def get_watched_price(self) -> Decimal:
        return self.watched_price
