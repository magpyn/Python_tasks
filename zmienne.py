# # zadanie 1
# # W ciągu 3 godzin biegu biegacz pokonał 38 kilometrów.
# # Wyznacz średnią prędkość korzystając ze zmiennych.
#
# time = 3
# distance = 38
#
# speed = distance / time
# print(speed)
#
# # zadanie 2
# # Zakładając, że na lokatę wpłacono 1000 zł, a oprocentowanie wynosi 4% w skali roku, oblicz jaka będzie wartość lokaty po 5 latach.
# #
# # Wzór to:
# # wartość = wartość pocz. * (1 + procent/100) ^ liczba lat
#
# value = 1000
# percentage = 4
# years_time = 5
#
# investment_value = value * (1 + percentage/100) ** years_time
# print(investment_value)
#
# # zadanie 3
# # Oblicz jaką drogę pokonasz idąc do sklepu po czerwonych liniach i wypisz tyle myślników (-) jaki będzie wynik.
#
# c = 2 * ((9 ** 2 + 12 ** 2) ** 0.5)
# total_distance = 2 * c
# print(total_distance)
#
# print("-" * int(total_distance))
#
# # zadanie 4
# # wypisz swoje ulubione potrawy, każdą z nich umieszczając w nowej linii.
#
# print("Moje ulubione potrawy to: ", "pierogi", "krupnik", "tort czekoladowy", sep = "\n")
#
# # zadanie 5
# # zapytaj użytkownika ile ma lat i wyświetl, ile to miesięcy.
#
# wiek = input("Ile masz lat?")
# miesiace = int(wiek) * 12
# print(miesiace)
#
# # zadanie 6
# # Zapytaj ile kilometrów przeszedł w tym tygodniu i policz ile tygodni zajmie mu okrążenie Ziemi.
# # Pamiętaj, że obwód Ziemi to 40 075 km.
#
# kilometers = input("Ile km przeszedłeś w tym tygodniu?")
# tygodnie = int(kilometers) * 7
# obwod = 40075
# ile_zajmie = obwod / tygodnie
#
#
# print("Okrążenie Ziemi zajmie Ci", ile_zajmie, "tygodni.")
#
# # zadanie 7
# # Zastosuj wzór do obliczenia wartości lokaty, pobierając od użytkownika następujące dane:
# #
# # początkowa wartość
# # oprocentowanie
# # czas trwania w latach
# #
# # Wzór to:
# # wartość = wartość pocz. * (1 + procent / 100) ^ liczba lat
# Dostosuj program liczący wartość lokaty, tak aby wyświetlał ją z dokładnością do groszy (dwóch cyfr po przecinku).
# start_value = input("Podaj początkową wartość.")
# percentage = input("Podaj wysokość oprocentowania.")
# time = input("Podaj czas trwania lokaty.")
#
# value = int(start_value) * (1 + int(percentage)/100) ** int(time)
# print(f"Wartość lokaty to: {value:.2f}")

# zadanie 8
# Napisz program, który zapyta użytkownika jaka jest cena jabłek w Biedronce, Lidlu i Żabce.
# Następnie wypisz informację: Ile kosztują najtańsze jabłka?

# apple_price_biedronka = float(input("Jaka jest cena jabłek w Biedronce?"))
# apple_price_lidl = float(input("Jaka jest cena jabłek w Lidlu?"))
# apple_price_zabka = float(input("Jaka jest cena jabłek w Żabce?"))
#
#
# minimum_price = min(apple_price_biedronka, apple_price_lidl, apple_price_zabka)
# print("Najtansze jabłka kosztują", minimum_price, "zł.")

# zadanie 9
# Zapytaj użytkownika o imię i wypisz ile liter zawiera.
# name = input("Podaj imie:")
# print(f"Twoje imię ma {len(name)} liter.")

# Zadanie 10
# Zapytaj użytkownika gdzie mieszka i wypisz odpowiedź, np. "Jak miło, że mieszkasz w Gdańsku".
# W razie nieuwagi użytkownika popraw wprowadzoną nazwę miasta, tak by zaczynała się z wielkiej litery.

# home_place = input("Gdzie mieszkasz?")
# home_place = home_place.title()
# print(f"Jak miło, że mieszkasz w {home_place}")

# zadanie 11
# Stwórz zmienną favourite_sports, która będzie listą zawierającą nazwy dyscyplin sportu, które lubisz.
# Następnie wypisz informacje, jaki sport jest pierwszy na Twojej liście, a jaki ostatni.
# Podmień jeden ze sportów na inny i wypisz całą listę.

