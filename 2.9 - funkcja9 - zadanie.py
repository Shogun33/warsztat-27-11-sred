# napisanie funkcji, która za pomocą przekazanych argumentów
# zbuduje słownik i zwróci go
# first, name, age=None

# z chat GPT
def build_dictionary(first, name, age=None):
    my_dict = {
        'first': first,
        'name': name,
    }

    if age is not None:
        my_dict['age'] = age

    return my_dict


# Przykłady użycia funkcji:
result1 = build_dictionary('John', 'Doe')
print(result1)

result2 = build_dictionary('Alice', 'Smith', age=25)
print(result2)


# W powyższym przykładzie funkcja build_dictionary przyjmuje trzy argumenty:
# first, name, i opcjonalny argument age, który domyślnie jest ustawiony na None.
# Funkcja tworzy słownik zawierający te wartości, a jeśli age nie jest równy None, dodaje go do słownika.

def build_dictionary_with_input():
    my_dict = {}
    keys = ['first', 'name', 'age']

    i = 0
    while i < len(keys):
        user_input = input(f"Enter {keys[i]}: ")

        # Sprawdzamy, czy użytkownik wprowadził dane
        if user_input:
            my_dict[keys[i]] = user_input
            i += 1
        else:
            print("Please enter a value.")

    return my_dict


# Użycie funkcji
result = build_dictionary_with_input()
print(result)


# W tym przykładzie pętla while będzie kontynuować się,
# dopóki użytkownik nie poda wartości dla wszystkich kluczy.
# Pobierać będzie dane od użytkownika dla każdego klucza z listy keys i dodawać do słownika my_dict.
# Jeśli użytkownik nie wprowadzi wartości, zostanie wyświetlone odpowiednie ostrzeżenie.
# Po uzyskaniu wszystkich danych funkcja zwróci zbudowany słownik.

# -------------- z zajęć -----------------------------

# napisanie funkcji, która za pomoca przekazanych argumentów
# zbuduje słownik i zwroci go
# first, name, age=None

def build_dict(first, name, age=None):
    person = {'first': first, 'name': name}
    if age:
        person['age'] = age

    return person


print(build_dict("radek", "Kowalski"))  # {'first': 'radek', 'name': 'Kowalski'}

while True:
    print("Podaj imię i nazwisko")
    print("Wpisz q by zakończyc")
    f_name = input("Imię:")
    if f_name == 'q':
        break
    l_name = input("Nazwisko: ")
    if l_name == 'q':
        break
    age = input("Wiek: ")
    if age == "q":
        break

    print(build_dict(f_name, l_name, age))
