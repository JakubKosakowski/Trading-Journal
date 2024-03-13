import pytest
from src.utils import Utils
from urllib import error

def test_download_file():
    assert Utils.download_file('https://static.nbp.pl/dane/kursy/Archiwum/archiwum_tab_a_2024.csv') == 'Success'
    with pytest.raises(error.URLError):
        Utils.download_file('https://wrong.url.eu')