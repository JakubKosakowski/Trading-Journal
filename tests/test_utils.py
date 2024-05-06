import pytest
from src.utils import Utils
from urllib import error

def test_download_file(caplog):
    assert Utils.download_file('https://static.nbp.pl/dane/kursy/Archiwum/archiwum_tab_a_2024.csv', 'currencies.csv') == 'Success'
    assert Utils.download_file('https://static.nbp.pl/dane/kursy/Archiwum/archiwum_tab_a_2024.csv', 'currencies.csv', destination='./config') == 'Success'

    Utils.download_file('https://wrong.url.eu', 'currencies.csv')
    assert 'An error occurred: <urlopen error [Errno 11001] getaddrinfo failed>' in caplog.records[0].msg


def test_convert_csv_to_json():
    assert Utils.convert_csv_to_json('./config/currencies.csv') == 'Success'