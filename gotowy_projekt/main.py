import mysql.connector


# Funkcja do łączenia z bazą i wykonywania zapytania wstawiającego
def baza_danych_wstawienie(query, dane):
    obiekt = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Szkola"
    )
    cursor = obiekt.cursor()
    cursor.execute(query, dane)
    obiekt.commit()
    print("Dane zostały wstawione do bazy.")
    cursor.close()
    obiekt.close()


# Funkcja do łączenia z bazą i pobierania danych
def baza_danych_pobranie(query, dane):
    obiekt = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Szkola"
    )
    cursor = obiekt.cursor()
    cursor.execute(query, dane)
    wynik = cursor.fetchall()
    cursor.close()
    obiekt.close()
    return wynik


# Funkcja do wyświetlania dostępnych komend
def komendy():
    print("? - wyswietl komendy")
    print("exit - wyjscie z programu")
    print("addc - dodaj nową klasę")
    print("adds - dodaj nowego ucznia")
    print("addt - dodaj nowego nauczyciela do klasy")
    print("seea - zobacz cala klase")
    print("dels - usun ucznia")
    print("delt - usun nauczyciela")
    print("delc - usun klase")


# Funkcja sprawdzająca, czy klasa istnieje w bazie
def jakie_sa_klasy(k):
    lista = baza_danych_pobranie("SELECT Klasa_Id FROM Tablica_Klasa WHERE Klasa_Nazwa = %s;", (k,))
    if lista:
        return lista[0][0]  # Zwraca Klasa_Id, czyli pierwszy element z krotki
    else:
        return None  # Jeśli klasy nie ma w bazie


def nauczyciel_dla_klasy(k):
    # Zapytanie SQL z połączeniem tabeli Tablica_Klasa i Tablica_Nauczyciel
    query = """
    SELECT 
        CONCAT(TN.Nauczyciel_Imie, ' ', TN.Nauczyciel_Nazwisko) AS Nauczyciel
    FROM 
        Tablica_Klasa AS TK
    INNER JOIN Tablica_Nauczyciel AS TN 
        ON TK.Klasa_ID = TN.Nauczyciel_Klucz_Obcy_Klasa
    WHERE 
        TK.Klasa_Nazwa = %s;
    """

    # Wykonaj zapytanie
    lista = baza_danych_pobranie(query, (k,))  # Przekazujemy nazwę klasy jako parametr

    if lista:
        return lista[0][0]  # Zwraca imię i nazwisko nauczyciela
    else:
        return False  # Jeśli nauczyciela nie ma dla danej klasy


