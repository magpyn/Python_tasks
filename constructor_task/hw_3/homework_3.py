# Napisz funkcję generującą zamówienie z losową listą produktów na przykład: Produkt-1, Produkt-2 itd.
import random

class Product:

    def __init__(self, name, category_name, price):
        self.name = name
        self.category_name = category_name
        self.price = price


class Order:

    def __init__(self, first_name, last_name, product=None):
        self.first_name = first_name
        self.last_name = last_name

        if product is None:
            product = []
        self.product = product

        total_price = 0
        for product in product:
            total_price += product.price
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


# Funkcja wypisująca produkt i zamówienie.
def print_product(product):
    print(f"Nazwa: {product.name} | Kategoria: {product.category_name} | Cena: {product.price}/szt")


def print_order(order):
    print("=" * 20)
    print(f"Zamówienie złożone przez: {order.first_name}, {order.last_name}")
    print(f"O łącznej wartości: {order.total_price} PLN")
    print("Zamówione produkty:")
    for product in order.products:
        print("\t", end="")
        print_product()
    print("=" * 20)
    print()


def generate_order():
    number_of_product = random.randint(1, 10)
    products = []
    for product_number in range(number_of_product):
        category_name = f"Produkt - {product_number}"
        category_name = "Inne"
        price = random.randint(1, 30)
        product = Product(product_name, category_name, price)
        products.append(product)

    order = Order(first_name = "Magda", last_name = "Pyndryk", products = products)
    return order



def run_homework_3():
    first_order = generate_order()
    print_order(first_order)
    second_order = generate_order()
    print_order(second_order)


if __name__ == '__main__':
    run_homework_3()