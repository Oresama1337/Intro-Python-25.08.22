import requests
import json
from json.decoder import JSONDecodeError


def sort(sortable):
    """
    Функция сортирует записи по фамилии автора
    param list sortable: список словарей для сортировки
    return: list: список словарей, отсортированный по фамилии автора
    """

    return sorted(sortable, key=lambda d: d['Author'].split()[-1])


class Quotes:
    URL = 'http://api.forismatic.com/api/1.0/'
    LIST = []

    def __init__(self, quote_amount, filename='Quotes.json'):
        """
        :param int quote_amount: количество цитат (int)
        :param file filename: имя файла для сохранения (формат json, параметр по умолчанию)
        """
        self.quote_amount = quote_amount
        self.filename = filename

    def get_quotes(self):
        """
        Метод сохраняет список оветов (список словарей)
        Если автор не указан или цитата повторяется, цитатa игнорируются
        """
        self.LIST = []

        for key in range(self.quote_amount):
            buffer = {}
            params = {
                'method': 'getQuote',
                'format': 'json',
                'key': key,
                'lang': 'en'
            }

            try:
                response = requests.get(self.URL, params=params)

                quote = response.json()['quoteText']
                author = response.json()['quoteAuthor']
                sender_name = response.json()['senderName']
                sender_link = response.json()['senderLink']

                if not author:
                    continue
                buffer['Author'] = author
                buffer['Quote'] = quote
                buffer['SenderName'] = sender_name
                buffer['SenderLink'] = sender_link

                not any(item for item in self.LIST if quote in item['Quote']) and self.LIST.append(buffer)

            except JSONDecodeError:
                pass

    def print_quotes(self):
        """
        Метод печатает из списка полученных ответов от сервера цитату и автора
        """
        for item in self.LIST:
            print(item['Author'] + ': ' + item['Quote'])

    def save_quotes(self):
        """
        Метод сохраняет список оветов (список словарей) в json файл
        Перед сохранением в json, записи сортируются по фамилии автора
        """
        json_object = json.dumps(sort(self.LIST), indent=4)
        with open(self.filename, "w") as file:
            file.write(json_object)


if __name__ == '__main__':
    q = Quotes(50)
    q.get_quotes()
    q.print_quotes()
    q.save_quotes()