# favourite_sports = [
#     "badminton",
#     "piłka nożna",
#     "jogging"
# ]
# print("Moim ulubionym sportem jest:", favourite_sports[0])
# print("Lubię też:", favourite_sports[-1])
#
# favourite_sports[1] = "koszykówka"
# print("Zmieniłam zdanie. Moimi ulubionymi sportami są teraz:", favourite_sports)
#
# # zadanie 12
# Zapytaj użytkownika o 3 ulubione potrawy i zapisz je w postaci listy.

# favourite_meals = []
# dish = input("Jakie jest Twoje ulubione danie nr 1?")
# favourite_meals.append(dish)
# dish = input("Jakie jest Twoje ulubione danie nr 2?")
# favourite_meals.append(dish)
# dish = input("Jakie jest Twoje ulubione danie nr 3?")
# favourite_meals.append(dish)
#
# print("Twoje ulubione dania to:", favourite_meals)
#
# # zadanie 13
# # Zapytaj użytkownika o numer telefonu i wypisz go w postaci zanonimizowanej.
# # Wypisz pierwszych 5 cyfr, a kolejne zastąp myślnikiem.
#
# phone_number = input("Jaki jest Twój numer telefonu?")
# phone_number = phone_number.replace("-", "")
# public_digits = phone_number[:6]
# number_of_private_digits = len(phone_number) - 6
# private_digits = "-" * number_of_private_digits
# anonymous_number = f"{public_digits}{private_digits}"
#
# print("Zanonimizowany numer:", anonymous_number)

# zadanie 14
# Stwórz i wypisz słownik, w którym kluczami będą różne przedmioty szkolne, a wartościami oceny uzyskane z tych przedmiotów.

oceny = {
    "matematyka" : [5, 2, 3, 4.5, 3.5],
    "fizyka" : [3.5, 2, 4.5, 4, 3.5],
    "geografia" : [4, 3, 3.5, 4.5, 2],
}
print("Przedmioty i oceny:", oceny)

# zadanie 15
# Stwórz zmienną my_family zawierającą drzewo genealogiczne Twojej rodziny.
# Zacznij od siebie, opisując imię, nazwisko oraz datę urodzenia każdej osoby oraz jej rodziców.
# Podpowiedź: rodzice będą listami zawierającymi w sobie kolejne słowniki.

my_family = {
    "first_name" : "Magda",
    "last_name" : "Pyndryk",
    "birth_date" : "03-04-1995",
    "parents:" : [
    {
        "first_name:" : "Tomasz",
        "last_name:" : "Pyndryk",
        "birth_date:" : "23-08-1971",
        "parents:" [
            {
                "first_name:" : "Jan",
                "last_name:" : "Pyndryk",
                "birth_date:" : "24-03-1932",
                "parents:" : []
            }
        ]
    }
]
}
print("Drzewo genealogiczne", my_family)

# zadanie 16
# Zapytaj użytkownika ile miesięcznie wydaje pieniędzy na:
# jedzenie
# rozrywkę
# opłaty
# inne
# Oblicz udział procentowy każdej kategorii w łącznych wydatkach.
# Następnie poproś użytkownika o wybór kategorii i wypisz jaki jest jej udział procentowy.

expenditures = input("Ile miesięcznie wydajesz pieniędzy na:")
jedzenie = float(input("jedzenie?"))
rozrywke = float(input("rozrywkę?"))
oplaty = float(input("oplaty?"))
inne = float(input("inne?"))

total_expenditure = jedzenie + rozrywke + oplaty + inne

expenditure_percentage = {
    "jedzenie" : jedzenie * 100 / total_expenditure,
    "rozrywka" : rozrywke * 100 / total_expenditure,
    "oplaty" : oplaty * 100 / total_expenditure,
    "inne" : inne * 100 / total_expenditure,
}

selected_category =  input("Wybierz jedną z kategorii wydatków.")
print(f"Na {selected_category} wydajesz {expenditure_percentage[selected_category]:.0f}")

# zadanie 17
# Zapytaj użytkownika o ceny trzech produktów i wypisz wyniki ich porównania.


mleko = float(input("Ile kosztuje mleko?"))
cukier = float(input("Ile kosztuje cukier?"))
smietana = float(input("Ile kosztuje smietana?"))

print(f"Czy smietana jest droższa niż cukier? {smietana > cukier}")

# zadanie 18
# Poproś użytkownika o wprowadzenie listy zakupów, rozdzielając poszczególne elementy przecinkiem.
# Następnie powiedz (wypisz), czy jest to według Ciebie długa lista, czy też nie.

lists = input("Podaj listę zakupów, rozdzielając poszczególne elementy przecinkiem.")
shopping_list = lists.split(",")
is_shopping_list_long = len(shopping_list) > 4
print("Czy uważam, że Twoja lista zakupów jest długa?", {is_shopping_list_long})