# Główny program
while True:
    print("Witaj w aplikacji dziennik w konsoli")
    komendy()
    while True:
        odp = input(">>> ").strip().lower()  # Pobranie komendy od użytkownika.

        if odp == "?":
            komendy()
        elif odp == "exit":
            exit()
        elif odp == "addc":
            odpw = input("Podaj nazwę klasy >>> ").strip().upper()
            if odpw:
                query = "INSERT INTO Tablica_Klasa (Klasa_Nazwa) VALUES (%s)"
                baza_danych_wstawienie(query, (odpw,))
            else:
                print("Bład, nie podałeś nazwy klasy")
        elif odp == "adds":
            odpw1 = input("Podaj imie ucznia >>> ").strip().capitalize()
            odpw2 = input("Podaj nazwisko ucznia >>> ").strip().capitalize()
            odpw3 = input("Podaj klasę ucznia (Nazwę Klasy) >>> ").strip().upper()

            if odpw1 and odpw2 and odpw3:
                klasa_id = jakie_sa_klasy(odpw3)  # Sprawdzanie ID klasy na podstawie nazwy
                if klasa_id:
                    query = "INSERT INTO Tablica_Uczen (Uczen_Imie, Uczen_Nazwisko, Uczen_Klucz_Obcy_Klasa) VALUES (%s, %s, %s)"
                    baza_danych_wstawienie(query, (odpw1, odpw2, klasa_id))  # Wstawianie ucznia do bazy
                    print("Udalo się dodać ucznia.")
                else:
                    print("Błąd: Klasa nie istnieje w bazie!")
            else:
                print("Błąd, sprawdź dane ucznia (imię, nazwisko, ID klasy)")
        elif odp == "addt":
            odpw1 = input("Podaj imie nauczyciela >>> ").strip().capitalize()
            odpw2 = input("Podaj nazwisko nauczyciela >>> ").strip().capitalize()
            odpw3 = input("Podaj klasę nauczyciela (Nazwę Klasy) >>> ").strip().upper()
            if odpw1 and odpw2 and odpw3:
                klasa_id = jakie_sa_klasy(odpw3)  # Sprawdzanie ID klasy na podstawie nazwy
                if klasa_id:
                    query = "INSERT INTO Tablica_Nauczyciel (Nauczyciel_Imie, Nauczyciel_Nazwisko, Nauczyciel_Klucz_Obcy_Klasa) VALUES (%s, %s, %s);"
                    baza_danych_wstawienie(query, (odpw1, odpw2, klasa_id))  # Wstawianie ucznia do bazy
                    print("Udalo się dodać nauczyciela.")
                else:
                    print("Błąd: Klasa nie istnieje w bazie!")

        elif odp == "seea":
            odpw1 = input("Podaj jaka klase chcesz zobaczyc >>> ").strip().upper()

            if jakie_sa_klasy(odpw1):

                if nauczyciel_dla_klasy(odpw1) == None:
                    nauczyciel = "Nie przydzielono nauczyciela do klasy"
                else:
                    nauczyciel = nauczyciel_dla_klasy(odpw1)  # pobranie nauczyciela

                    print(f"Wychowawca klasy: {nauczyciel}")

                    lista = baza_danych_pobranie(
                        "SELECT CONCAT(TU.Uczen_Imie, ' ', TU.Uczen_Nazwisko) AS Uczen FROM Tablica_Klasa AS TK INNER JOIN Tablica_Uczen AS TU ON TK.Klasa_ID = TU.Uczen_Klucz_Obcy_Klasa WHERE TK.Klasa_Nazwa = %s;",
                        (odpw1,))

                    # Iteracja po wszystkich uczniach i wyświetlanie indeksu oraz imienia i nazwiska
                    for idx, e in enumerate(lista, start=1):  # 'start=1' zaczyna numerowanie od 1
                        print(f"{idx}. {e[0]}")
            else:
                print("Nie ma takiej klasy")
        elif odp == "dels":
            odpw1 = input("Podaj imię ucznia >>> ").strip().capitalize()
            odpw2 = input("Podaj nazwisko ucznia >>> ").strip().capitalize()
            odpw3 = input("Podaj nazwę klasy ucznia >>> ").strip().upper()

            klasa_id = jakie_sa_klasy(odpw3)

            if klasa_id:
                # Sprawdzenie, czy taki uczeń istnieje
                query_check = """
                SELECT * FROM Tablica_Uczen 
                WHERE Uczen_Imie = %s AND Uczen_Nazwisko = %s AND Uczen_Klucz_Obcy_Klasa = %s
                """
                wynik = baza_danych_pobranie(query_check, (odpw1, odpw2, klasa_id))

                if wynik:
                    # Jeśli istnieje, usuwamy
                    query_delete = """
                    DELETE FROM Tablica_Uczen 
                    WHERE Uczen_Imie = %s AND Uczen_Nazwisko = %s AND Uczen_Klucz_Obcy_Klasa = %s
                    """
                    baza_danych_wstawienie(query_delete, (odpw1, odpw2, klasa_id))
                    print(f"Uczeń {odpw1} {odpw2} został usunięty z klasy {odpw3}.")
                else:
                    print("Taki uczeń nie istnieje w podanej klasie.")
            else:
                print("Błąd: Podana klasa nie istnieje.")

        elif odp == "delt":
            odpw1 = input("Podaj imię nauczyciela >>> ").strip().capitalize()
            odpw2 = input("Podaj nazwisko nauczyciela >>> ").strip().capitalize()
            odpw3 = input("Podaj nazwę klasy nauczyciela >>> ").strip().upper()

            klasa_id = jakie_sa_klasy(odpw3)

            if klasa_id:
                # Sprawdzenie, czy taki nauczyciel istnieje
                query_check = """
                SELECT * FROM Tablica_Nauczyciel 
                WHERE Nauczyciel_Imie = %s AND Nauczyciel_Nazwisko = %s AND Nauczyciel_Klucz_Obcy_Klasa = %s
                """
                wynik = baza_danych_pobranie(query_check, (odpw1, odpw2, klasa_id))

                if wynik:
                    # Jeśli istnieje, usuwamy
                    query_delete = """
                    DELETE FROM Tablica_Nauczyciel 
                    WHERE Nauczyciel_Imie = %s AND Nauczyciel_Nazwisko = %s AND Nauczyciel_Klucz_Obcy_Klasa = %s
                    """
                    baza_danych_wstawienie(query_delete, (odpw1, odpw2, klasa_id))
                    print(f"Nauczyciel {odpw1} {odpw2} został usunięty z klasy {odpw3}.")
                else:
                    print("Taki nauczyciel nie istnieje w podanej klasie.")
            else:
                print("Błąd: Podana klasa nie istnieje.")

        elif odp == "delc":
            odpw = input("Podaj nazwę klasy do usunięcia >>> ").strip().upper()

            klasa_id = jakie_sa_klasy(odpw)

            if klasa_id:
                # Sprawdzenie, czy klasa istnieje
                query_check = "SELECT * FROM Tablica_Klasa WHERE Klasa_Nazwa = %s"
                wynik = baza_danych_pobranie(query_check, (odpw,))

                if wynik:
                    # Jeśli istnieje, usuwamy uczniów i nauczycieli przypisanych do klasy (jeśli istnieją)
                    query_delete_uczniowie = "DELETE FROM Tablica_Uczen WHERE Uczen_Klucz_Obcy_Klasa = %s"
                    query_delete_nauczyciele = "DELETE FROM Tablica_Nauczyciel WHERE Nauczyciel_Klucz_Obcy_Klasa = %s"
                    query_delete_klasa = "DELETE FROM Tablica_Klasa WHERE Klasa_Id = %s"

                    baza_danych_wstawienie(query_delete_uczniowie, (klasa_id,))
                    baza_danych_wstawienie(query_delete_nauczyciele, (klasa_id,))
                    baza_danych_wstawienie(query_delete_klasa, (klasa_id,))

                    print(f"Klasa {odpw} oraz powiązani uczniowie i nauczyciele zostali usunięci.")
                else:
                    print("Taka klasa nie istnieje w bazie.")
            else:
                print("Błąd: Podana klasa nie istnieje.")


        else:
            continue
