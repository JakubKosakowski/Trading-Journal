from urllib.request import urlretrieve
from urllib import error
import os

class Utils:
    def __init__(self):
        pass

    @staticmethod
    def download_file(url, filename, destination='./config'):
        try:
            urlretrieve(url, f'{destination}/{filename}')
        except (error.URLError) as err:
            raise(err)
        return 'Success'