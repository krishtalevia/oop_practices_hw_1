from __future__ import annotations


class Car:

    def __init__(self, brand: str, model: str, manufacture_year: int,
                 color: str, mileage: int, engine_status: bool, velocity: int):
        self.brand = brand
        self.model = model
        self.manufacture_year = manufacture_year
        self.color = color
        self.mileage = mileage
        self.engine_status = engine_status
        self.velocity = velocity

    def set_engine_status(self, status: bool):
        if not isinstance(status, bool): raise TypeError('Неправильный тип данных')

        self.engine_status = status

    def set_velocity(self, velocity: float):
        if not isinstance(velocity, float): raise TypeError('Неправильный тип данных')

        if velocity > 0 or velocity <= 200:
            self.velocity = velocity
        else:
            print('Скорость не может быть ниже нуля или выше 200 км/ч')

    def set_color(self, color: str):
        if not isinstance(color, str): raise TypeError('Неправильный тип данных')

        self.color = color

    def get_brand(self):
        return self.brand

    def get_model(self):
        return self.model

    def get_manufacture_year(self):
        return self.manufacture_year

    def get_color(self):
        return self.color

    def get_mileage(self):
        return self.mileage

    def get_engine_status(self):
        return self.engine_status

    def get_velocity(self):
        return self.velocity

    def __str__(self):
        return (f'Марка: {self.brand}\n'
                f'Модель: {self.model}\n'
                f'Год выпуска: {self.manufacture_year}\n'
                f'Цвет: {self.color}\n'
                f'Пробег: {self.mileage}\n'
                f'Состояние двигателя: {self.engine_status}\n'
                f'Текущая скорость: {self.velocity}\n')

class Smartphone:

    def __init__(self, brand: str, model: str, os: str, internal_memory: float,
                 ram: float, battery_charge: int, turned_on_status: bool):
        self.brand = brand
        self.model = model
        self.os = os
        self.internal_memory = internal_memory
        self.ram = ram
        self.battery_charge = battery_charge
        self.turned_on_status = turned_on_status

    def set_turned_on_status(self, status: bool):
        if not isinstance(status, bool): raise TypeError('Не подходящий тип данных')

        self.turned_on_status = status

    def set_os(self, os):
        if not isinstance(os, str): raise TypeError('Не подходящий тип данных')

        self.os = os

    def install_app(self, app_memory_volume: float):
        if not isinstance(app_memory_volume, float): raise TypeError('Не подходящий тип данных')

        if app_memory_volume > self.internal_memory: raise Exception('Недостаточно памяти')

        print('Приложение установлено')

    def delete_app(self):
        print('Приложение удалено')

    def set_battery_charge(self, battery_charge: int):
        if not isinstance(battery_charge, int): raise TypeError('Не подходящий тип данных')

        if battery_charge < 0 and battery_charge > 100: raise Exception('Не может быть меньше 0 или больше 100')

        self.battery_charge = battery_charge

    def get_turned_on_status(self):
        return self.turned_on_status

    def get_battery_charge(self):
        return self.battery_charge

    def __str__(self):
        return (f'Марка: {self.brand}\n'
                f'Модель: {self.model}\n'
                f'ОС: {self.os}\n'
                f'Объем встроенной памяти: {self.internal_memory}\n'
                f'Объем оперативной памяти: {self.ram}\n'
                f'Заряд батареи: {self.battery_charge}\n'
                f'Включен ли телефон: {self.turned_on_status}\n')


class Potion:

    def __init__(self, name: str, ingredients: list, difficulty: int, effect: str, ready_status: bool):
        self.name = name
        self.ingredients = ingredients
        self.difficulty = difficulty
        self.effect = effect
        self.ready_status = ready_status

    def add_ingredient(self, ingredient: str):
        if not isinstance(ingredient, str): raise TypeError('Не подходящий тип данных')

        self.ingredients.append(ingredient)

    def del_ingredients(self, ingredient: str):
        if not isinstance(ingredient, str): raise TypeError('Не подходящий тип данных')

        if ingredient in self.ingredients:
            for i in range(0, len(self.ingredients), 1):
                if self.ingredients[i] == ingredient:
                    del self.ingredients[i]
                    break

    def set_difficulty(self, difficulty: int):
        if not isinstance(difficulty, int): raise TypeError('Не подходящий тип данных')

        if difficulty < 0 and difficulty > 10: raise Exception('Не может быть меньше 0 или больше 10')

        self.difficulty = difficulty

    def set_effect(self, effect: str):
        if not isinstance(effect, str): raise TypeError('Не подходящий тип данных')

        self.effect = effect

    def get_ready_status(self):
        return self.ready_status

    def get_ingredients(self):
        return self.ingredients

    def __str__(self):
        return (f'Название: {self.name}\n'
                f'Ингредиенты: {self.ingredients}\n'
                f'Сложность приготовления: {self.difficulty}\n'
                f'Эффект зелья: {self.effect}\n'
                f'Приготовлено ли?: {self.ready_status}\n')

