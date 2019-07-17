import argparse, time
from decimal import Decimal
from api.WatchedProduct import Product
from api.WatchService import WatchService
from api.EmailCredentials import EmailCredentials

parser = argparse.ArgumentParser()
parser.add_argument('-url', '--produrl', required=True, type=str, help='The amazon product URL')
parser.add_argument('-p', '--price', required=True, type=Decimal, help='The target watch price')


def main(args: argparse.Namespace):
    wp = Product(args.produrl, args.price)
    e_address = input("Enter Email Address: ")  # Require user to enter their email credentials
    e_uname = input("Enter Email user name: ")
    e_pw = input("Enter Email password: ")
    ec = EmailCredentials(e_address, e_uname, e_pw)
    ws = WatchService(wp, ec)
    while True:
        ws.check_price()
        time.sleep(24 * 60 * 60)  # Check every 24 hours


if __name__ == "__main__":
    args = parser.parse_args()
    main(args=args)