# zadanie 19
# Zmodyfikuj rozwiązania zadań 1 i 2 z poprzedniej lekcji, tak aby wypisywać różne informacje w zależności od wyniku porównań.

if len(shopping_list) > 4:
    print("Ale długa lista zakupów!")
else:
    print("To nie jest taka długa lista zakupów.")

# zadanie 20
# Zapytaj użytkownika o jego oceny końcowe z kilku przedmiotów (matematyka, fizyka, itd.).
# Następnie, przeanalizuj je i wypisz informację czy zdał/zdała do kolejnej klasy.
# Załóż, że zdać można wtedy jeżeli nie ma się żadnej jedynki albo jeżeli ma się jedną jedynkę,
# ale średnia ze wszystkich ocen jest wyższa niż 3.5.


matematyka = int(input("Jaką ocenę uzyskałeś z matematyki?"))
angielski = int(input("Jaką ocenę uzyskałeś z angielskiego?"))
fizyka = int(input("Jaką ocenę uzyskałeś z fizyki?"))

liczba_uzyskanych_jedynek = 0

if matematyka < 2:
    liczba_uzyskanych_jedynek = liczba_uzyskanych_jedynek + 1
if angielski < 2:
    liczba_uzyskanych_jedynek = liczba_uzyskanych_jedynek + 1
if fizyka < 2:
    liczba_uzyskanych_jedynek = liczba_uzyskanych_jedynek + 1

if liczba_uzyskanych_jedynek ==0:
    print("Gratuluję, zdałeś do następnej klasy! :)")
else:
    if liczba_uzyskanych_jedynek == 1:
        srednia = (matematyka + angielski + fizyka) / 3
        if srednia > 3.5:
            print("Super, zdajesz do następnej klasy! :)")
        else:
            print("No niestety, nie zdajesz...")
    else:
        print("No, niestety...")

# zadanie 21
# Zapytaj o imię i "rozpoznaj" czy użytkownik to kobieta czy mężczyzna.
# Podpowiedź: Na potrzeby tego zadania możemy założyć, że żeńskie imiona kończą się na "a".

name = input("Jak masz na imię?")

if name[-1] == "a":
    print("Jesteś konietą.")
else:
    print("Jesteś mężczyzną.")

# zadanie 22
#

expenditures = input("Ile miesięcznie wydajesz pieniędzy na:")
jedzenie = float(input("jedzenie?"))
rozrywke = float(input("rozrywkę?"))
oplaty = float(input("oplaty?"))
inne = float(input("inne?"))

total_expenditure = jedzenie + rozrywke + oplaty + inne

expenditure_percentage = {
    "jedzenie": jedzenie * 100 / total_expenditure,
    "rozrywka": rozrywke * 100 / total_expenditure,
    "oplaty": oplaty * 100 / total_expenditure,
    "inne": inne * 100 / total_expenditure,
}

most_important_category = "jedzenie"

if expenditure_percentage["rozrywka"] > expenditure_percentage[most_important_category]:
    most_important_category = "rozrywka"


# zadanie 23
# Mamy 4 rodzaje wsparcia - od najlepszych do najgorszych są to:
# - Główne wsparcie -> przychód poniżej 5000
# - Wsparcie z funduszu pracowników -> od 5 do 10 pracowników
# - Wsparcie dla nowych firm -> krócej niż 3 lata na rynku
# - Wsparcie na pocieszenie -> dla każdego, kto nie dostał żadnego innego

income = 5000
employeers_number = 7
years_on_the_market = 3

if income < 5000:
    print("Przyznano główne wsparcie")
else:
    if 5 <= employeers_number <= 10:
        print("Przyznano wsparcie z funduszu pracowników")
    else:
        if years_on_the_market < 3:
            print("Przyznano wsparcie dla nowych firm")
        else:
            print("Przyznano wsparcie na pocieszenie ;)")


# 2 sposób

if income < 5000:
    print("Przyznano główne wsparcie")
if income >= 5000 and 5 <= employeers_number <= 10:
    print("Przyznano wsparcie z funduszu pracowników")
if income >= 5000 and 5 <= employeers_number <= 10 and years_on_the_market < 3:
    print("Przyznano wsparcie dla nowych firm")
else:
    print("Przyznano wsparcie na pocieszenie")

# 3 sposób, elif, czyli "inaczej, jeśli..."

if income < 5000:
    print("Przyznano główne wsparcie")
elif 5 <= employeers_number <= 10:
    print("Przyznano wsparcie z funduszu pracowników")
elif years_on_the_market < 3:
    print("Przyznano wsparcie dla nowych firm")
else:
    print ("Przyznano wsparcie na pocieszenie")


