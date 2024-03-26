#1
class Car:
    def __init__(self, marka, model, year):
        self.marka = marka
        self.model = model
        self.year = year

    def description(self):
        print(f"Марка - {self.marka}, Модель - {self.model}, Год выпуска - {self.year}")

merc = Car("Mercedes", "Mercedes Benz", 1923)
bmw = Car("BMW", "BMW X4", 2014)
lexus = Car("Lexus", "Lexus XN", 2014)
merc.description()
bmw.description()
lexus.description()


#2
class Magic_number:
    def __init__(self, num):
        self.num = num

    def __sub__(self, other):
        new_num = self.num - other.num
        return Magic_number(new_num)

    def __add__(self, other):
        new_num = self.num + other.num
        return Magic_number(new_num)
    
    def __mul__(self, other):
        new_num = self.num * other.num
        return Magic_number(new_num)

    def __treativ__(self, other):
        new_num = self.num / other.num
        return Magic_number(new_num)

    def __foortiv__(self, other):
        new_num = self.num // other.num
        return Magic_number(new_num)
    
    def __foortiv__(self, other):
        new_num = self.num == other.num
        return Magic_number(new_num)

a = Magic_number(2)
print(293+392)
print(373-38)
print(3829/323)
print(8274//323)
print(283*2)
print(383==248)


#3
import sqlite3

connection = sqlite3.connect("Library.db")
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS book(
               id INTEGER PTIMARY KEY AUTOINCREAMENT,
               book_name VARCHAR (100) NOT NULL
);""")

class Library:
    def __init__(self):
        self.name = None
        self.shelff = 0

    def registration(self, book_name):
        self.book_name = book_name
        cursor.execute(f"""INSERT INTO book (book_name) 
                       VALUES ('{book_name}')""")
        connection.commit()

    def shelf(self, shelff):
        self.shelff = shelff
        cursor.execute(f"В библиотеке {self.shelff} книг") 
        connection.commit()

    def plus_book(self, plus):
        cursor.execute(f"""UPDATE book SET book_name=book_name+plus WHERE name = '{self.name}'""")
        connection.commit()
        self.shelf+=plus

    def minus_book(self, minus):
        cursor.execute(f"""UPDATE book SET book_name=book_name-plus WHERE name = '{self.name}'""")
        connection.commit()
        self.shelf+=minus

    def start(self):
        while True:
            print("Выберите действие")
            you = int(input("1 - книги, 2 - взять книгу, 3 - положить книгу: "))
            if you == 1:
                book_name = input("Введите название книги: ")
                self.registration(book_name)
            elif you == 2:
                minus = input("Введите какую книгу хотите взять: ")
                self.minus_book(minus)
            elif you == 3:
                plus = input("Введите какую книгу хотите добавить")
                self.plus_book(plus)

eliza = Library()
eliza.start()
