# stworzenie raport, przetworzenie danych, dane generowane generatorem
# wykorzystać dekorator do pomiaru czasu operacji (time)

import time


def monitor_wydajnosci(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Funkcja wykonana w czasie {end - start} sekund")
        return result

    return wrapper


# generator danych
def generator_danych(dane):
    for element in dane:
        yield element


def przetworz_dane(dane):
    przetworzone_dane = [element for element in dane if element % 2 == 0]
    return przetworzone_dane


@monitor_wydajnosci
def stworz_raport(dane):
    for element in generator_danych(dane):
        print(f"Raport dla elementu: {element}")
        # pass


dane = range(100_000)
prz_dane = przetworz_dane(dane)
stworz_raport(prz_dane)


# --------- z chat GPT ----------------
# import time


# Dekorator do pomiaru czasu operacji
def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed time: {elapsed_time:.6f} seconds")
        return result

    return wrapper


# Generator do generowania danych
def data_generator(n):
    for i in range(n):
        yield i


# Funkcja do przetwarzania danych
@timing_decorator
def process_data(data):
    result = sum(data)  # Przykładowe przetwarzanie danych (suma elementów)
    return result


# Tworzenie raportu
@timing_decorator
def generate_report(data_size):
    data = data_generator(data_size)
    result = process_data(data)
    print(f"Report generated. Result: {result}")


# Użycie funkcji do generowania raportu
generate_report(1000000)
