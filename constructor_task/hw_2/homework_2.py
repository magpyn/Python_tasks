# Napisz funkcję wypisującą produkt i zamówienie.
# Podczas wypisywania zamówienia skorzystaj z wypisywania produktu.


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



def run_homework_2():
    cookies = Product(name="Cookies", category_name="Food", price=4)
    empty_order = Order(first_name="Magda", last_name="Pyndryk")
    order = Order(first_name="Magda", last_name="Pyndryk", list_of_products=[cookies])
    print(cookies)
    print(empty_order)
    print(order)


if __name__ == '__main__':
    run_homework_2()
