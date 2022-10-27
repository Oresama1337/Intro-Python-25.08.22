import requests, json

filename = "Quotes"
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
        print(response.json()["quoteText"])

    def print_quotes(self):
        pass

    def save_quotes(self):
        pass

# Написать класс Quotes.
# Параметр инициализации - количество цитат (int), и имя файла для сохранения (формат json, параметр по умолчанию)
#
# В классе реализовать метод get_quotes.
# Метод сохраняет список оветов (список словарей) сервиса http://forismatic.com/ru/api/. Если метод не вызван - список пустой.
# Если автор не указан, цитату не брать. Цитаты не должны повторяться (уникальные, без повтора).
#
# В классе реализовать метод print_quotes.
# Метод печатает из списока полученных ответов от сервера только цитату и автора (а не весь словарь). По одной в каждой строке.
#
# Реализовать метод save_quotes.
# Метод сохраняет список оветов (список словарей) в json файл.
# Перед сохранением в json, записи отсортировать по фамилии автора (повторим функцию сортировки).
# Функцию для сортировки в класс засовывать не нужно. Напишите ее отдельно перед классом ))
#
# Не забудьте написать try except для обработки ошибки при получении цитат.
# Там не всегда срабатывает преобразование в json.
