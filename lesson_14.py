# OOP
# Class
# атрибут класса
# экземпляр класса
# атрибут экземпляря класса
# метод экземпляря класса


class Person:
    # def __init__(self):
    # self.name = "John"      # атрибут экземпляря класса
    def __init__(self, first_name: str, last_name: str, bday: str):
        self.first_name = first_name    # атрибут экземпляря класса
        self.last_name = last_name
        self.bday = bday    # атрибут экземпляря класса
        self.db_user = None
        self.full_name = self.get_full_name()

    def __str__(self):
        return f"name: {self.first_name}, bday: {self.bday}"

    def __repr__(self):     # persons = [person_1, person_2]
        return f"{self.first_name}"

    # def get_full_name(self, separator):
    #     full_name = f"{self.first_name} {separator} {self. last_name}"
    #     return full_name
    def get_full_name(self):
        full_name = f"{self.first_name} {self. last_name}"
        return full_name


person_1 = Person(first_name="John", bday="12/12/00", last_name="Lennon") # экземпляр класса
person_2 = Person("Anna", "Karenina", "01/01/2000") # экземпляр класса
#person_1.last_name = "Lennon"  #bad style

# print(person_1.name, person_1.bday, person_2.name, person_2.bday)

print(person_1)
print(person_2)

persons = [person_1, person_2]

print(persons)
#print(person_1.get_full_name())
#full_name = person_1.get_full_name(separator= "___")

full_name = person_1.get_full_name()

print(full_name)
# class Person:  # Class
#     # name = "John"   # атрибут класса
#     # bday = ""
#     bday: str
#     name: str
#
#
# person_1 = Person()  # экземпляр класса
# person_2 = Person()  # экземпляр класса
#
# person_2.name = "Anna"
# person_2.bday = "01/01/2000"
# person_1.name = "John"
# person_1.bday = ""
#
# print(person_1.name, person_1.bday, person_2.name, person_2.bday)