# zadanie 24
# Zaimplementuj program interpretujący wynik uzyskany w teście Coopera.
# Zapytaj o wiek, płeć, uzyskany wynik.
# na tej podstawie zinterpretuj rezultat.
# możesz zaimplementować tylko wybrane przedziały wiekowe.

age = int(input("Ile masz lat? "))
gender = input("Jesteś mężczyzną czy kobietą? (M/K) ")
result = int(input("Jaki był Twój wynik w teście 12 minut biegu (ile metrów)? "))

if age == 8:
    if gender == "M":
        if result >= 2190:
            print("Bardzo dobrze")
        elif result >= 1810:
            print("Dobrze")
        elif result >= 1420:
            print("Średnio")
        elif result >= 1050:
            print("Źle")
        else:
            print("Bardzo źle")
    else:
        if result >= 2010:
            print("Bardzo dobrze")
        elif result >= 1670:
            print("Dobrze")
        elif result >= 1320:
            print("Średnio")
        elif result >= 990:
            print("Źle")
        else:
            print("Bardzo źle")
else:


# zadanie 25
# Połącz kalkulator wartości lokaty i kredytowy.
# zapytaj użytkownika czy chce żeby obliczyć wartość lokaty, czy zdolność kredytową
#a następnie wyznacz oczekiwaną wartość.
# obsłuż (np. odnpowiednim komunikatem) sytuację, w której użytkownik wybierze nieistniejącą opcję.

print("Kalkulator:", "1 -> wartości lokaty", "2 -> kredytowy", sep="\n")
option = input("Wybierz opcję:")

if option == "1":
    print("Kalkulator wartości lokaty z roczną kapitalizacją")

    initial_value_input = input("Jaką kwotę wpłaciłeś/wpłaciłaś? ")
    initial_value = int(initial_value_input)
    percentage_input = input("Jakie jest oprocentowanie (%)? ")
    percentage = int(percentage_input)
    years_input = input("Ile lat trwa lokata? ")
    years = int(years_input)

    final_value = initial_value * (1 + percentage / 100)  ** years
    print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

elif option == "2":
    loan_amount = int(input("Jaka jest kwota kredytu? "))
    interest_rate = float(input("Jakie jest oprocentowanie? "))
    own_contribution = int(input("Jaka jest wartość wkładu własnego? "))
    years = int(input("Jaki jest czas kredytowania (w latach)? "))
    monthly_income = int(input("Jaki jest miesięczny przychód? "))
    monthly_expenditure = int(input("Jaka jest suma miesięcznych wydatków? "))

    installment_value = (loan_amount * interest_rate / 100) / 12 + (loan_amount / (years * 12))
    available_money = monthly_income - monthly_expenditures
    property_value = loan_amount + own_contribution

    own_contribution_part = own_contribution / property_value
    money_over_installment = available_money - installment_value

    if own_contribution_part >= 0.2 and money_over_installment >= 1000:
        print("Można wziąć kredyt")
    elif own_contribution_part >= 0.1 and money_over_installment >=2000:
        print("Można wziąć kredyt")
    else:
        print("Nie można wziąć kredytu")

else:
    print(f"Nie ma takiej opcji: {option}")


# zadanie 26
# Zapytaj użytkownika o numer telefonu i sprawdź, czy zawiera przynajmniej jedną cyfrę 0.

phone_number = input("Jaki jest Twój numer telefonu? ")

if "0" in phone_number:
    print("Twój numer zawiera cyfrę 0")
else:
    print("W Twoim numerze nie ma zer")

# zadanie 27
# Utwórz zmienną value oraz instrukcję warunkową, która sprawdzi, czy wartość tej zmiennej jest:
# True
# False
# None
# inną wartością.

value = 3

if value is True:
    print("To prawda")
elif value is False:
    print("To fałsz")
elif value is None:
    print("To None")
else:
    print("To inna wartość")


# zadanie 28
# pętla while

counter = 0
while counter <= 30:
    print(counter)
    counter += 1

# zadanie 29
#Ile chcesz ziemniaków na obiad?

expected_potatoes = int((input("Ile chcesz ziemniaków na obiad? ")))
potatoes = []
while len(potatoes) < expected_potatoes:
    print("Obieram ziemniaka...")
    print("I wrzucam go do garnka")
    potatoes.append("Ziemniak")
print(potatoes)

# zadanie 30
# liczba podana przed użytkownika musi być większa niż 100

number = 0
while number <= 100:
    number = int(input("Podaj liczbę większą niż 100"))
    if number <= 100:
        print(f"{number} nie jest większe niż 100, spróbuj ponownie... \n")
print("Brawo!")

