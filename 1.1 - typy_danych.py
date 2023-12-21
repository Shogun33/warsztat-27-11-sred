print("Hi,", "Tadeusz to ja")
# 2 x shift - podręczna wyszukiwarka
print(type("Tadek"))  # <class 'str'> - typ znakowy - teksty
print(39)
print(type(39))  # <class 'int'> - liczby całkowite
print("93")
print(type("93"))  # <class 'str'>
print("93" + "93")  # konkatenacja - łączenie stringów 9393
print(93 + 93)
# PEP8 ctr alt l - dostosowanie kodu do PEP8
print(5 * "93")  # 9393939393
# zmienna
# pudełko o można wrzucić co chcemy
# nie musimy określac typu
# w każdej chwili możemy wrzucić inny typ danych
wiek = "Tadek"
print(type(wiek))
wiek: int = 54  # tylko podpowiedź (hint), nie sprawdza typu
print(type(wiek))
print(wiek)
wiek = "Tadek"
print(wiek)
# silne typowanie
# print(14 + "23")  # TypeError: unsupported operand type(s) for +: 'int' and 'str'
# sam nie zmiena typu, musimy jawnie zmienić typ
print(int("14") + 23)  # 37 int()  - rzutowanie na typ całkowity

wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float - liczby zmiennoprzecinkowe
print(type(temp))

print(0.1 + 0.5)  # 0.6
print(0.1 + 0.7)  # 0.7999999999999999
print(0.1 + 0.2)  # 0.30000000000000004
# float -  w postaci wykładniczej n * 2 ^ x
# błąd zaokrąglenia
# decimal - np.: do liczenia pieniedzy, operacje wolniejsze

print(wiek + rok)
print(wiek * rok)
print(wiek - rok)
print(wiek / rok)  # 0.023232822540781017
print(wiek // rok)  # 0 - CZĘŚĆ CAŁKOWITA Z DZIELENIA
print(wiek % rok)  # modulo, reszta z dzielenia
# 47 % 2023 = 0 całych i 47 reszty
print(5 % 2)  # reszta 0 lub 1

print(wiek ** rok)  # potęgowanie
print(54 - 5 * 43 + 4 / 2 + 4 / 2)  # -157.0
print(54 - (5 * 43) + (4 / 2 + 4) / 2)  # -158.0

print("Tadek")
print('Tadek')

print(wiek, rok)
print(wiek, rok, sep=";", end="")
print("Tadek")
print("kolejna linia")

imie = "Tadek"
print("Twoje imię %s" % 39.7)
# Twoje imię 39.7
# weryfikuje typ
# %s - stringa
# %i - inta
# print("Twoje imię %i" % imie) # TypeError: %i format: a real number is required, not str

print("Twoje imie {}".format(imie))  # Twoje imie Tadek
print(f"Sprawdzam zmienna temp {temp} i wiek {wiek}")  # f-stringi formatowanie stri
# Sprawdzam zmienna temp 36.6 i wiek 47

wersja = 3.900001  # float
print(f"Używamy wersji pythona {wersja}")  # Używamy wersji pythona 3.900001
print(f"Używamy wersji pythona {wersja:.2f}")  # Używamy wersji pythona 3.900001
# print(f"Używamy wersji pythona {wersja:.}")  # Używamy wersji pythona 3.900001
# print(f"Używamy wersji pythona [wersja")  # Używamy wersji pythona 3.900001

print(f"""
Tekst wielolinijkowy
   kolejna linijka
""")

print((f"dodaj tabulator,\n\t w kolejnej linii\b"))

# \n - nowa linia
# \t - tabulator
# \b - backspace


imie = " Tadek Tadek"
print(type(imie))  # <class 'str'>

imie.lower()  # zmienna ma małe literki
print(imie.lower())
imie2 = imie.lower()
print(imie2)
print(imie)
# upper, capitalize, title
print(imie.capitalize())
print(imie.upper())
print(imie.title())

print(imie.replace(" ", "&"))
print(imie.count("a"))
print(imie)
print(len(imie))  # długość sekwencji
# tekst posiada indeks
# indeksowanie od 0
print(imie[0])  # wypisanie literki o indeksie 0 T - pierwsza literka
print(imie.count(imie, 0, 3))  # 0 bierze: Tad 0,1,2 - indeks 3 już nie brany
print(imie.count("a", 0, 3))  # 1 jedna literka "a", bierze: Rad 0,1,2 - indeks 3 już nie brany
print(imie.count("e", 0, 3))  # 0, bierze: Rad 0,1,2 - indeks 3 już nie brany

liczba = 4234234234324
print((f"Nasza duża liczba {liczba}"))
print((f"Nasza duża liczba {liczba:,}"))
print((f"Nasza duża liczba {liczba:,}".replace(",", ".")))
print((f"Nasza duża liczba {liczba:,}".replace(",", " ")))

liczba2 = 1111112.768
print((f"Nasza duża liczba {liczba2:,}".replace(",", " ")))

# typ logiczny
# przyjmuje wartości: prawda lub fałsz
czy_znasz_python = True  # prawda
czy_znasz_python = False  # fałsz
print((czy_znasz_python))  # False
print(int(czy_znasz_python))  # 1
print(bool(1))  # True bool() - zmiana na typ bool() - logiczny
print(bool(100))  # True
print(bool(-10))
print(bool("Tadek"))  # True
print(bool(0))  # False
print(bool(""))  # False
print(bool(None))  # False -> None - nic, null
# komentarz
"""
komentarz wielolinijkowy

"""

tekst = "    Tekst  "
print(tekst.strip())  # "Tekst" czyści białe znaki na początku i na końcu
print(tekst.lstrip())  # "Tekst   "
tekst_x = "witaj świecie"
encoded_s = tekst_x.encode('utf-8')
print(encoded_s)  # b'witaj \xc5\x9bwiecie'
# \x  - zapis w postaci szesnastkowej
# \xc5 = 197
print(encoded_s.decode('utf-8'))  # witaj świecie
print(ord("1"))  # 49
print(chr(49))  # 1
print("\u0105")  # ą
