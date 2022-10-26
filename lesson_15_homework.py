import requests, json

url = "http://forismatic.com/ru/api"
class Quotes:

    def __init__(self, amount: int, filename: str):
        self._filename = filename
        self._create_file(filename)

    @staticmethod
    def _create_file(filename: str):
        with open(filename, "w") as json_file:
            json_file.write()

    def get_quotes(self, url):
        params = {
            "method": "getQuote",
            "format": "json",
            "key": key,
            "lang": "en"
        }
        response = requests.get(url, params=params)

    def print_quotes(self):
        pass

    def save_quotes(self):
        pass