# 2 sposób
number = int(input("Podaj liczbę większą niż 100: "))
while number <= 100:
    print(f"{number} nie jest większe niż 100, spróbuj ponownie... \n")
    number = int(input("Podaj licznę większą niż 100: "))
print(f"Brawo!")

#zadanie 31
# sprawdź, czy użytkownik podał sensowną wartość

age = int(input("Ile masz lat? "))
while age < 1:
    if age < 1:
        print("Chyba nie... \n")
        age = int(input("Ile masz lat? "))
if age < 18:
    print("Jeszcze nie możesz głosować")
else:
    print("Możesz już głosować!")

# zadanie 32
# pozwalam użytkownikowi skorzystać z programu wielokrotnie

option = None
while option == "T":
    income = int(input("Podaj przychód: "))
    employeers_number = int(input("Podaj liczbę pracowników: "))
    years_on_the_market = int(input("Ile lat działacie na rynku: "))
    if income < 2000:
        print("Przyznano główne wsparcie")
    elif 5 <= employeers_number <= 10:
        print("Przyznano wsparcie z funduszu pracowników")
    elif years_on_the_market < 3:
        print("Przyznano wsparcie dla nowych firm")
    else:
        print("Przyznano wsparcie na pocieszenie")

    option = input("Jeżeli chcesz sprawdzić dla innych danych wpisz 'T'")


# zadanie 33
# wypisywanie listy ulubionych sportów

favourite_sports = ["bieganie", "pływanie", "koszykówka", "piłka nożna"]
sport_index = 0
while sport_index < len(favourite_sports[sport_index]):
    print(favourite_sports[sport_index])
    sport_index += 1

# zadanie 34
# wypisywanie co 2 sportu

favourite_sports = ["bieganie", "pływanie", "koszykówka", "piłka nożna"]
sport_index = 0
while sport_index < len(favourite_sports):
    if sport_index % 2 == 0:
        print(favourite_sports[sport_index])
    sport_index += 1

# zadanie 35
# sumowanie liczb

numbers = [1, 3, 15, 128, 98]
numbers_sum = 0
number_index = 0
while number_index < len(numbers):
    numbers_sum += numbers[number_index]
    number_index += 1
print(f"Suma:" {numbers_sum})

# zadanie 36
# wypisywanie kodu pocztowego znak po znaku

post_code = input("Jaki jest Twój kod pocztowy? ")
letter_index = 0
while letter_index < len(post_code):
    print(f"[{letter_index}] -> {post_code[letter_index]}")
    letter_index += 1

# zadanie 37
# zmiana kodu pocztowego, aby zawsze był zgodny z wybranym formatem

post_code = input("Jaki jest Twój kod pocztowy? ")
post_code = post_code.replace("-", "")
formatted_post_code = ""
letter_index = 0
while letter_index < len(post_code):
    if letter_index % 2 == 0 and letter_index != 0:
        formatted_post_code += "-"
    formatted_post_code += post_code[letter_index]
    letter_index += 1
print(formatted_post_code)

# zadanie 38
# Pytaj użytkownika o liczbę tak długo, aż poda liczbę parzystą lub przekroczy limit 10 prób.

number = int(input("Podaj liczbę parzystą: "))
try_number = 1

while try_number < 10 and number % 2 != 0:
    number = int(input("Podaj liczbę jeszcze raz"))
    try_number += 1



# zadanie 39
# Wczytaj numer telefonu użytkownika i rodziel go myślnikami (format XXX-XXX-XXX).

telephone_number = int(input("Podaj numer telefonu"))
telephone_number = telephone_number.replace("-", "")
formatted_telephone_number = ""
number_index = 0

while number_index < len(telephone_number):
    if number_index % 3 and number_index != 0:
        formatted_telephone_number += telephone_number[number_index]
        number_index += 1
print(formatted_telephone_number)


# zadanie 40
# Poproś użytkownika o podanie ulubionych dań, rozdzielając każde z nich przecinkiem.
# Następnie wypisz każde z nich wraz z informacją, które miejsce zajmuje na jego liście.

dishes = input("Podaj swoje ulubione dania, rozdzielając je przecinkiem: ")
favourite_dishes = dishes.split(",")

dish_index = 0
while dish_index < len(favourite_dishes):
    print(f"Ulubione danie numer {dish_index}: {favourite_dishes[dish_index]}")
    dish_index += 1

# zadanie 41
# za pomocą pętli for wypisać klucze ze słownika
expenditures = {
    "prąd": [250],
    "woda": [30.45],
    "zakupy": [
        120.15,
        170.53,
        20.15
    ]
}
for expenditure_name in expenditures:
    print(expenditure_name)

# można wypisać wartości ze slownika

for expenditures in expenditures.values():
    print(expenditures)

