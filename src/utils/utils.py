from urllib.request import urlretrieve
from urllib import error
import os
import csv
import json

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
    
    @staticmethod
    def convert_csv_to_json(csv_file_path, json_file_path="./config/data.json"):
        pass

    @staticmethod
    def get_list_of_csv_file_columns(file_path):
        with open(file_path) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=";")

            list_of_columns_names = []

            for row in csv_reader:
                list_of_columns_names.append(row)
                break
        return list_of_columns_names
