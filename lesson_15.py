import os
from string import ascii_lowercase as alphabet
import random


class ExampleEncapsulation:
    def __init__(self, dirname: str):
        self.dirname = dirname


    def create_directory(self) -> None:
        os.makedirs(self.dirname, exist_ok=True)

    def create_files(self) -> None:
        for symbol in alphabet:
            filename = os.path.join(self.dirname, f"{symbol}.txt")
            self.create_file_from_symbol(filename, symbol)

    def create_file_from_symbol(self, filename: str, symbol: str) -> None:
        data = alphabet.replace(symbol, symbol.upper())
        with open(filename, "w") as file:
            file.write(data)

    def do_tanos_click(self) -> None:
        listdir = os.listdir(self.dirname)
        random.shuffle(listdir)
        for filename in listdir[:len(listdir) // 2]:
            os.remove(os.path.join(self.dirname, filename))


dirname = "test"
example = ExampleEncapsulation(dirname)
example.create_directory()
example.create_files()
example.do_tanos_click()