class Library:

    def __init__(self, name: str, adress: str, books_list: list, users_list: list):
        self.name = name
        self.adress = adress
        self.books_list = books_list
        if books_list is None:
            self.books_list = []

        self.users_list = users_list
        if users_list is None:
            self.users_list = []

    def add_book(self, book: Book):
        if not isinstance(book, Book): raise TypeError('Не подходящий тип данных')

        if book not in self.books_list:
            self.books_list.append(book)

    def remove_book(self, book: Book):
        if not isinstance(book, Book): raise TypeError('Не подходящий тип данных')

        if book in self.books_list:
            for i in range(0, len(self.books_list), 1):
                if self.books_list[i] == book:
                    del self.books_list[i]
                    break

    def register_user(self, user: User):
        if not isinstance(user, User): raise TypeError('Не подходящий тип данных')

        if user not in self.users_list:
            self.users_list.append(user)

    def issue_book(self, book: Book, user: User):
        if not isinstance(book, Book): raise TypeError('Не подходящий тип данных')
        if not isinstance(user, User): raise TypeError('Не подходящий тип данных')

        if book in self.books_list and book.in_stock == True:
            book.set_stock_status(False)
            book.set_current_user(user)
            user.add_book(book)

    def return_book(self, book: Book, user: User):
        if not isinstance(book, Book): raise TypeError('Не подходящий тип данных')
        if not isinstance(user, User): raise TypeError('Не подходящий тип данных')

        if book in self.books_list and book.in_stock == False:
            book.set_stock_status(True)
            book.set_current_user(None)
            user.remove_book(book)

    def get_books_status(self) -> str:
        books_status = ''

        for i in self.books_list:
            books_status += str(i)
            books_status += '\n'

        return books_status

    def get_users_status(self) -> str:
        users_list = ''

        for i in self.users_list:
            users_list += str(i)
            users_list += '\n'

        return users_list

    def __str__(self):
        return (f'Название: {self.name}\n'
                f'Адрес: {self.adress}\n'
                f'Список книг: {self.books_list}\n'
                f'Список пользователей: {self.users_list}\n')


class Book:

    def __init__(self, name: str, author: str, year: int, genre: str, in_stock: bool, current_user: User):
        self.name = name
        self.author = author
        self.year = year
        self.genre = genre
        self.in_stock = in_stock
        self.current_user = current_user

    def get_stock_status(self):
        return self.in_stock

    def get_name(self):
        return self.name

    def get_author(self):
        return self.author

    def get_year(self):
        return self.year

    def get_genre(self):
        return self.genre

    def get_current_user(self):
        return self.current_user

    def set_stock_status(self, status: bool):
        if not isinstance(status, bool): raise TypeError('Не подходящий тип данных')

        self.in_stock = status

    def set_current_user(self, user: User):
        if not isinstance(user, User): raise TypeError('Не подходящий тип данных')

        self.current_user = user

    def set_genre(self, genre: str):
        if not isinstance(genre, str): raise TypeError('Не подходящий тип данных')

        self.genre = genre

    def __str__(self):
        return (f'\nНазвание: {self.name}\n'
                f'Автор: {self.author}\n'
                f'Год издания: {self.year}\n'
                f'Жанр: {self.genre}\n'
                f'Наличие: {self.in_stock}\n'
                f'Пользователь: {self.current_user}\n')


class User:

    def __init__(self, name: str, ticket_number: int, books_list: list):
        self.name = name
        self.ticket_number = ticket_number
        if books_list is None:
            self.books_list = []
        else:
            self.books_list = books_list

    def add_book(self, book: Book):
        if not isinstance(book, Book): raise TypeError('Не подходящий тип данных')

        self.books_list.append(book)

    def remove_book(self, book: Book):
        if not isinstance(book, Book): raise TypeError('Не подходящий тип данных')

        for i in range(0, len(self.books_list), 1):
            if self.books_list[i] == book:
                del self.books_list[i]
                break

    def get_books_status(self) -> str:
        books_status = ''

        for i in self.owned_books:
            books_status += str(i)
            books_status += '\n'

        return books_status

    def __str__(self):
        return (f'\nИмя: {self.name}\n'
                f'Номер билета: {self.ticket_number}\n'
                f'Список взятых книг: {self.books_list}\n')

class Program:

    @staticmethod
    def main():
        # Авто
        loaf_car = Car('УАЗ', '452', 1970,
                       'Белый', 50000, True, 199)

        color = loaf_car.get_color()
        print(color)
        loaf_car.set_color('Красный')
        loaf_car.set_engine_status(False)
        print(loaf_car)
        print()

        # Смартфон
        phone = Smartphone('Samsung', 'S24', 'Android', 256,
                           12, 10, True)

        phone.set_turned_on_status(False)
        phone.set_os('ios')
        phone.install_app(100.0)
        print(phone)

        # Зелье
        heal_potion = Potion('Зелье здоровья', ['Мёд', 'Лимон', 'Чеснок'],
                             3, 'Лечит', True)

        heal_potion.add_ingredient('Крапива')
        heal_potion.del_ingredients('Чеснок')
        heal_potion.get_ingredients()
        print()
        print(heal_potion)

        # Библиотека

        funtik = Book('Фунтик', 'Шульжик В.', 2020, 'Детская', True, None)
        hegels_phenomenology = Book('Феноменология духа', 'Фридрих Гегель', 1807,
                                    'Философия', True, None)

        dubrovskiy = Book('Дубровский', 'А.С. Пушкин', 1841,
                          'Роман', True, None)

        ivan = User('Иван', 9, [])
        oleg = User('Олег', 10, [])

        lenin_library = Library('Библиотека им. Ленина', 'Москва, улица Воздвиженка, 3/5',
                                [funtik, hegels_phenomenology], None)

        lenin_library.add_book(dubrovskiy)
        print(lenin_library)

        lenin_library.issue_book(funtik, oleg)
        lenin_library.issue_book(hegels_phenomenology, oleg)
        lenin_library.issue_book(dubrovskiy, ivan)
        print(oleg)
        print()


Program.main()