# lub odwołanie do kluczy i wartości słownika

for expenditure_name in expenditures:
    print(f"{expenditure_name} -> {expenditures[expenditure_name]}")

# lub metoda items na słowniku

for expenditure_name, expenditures in expenditures.items():
    print(f"{expenditure_name} -> {expenditures}")

# metoda items zwraca krotki dwuelementowe, które zawierają w pierwszym elemencie tej krotki klucz i drugi wartość

# zadanie 42
# Wypisz kod pocztowy - znak po znaku wraz z informacją o kolejności

post_code = input("Jaki jest Twój kod pocztowy? ")
for index, letter in enumerate(post_code):
    print(f"[{index}] -> {letter}")


# zadanie 43
# Wypisz co drugi sport
favourite_sports = ["bieganie", "pływanie", "piłka nożna", "koszykówka"]
for index, sport in enumerate(favourite_sports):
    if index % 2 == 0:
        print(sport)

# zadanie 44
# zamień kod pocztowy z użyciem pętli for tak, aby był zgodny z formatowaniem XX-XX-XX-XX...

post_code = input("Jaki jest Twój kod pocztowy? ")
post_code = post_code.replace("-", "")
formatted_post_code = ""
for index, letter in enumerate(post_code):
    if index % 2 and index != 0:
        formatted_post_code += "-"
    formatted_post_code += letter
print(formatted_post_code)

# pętla while dobrze sprawdza się podczas wczytywania od użytkownika listy danych nieznanej długości
# natomiast przetworzenie każdego elementu takiej listy powinno odbywać się z użyciem pętli for

# zadanie 45
# Poproś użytkownika o wprowadzenie ocen, które uzyskał.
# Wykorzystaj pętlę while, aby pytać o kolejne oceny i zakończyć wprowadzanie odpowiednim znakiem (np. X).
# Następnie, stosując pętlę for, oblicz średnią z podanych ocen.

oceny = []
wprowadzanie_ocen = input("Podaj kolejną ocenę lub zakończ wpisując 'X': ")
while wprowadzanie_ocen != 'X':
    oceny = int(wprowadzanie_ocen)
    oceny.append(oceny)
    wprowadzanie_ocen = input("Podaj kolejną ocenę lub zakończ wpisując 'X': ")

suma_ocen = 0
for ocena in oceny:
    suma_ocen += ocena

# sumę można też policzyć tak:
# suma_ocen = sum(ocena)

srednia = suma_ocen / len(oceny)
print(f"Twoja średnia ocen wynosi: {srednia:.2f}")




# zadanie 46
# Zmodyfikuj zadanie z poprzedniej lekcji, dotyczące formatowania numeru telefonu.
# zastąp pętlę while pętlą for.

phone_number = input("Podaj numer telefonu")
phone_numer = phone_numer.replace("-", "")
formatted_phone_number = ""
for index, digit in enumerate(phone_number):
    if index % 3 == 0 and index != 0:
        formatted_phone_number += "-"
    formatted_phone_number += phone_number[index]

print(f"Twój numer telefonu to: {formatted_phone_number}")


# zadanie 47
# Wczytaj od użytkownika kolejne kategorie wydatków oraz dla każdej z nich dokonane wydatki.
# Zastosuj pętlę while, aby użytkownik mógł zakończyć wprowadzanie kategorii i wydatków.
# Stosując pętlę for, oblicz procentowy udział każdego z wydatków w miesięcznym budzecie i wypis wyniki
# oraz dodatkową informację, która powie o najbardziej znaczącej kategorii.

print("Kalkulator budżetu miesięcznego")
expenditures = {}

category_name = input("Podaj kategorię wydatków albo zakończ wpisując 'X': ")
while category_name != 'X':
    expenditures[category_name] = []
    expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisując 'X': ")
    while expenditure != 'X':
        expenditure_value = float(expenditure)
        expenditures[category_name].append(expenditure_value)
        expenditure = input(f"Podaj wartość następnego wydatku w kategorii {category_name} albo zakończ wpisuac 'X': ")
    category_name = input("Podaj kategorię wydatków albo zakncz wpisując 'X: ")

total_expenditures = 0
for category_expenditures in expenditures.values():
    for expenditure_value in category_expenditures:
        total_expenditures += expenditure_value

expenditure_percentage = {}
for category_name, category_expenditures in expenditures.items():
    total_category_expenditures = 0
    for expenditure_value in category_expenditures:
        total_category_expenditures += sum(category_expenditures)
    expenditures_percentage[category_name] = total_category_expenditures * 100 / total_expenditures

most_important_category = None
most_important_category_percentage = 0
for category, percentage in expenditures_percentage.items():
    if percentage > most_important_category_percentage:
        most_important_category_percentage = percentage
        most_important_category = category

