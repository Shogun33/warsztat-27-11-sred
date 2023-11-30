# zadanie 1
# stworzenie książki telefonicznej z wykorzystaniem pętli while, jako głuwnej pętli programu
# książka powinna zawierać możliwość: dodaj kontakt, usuń kontakt, wyszukaj kontakt, wyświetl kontakty

# ---------------- z chat GPT ---------------------
class KsiazkaTelefoniczna:
    def __init__(self):
        self.kontakty = {}

    def dodaj_kontakt(self, imie, numer):
        self.kontakty[imie] = numer
        print(f"Dodano kontakt: {imie} - {numer}")

    def usun_kontakt(self, imie):
        if imie in self.kontakty:
            del self.kontakty[imie]
            print(f"Usunięto kontakt: {imie}")
        else:
            print(f"Brak kontaktu o imieniu {imie}")

    def wyszukaj_kontakt(self, imie):
        if imie in self.kontakty:
            print(f"Numer telefonu dla {imie}: {self.kontakty[imie]}")
        else:
            print(f"Brak kontaktu o imieniu {imie}")

    def wyswietl_kontakty(self):
        print("Lista kontaktów:")
        for imie, numer in self.kontakty.items():
            print(f"{imie} - {numer}")


# Główna pętla programu
ksiazka = KsiazkaTelefoniczna()

while True:
    print("\nMenu:")
    print("1. Dodaj kontakt")
    print("2. Usuń kontakt")
    print("3. Wyszukaj kontakt")
    print("4. Wyświetl kontakty")
    print("5. Wyjście")

    wybor = input("Wybierz opcję (1-5): ")

    if wybor == '1':
        imie = input("Podaj imię: ")
        numer = input("Podaj numer telefonu: ")
        ksiazka.dodaj_kontakt(imie, numer)

    elif wybor == '2':
        imie = input("Podaj imię kontaktu do usunięcia: ")
        ksiazka.usun_kontakt(imie)

    elif wybor == '3':
        imie = input("Podaj imię kontaktu do wyszukania: ")
        ksiazka.wyszukaj_kontakt(imie)

    elif wybor == '4':
        ksiazka.wyswietl_kontakty()

    elif wybor == '5':
        print("Zakończono program.")
        break

    else:
        print("Nieprawidłowy wybór. Wybierz liczbę od 1 do 5.")

# -------------------- z zajęć -----------------------

contacts = {}
while True:
    print(f"""
    1. Dodaj kontakt
    2. Usuń kontakt
    3. Wyszukaj kontakt
    4. Wyświetl liste kontaktow
    5. Koniec
""")
    try:
        odp = input("Wybierz opcję")
        if odp == "1":
            name = input("Podaj imie kontaktu")
            number = input("Podaj numer telefonu (tylko cyfry)")
            if not number.isdigit():
                raise ValueError("Numer telefonu powinien zawierać cyfry!")
            else:
                contacts[name.lower()] = number
                print(f"Kontakt {name} został dodany")
        elif odp == "2":
            name = input("Podaj imię kontaktu do usunięcia")
            if name in contacts:
                # del contacts[name]
                contacts.pop(name.lower())
                print(f"Kontakt {name} został usunięty")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "3":
            name = input("Podaj imię kontaktu do wyszukania")
            if name.lower() in contacts:

                print(f"Kontakt {name} nr telefonu: {contacts[name.lower()]} ")
            else:
                print(f"Nie znaleziono kontaktu o imieniu {name}")
        elif odp == "4":
            print(f"Lista kontaktów: {contacts}")
        elif odp == "5":
            break
        else:
            print("Błedny wybór z menu")
    except Exception as e:
        print("Bład", e)
