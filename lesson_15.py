import os
from string import ascii_lowercase as alphabet
import random


class ExampleEncapsulation:
    def __init__(self, dirname: str):
        self._dirname = dirname
        self._create_directory()

    @property
    def dirname(self):
        return self._dirname


    def _create_directory(self) -> None:
        os.makedirs(self._dirname, exist_ok=True)

    def create_files(self) -> None:
        for symbol in alphabet:
            filename = os.path.join(self._dirname, f"{symbol}.txt")
            self._create_file_from_symbol(filename, symbol)

    def _create_file_from_symbol(self, filename: str, symbol: str) -> None:
        data = alphabet.replace(symbol, symbol.upper())
        with open(filename, "w") as file:
            file.write(data)

    def do_tanos_click(self) -> None:
        listdir = os.listdir(self._dirname)
        random.shuffle(listdir)
        for filename in listdir[:len(listdir) // 2]:
            os.remove(os.path.join(self._dirname, filename))


dirname = "test1"
example = ExampleEncapsulation(dirname)

print(example.dirname)
#example._dirname = "test2"
#print(dir(example))
#example._create_directory()
example.create_files()
example.do_tanos_click()