if most_important_Category is not None:
    print(f"Najwięcej wydajesz na {most_important_category} - {most_important_category_percentage:.0f}% wszystkich wydatków")

for category, percentage in expenditures_percentage.items():
    print(f"Na {category} wydajesz {percentage:.0f}% miesięcnzych wydatków")

# zadanie 48
# for i in range

print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value_input = input("Jaką kwotę wpłaciłeś? ")
initial_value = int(initial_value_input)
percentage_input = input("Jakie jest oprocentowanie (%)? ")
percentage = int(percentage_input)
years_input = input("Ile lat trwa lokata? ")
years = int(years_input)

for year_number in range(1, years + 1):
    investment_value = initial_value * (1 + percentage / 100) ** year_number
    print(f"Po {year_number} latach Twoja lokata będzie warta {investment_value:.2f}")

# zadanie 49
# Poproś użytkownika o podanie numeru telefonu.
# Następnie wypisz informację ile razy występuje w nim każda cyfra.

phone_number = input("Podaj numer telefonu: ")
for digit in range(10):
    digit_times_in_number = phone_number.count(str(digit))
    print(f"Cyfra {digit} występuje w Twoim numerze: {digit_times_in_number} razy.")


# zadanie 50
# Napisz kalkulator dla kredytu o malejącej racie.
# Zapytaj użytkownika o:
# kwotę kredytu
# oprocentowanie kredytu (tutaj zakładamy, że oprocentowanie jest stałe)
# czas trwania (w latach)
# koszty początkowe (prowizja itp.)
# Oblicz jaką łącznie sumę użytkownik odda bankowi i porównaj ją z kapitałem, który otrzyma.
# Oblicz wartość każdej miesięcznej raty według wzoru:
# kapitał spłacany miesięcznie = kwota kredytu / (liczba lat * 12)
# pozostały kapitał = kwota kredytu - (numer miesiąca od początku - 1) * kapitał spłacany miesięcznie
# rata = (pozostały kapitał * oprocentowanie / 100) / 12 + kapitał spłacany miesięcznie



# zadanie 51
# Zmodyfikuj rozwiązanie zadania z promocją do kolejnej klasy z lekcji o instrukcji if/else (moduł 4).
# Wczytaj oceny do listy.
# Jeżeli jest jakakolwiek jedynka to klasę trzeba powtórzyć.
# W przeciwnym razie należą się gratulacje.

subjects = ["matematyka", "fizyka", "biologia", "język angielski", "chemia"]
grades = []

for subject in subjects:
    grade = int(input(f"Jaka jest Twoja ocena końcowa z przedmiotu {subject}? "))
    grades.append(grade)

for grade in grades:
    if grade == 1:
        print("Niestety...")
        break
else:
    print("Gratulacje! Zdałeś do następnej klasy")




# zadanie 52
# Zmodyfikuj rozwiązanie zadania trzeciego z lekcji dotyczącej pętli for (obliczanie wydatków domowych).
# Skorzystaj z instrukcji break, aby wyeliminować powtórzone wywołania funkcji input.


# zadanie 53
# Utwórz listę zawierającą różne liczby i skorzystaj z instrukcji continue, aby wypisać tylko liczby nieparzyste.

numbers = [13, 542, 26, 87, 103]

for number in numbers:
    if number % 2 == 0:
        continue
    print(number)


# zadanie 54
# defnionowanie funkcji - obieranie ziemniaków

def peel_the_potatoes():
    expected_potatoes = int(input("Ile ziemniaków chcesz na obiad? "))
    potatoes =  []
    while len(potatoes) < expected_potatoes:
        print("Obieram ziemnaika...")
        print("I wrzucam go do garnka")
        potatoes.append("Ziemniak")
    print(potatoes)


# zadanie 55
# Napisz funkcję, która obliczy pole poeiwrzchni prostokąta na podstawie długości jego boków.

def pole_prostokata(a, b):
    pole = a * b
    return pole

def zapytaj_o_wartosc(message):
    wprowadzona_wartosc = input(message)
    return int(wprowadzona_wartosc)

a = zapytaj_o_wartosc("Jaka jest długość boku a? ")
b = zapytaj_o_wartosc("Jaka jest długość boku b? ")

pole = pole_prostokata(a, b)
print(f"Pole prostokąta wynosi {pole:.2f}")


# zadanie 56
# Napisz funkcję liczącą prędkość średnią na podstawie zadanego dystansu i czasu.
# Następnie wykorzystaj ją implementując program, który wyznaczy:
# średnią prędkość biegu
# średnią prędkość jazdy na rowerze
# średnią prędkość jazdy autem

def average_speed(distance, time):
    return distance / time

