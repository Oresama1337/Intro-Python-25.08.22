# CLI (command-line interface)
from argparse import ArgumentParser

args = ArgumentParser()

args.add_argument("name", type=str)
# args.add_argument("age", type=int, nargs='?', default=0)
args.add_argument("--age", type=int, nargs='?', default=0)  #can switch places for parameters
args.add_argument("--job", type=str, nargs='?', default='') #in terminal --age 22 --job prog

args = vars(args.parse_args())
print(args)

name = args['name']
age = args['age'] * 2

print(f"Hello {name}! Age:{age}")

# (venv) C:\Users\nelly\PycharmProjects\Intro-Python-25.08.22>lesson_12.py John
# {'name': 'John'}
#
# (venv) C:\Users\nelly\PycharmProjects\Intro-Python-25.08.22>lesson_12.py John
# {'name': 'John', 'age': 0}
#
# (venv) C:\Users\nelly\PycharmProjects\Intro-Python-25.08.22>lesson_12.py John 22
# usage: lesson_12.py [-h] [--age [AGE]] name
# lesson_12.py: error: unrecognized arguments: 22
#
# (venv) C:\Users\nelly\PycharmProjects\Intro-Python-25.08.22>lesson_12.py John 22
# {'name': 'John', 'age': 22}
#
# (venv) C:\Users\nelly\PycharmProjects\Intro-Python-25.08.22>lesson_12.py John 22
# {'name': 'John', 'age': 22}
# Hello John! Age:44
#
# (venv) C:\Users\nelly\PycharmProjects\Intro-Python-25.08.22>lesson_12.py John --job programmer --age 45
# {'name': 'John', 'age': 45, 'job': 'programmer'}
# Hello John! Age:90
#
# (venv) C:\Users\nelly\PycharmProjects\Intro-Python-25.08.22>
