# Dodaj konstruktor przyjmujący odpowiednie argumenty do klas Product, Order,  Apple i Potato:
# Product: nazwa, nazwa kategorii, cena jednostkowa
# Order: imię i nazwisko zamawiającego, lista produktów (domyślnie pusta), łączna cena (obliczona w konstruktorze jako suma cen jednostkowych z listy produktów)
# Apple: nazwa gatunku, rozmiar, cena za kg
# Potato: nazwa gatunku, rozmiar, cena za kg
# Utwórz kilka obiektów każdej klasy.

class Product:

    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price


class Order:

    def __init__(self, first_name, last_name, list_of_products=None):
        self.first_name = first_name
        self.last_name = last_name

        if list_of_products is None:
            list_of_products = []
        self.list_of_products = list_of_products

        total_price = 0
        for product in list_of_products:
            total_price += list_of_products.price
        self.final_price = total_price


class Apple:

    def __init__(self, name, size, price):
        self.price = price
        self.size = size
        self.name = name


class Potato:

    def __init__(self, name, size, price):
        self.price = price
        self.size = size
        self.name = name


def run_homework_1():
    green_apple = Apple(name="Green", size="M", price=3.5)
    red_apple = Apple(name="Red", size="S", price=2.4)
    print(green_apple.name, green_apple)
    print(red_apple.name, red_apple)

    old_potato = Potato(name="Potato Old", size="M", price=1.45)
    print(old_potato.name, old_potato)

    cookies = Product(name="Cookies", category_name="Food", price=4)
    empty_order = Order(first_name="Magda", last_name="Pyndryk")
    order = Order(first_name="Magda", last_name="Pyndryk", list_of_products=[cookies])
    print(cookies)
    print(empty_order)
    print(order)


if __name__ == '__main__':
    run_homework_1()

