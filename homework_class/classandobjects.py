# Utwórz klasy do reprezentacji Produktu, Zamówienia, Jabłek i Ziemniaków.
# Stwórz po kilka obiektów typu jabłko i ziemniak i wypisz ich typ za pomocą funkcji wbudowanej type.
# Stwórz listę zawierającą 5 zamówień oraz słownik, w którym kluczami będą nazwy produktów,
# a wartościami instancje klasy produkt.

class Products:
    pass

class Orders:
    pass

class Apples:
    pass

class Potatoes:
    pass

if __name__ == '__main__':
    green_apple = Apples()
    red_apple = Apples()
    fresh_apple = Apples()
    print("green apple type: ", type(green_apple))
    print("red apple type: ", type(red_apple))
    print("fresh apple type: ", type(fresh_apple))

    old_potato = Potatoes()
    young_potato = Potatoes()
    print("old_potato type: ", type(old_potato))
    print("young potato type: ", type(young_potato))

    orders = []
    for i in range(5):
        orders.append(Orders())
    print(orders)

    products = {
        "Jabłko": Products(),
        "Ziemniak": Products(),
        "Marchew": Products(),
    }
    print(products)

