# zadanie 1
# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta na podstawie otrzymanych długości przyprostokątnych.
# Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.
# Wykorzystaj w tym celu moduł math z biblioteki standardowej oraz funkcje:
# sqrt(x) - liczy pierwiastek drugiego stopnia z podanej wartości x
# pow(x, y) - podnosi x do potęgi y

import math

def calculate_c_len(a_len, b_len):
    return math.sqrt(math.pow(a_len, 2) + math.pow(b_len, 2))

a = float(input("Jaka jest długość boku a? "))
b = float(input("Jaka jest długość boku b? "))

c = calculate_c_len(a, b)
print(f"Długość przeciwprostokątnej to {c}")

# zadanie 2
# Napisz kalkulator obliczający wartość lokaty po pewnym czasie.
# Wczytaj od użytkownika informacje o:
# Początkowym kapitale (wpłaconej kwocie)
# Oprocentowaniu
# Okresie trwania inwestycji (w latach)
# Umieść funkcję obliczająca wartość lokaty w pakiecie calculations,
# a wczytanie danych i uruchomienie obliczeń w pliku powyżej pakietu.
# Skorzystaj ze wzoru: wartość = wartość pocz. * (1 + procent/100) ^ liczba lat

import 