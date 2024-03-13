from urllib.request import urlretrieve
from urllib import error
import os

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def download_file(url):
        try:
            urlretrieve(url, 'currencies.csv')
        except error.URLError as err:
            raise(err)
        return 'Success'