running_distance = float(input("Ile km przebiegłeś? "))
running_time = float(input("Ile godzin Ci to zajęło? "))
bike_ride_distance = float(input("Ile km przejechałeś na rowerze? "))
bike_ride_time = float(input("Ile godzin Ci to zajęło? "))
car_drive_distance = float(input("Ile km przejechałeś autem? "))
car_drive_time = float(input("Ile godzin Ci to zajęło? "))

print(f"Twoja średnia prędkość biegu to {average_spped(running_distance, running_time)} km/h")
print(f"Twoja średnia prędkość jazdy rowerem to {average_speed(bike_ride_distance, bike_ride_time)} km/h")
print(F"Twoja średnia prędkość jazdy autem to {average_speed(car_drive_distance, car_drive_time)} km/h}")

# zadanie 57
# zadanie takie jak powyżej, tylko z zastosowaniem argumentów nazwanych

def avg_speed(distance, time):
    return distance / time

def run_avg_speed_calculator(vehicle_name):
    distance = float(input(f"Ile km pokonałeś za pomocą {vehicle_name}? "))
    time = float(input("Ile godzin Ci to zajęło? "))
    average_speed = avg_speed(distance=distance, time=time)
    print(f"Twoja średnia przemieszczania sią za pomocą {vehicle_name} to {average_speed} km/h")

run_avg_speed_calculator(vehicle_name="biegu")
run_avg_speed_calculator(vehicle_name="roweru")
run_avg_speed_calculator(vehicle_name="samochodu")

# zadanie 58
# Kalkulator wartości lokaty z funkcjami

def calculate_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage / 100) ** years
    return result

def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)

print("Kalkulator wartości lokaty z roczną kapitalizacją")

initial_value = ask_for_int_value("Jaką kwotę wpłaciłeś? ")
percentage = ask_for_int_value("Jakie jest oprocentowanie (%)? ")
years = ask_for_int_value("Ile lat trwa lokata? ")

final_value = calculate_investment_value(initial_value, percentage, years)
print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

longer_term = years * 2
alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
print(f"Rozważ zostawienie lokaty na {longer_term} lat - będzie wtedy warta {alternative_value:.2f}")



# zadanie 59
# inny przykład kalkulatora wartości lokaty z funkcjami

def calculate_investment_value(initial_value, percentage, years):
    result = initial_value * (1 + percentage / 100) ** years
    return result

def ask_for_int_value(message):
    input_value = input(message)
    return int(input_value)

def run_investment_calculator():
    print("Kalkulator wartości lokaty z roczną kapitalizacją")

    initial value = ask_for_int_value("Jaką kwotę wpłaciłeś? ")
    percentage = ask_for_int_value("Jakie jest oprocentowanie (%)? ")
    years = ask_for_int_value("Ile lat trwa lokata? ")

    final_value = calculate_investment_value(initial_value, percentage, years)
    print(f"Po {years} latach Twoja lokata będzie warta {final_value:.2f}")

    longer_term = years * 2
    alternative_value = calculate_investment_value(initial_value, percentage, longer_term)
    print(f"Rozważ zostawienie lokaty na {longer_term} lat - będzie wtedy warta {alternative_value:.2f}")

option = None
while option != "X":
    run_investment_calculator()
    option = input("Aby przerwać, wprowadz 'X', wpisz inny znak, aby kontynuować: ")


# zadanie 60
# Napisz funkcję, która podaną liczbę zamieni na zakres.
# Domyślnie przyjmujemy zakres jako +/- 10% podanej wartości.

def value_with_tolerance(value, tolerance_percentage=10):
    tolerance_value = tolerance_percentage * value / 100
    return [value - tolerance_value, value + tolerance_value]

print(value_with_tolerance(value=100))
print(value_with_tolerance(value=100, tolerance_percentage=40))

# zadanie 61
# Napisz funkcję, dodającą kolejne osoby do listy osób uczęszczających na zajęcia.
# Funkcja przyjmuje napis, który zawiera imiona rozdzielone przecinkiem oraz listę już zapisanych osób, która domyślnie jest pusta.

def add_people_to_classes(names_str, participants=None):
    if participants is None:
        participants = []
    names = names_str.split(',')
    for name in names:
        participants.append(name)
    return participants

attendees_names = "Ola, Bob, Ala, Kuba"
monday_course_participants = add_people_to_classes(attendees_names)
print(monday_course_participants)

attendees_names = "Paweł, Dominika"
monday_course_participants = add_people_to_classes(attendees_name, participants=monday_course_participants)
print(monday_course_participants)

attendees_names = "Ania, Krzysztof"
friday_course_participants = add_people_to_classes(attendees_names)
print(friday_course_participants)



