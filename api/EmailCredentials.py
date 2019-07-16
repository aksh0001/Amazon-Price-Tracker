"""
Class containing information about user's email credentials

@author a.k
"""


class EmailCredentials(object):
    def __init__(self, email_ad: str, email_uname: str, email_pw: str):
        self.e_address = email_ad
        self.e_uname = email_uname
        self.e_pw = email_pw

    def get_e_address(self) -> str:
        return self.e_address

    def get_e_uname(self) -> str:
        return self.e_uname

    def get_e_pw(self) -> str:
        return self.e_pw
