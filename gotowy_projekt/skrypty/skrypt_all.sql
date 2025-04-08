-- Tworzenie bazy danych, jeśli nie istnieje
CREATE DATABASE IF NOT EXISTS Szkola;

-- Przełączanie na bazę Szkola
USE Szkola;

-- Tworzenie tabel
CREATE TABLE IF NOT EXISTS Tablica_Klasa (
    Klasa_Id INT AUTO_INCREMENT PRIMARY KEY, 
    Klasa_Nazwa VARCHAR(100)  
);

CREATE TABLE IF NOT EXISTS Tablica_Uczen (
    Uczen_Id INT AUTO_INCREMENT PRIMARY KEY, 
    Uczen_Imie VARCHAR(100), 
    Uczen_Nazwisko VARCHAR(100),
    Uczen_Klucz_Obcy_Klasa INT,
    FOREIGN KEY (Uczen_Klucz_Obcy_Klasa) REFERENCES Tablica_Klasa(Klasa_ID)
);

CREATE TABLE IF NOT EXISTS Tablica_Nauczyciel (
    Nauczyciel_ID INT AUTO_INCREMENT PRIMARY KEY, 
    Nauczyciel_Imie VARCHAR(100), 
    Nauczyciel_Nazwisko VARCHAR(100),
    Nauczyciel_Klucz_Obcy_Klasa INT,
    FOREIGN KEY (Nauczyciel_Klucz_Obcy_Klasa) REFERENCES Tablica_Klasa(Klasa_ID)
);

-- Wstawianie danych do tabeli Tablica_Klasa (klasa 1A)
INSERT INTO Tablica_Klasa (Klasa_Nazwa) VALUES ('1A');

-- Wstawianie danych uczniów do klasy 1A
INSERT INTO Tablica_Uczen (Uczen_Imie, Uczen_Nazwisko, Uczen_Klucz_Obcy_Klasa)
VALUES
    ('Jan', 'Kowalski', 1),
    ('Anna', 'Nowak', 1),
    ('Piotr', 'Zieliński', 1),
    ('Maria', 'Wójcik', 1),
    ('Tomasz', 'Lewandowski', 1),
    ('Katarzyna', 'Jankowska', 1),
    ('Michał', 'Kwiatkowski', 1),
    ('Aleksandra', 'Mazur', 1),
    ('Jakub', 'Woźniak', 1),
    ('Natalia', 'Kaczmarek', 1),
    ('Patryk', 'Dąbrowski', 1),
    ('Emilia', 'Piotrowska', 1),
    ('Wojciech', 'Grabowski', 1),
    ('Adrianna', 'Nowakowska', 1),
    ('Bartosz', 'Szymański', 1),
    ('Marta', 'Olszewska', 1),
    ('Sebastian', 'Bąk', 1),
    ('Kinga', 'Kamińska', 1),
    ('Maciej', 'Kaczmarek', 1),
    ('Zuzanna', 'Kruk', 1),
    ('Dawid', 'Krawczyk', 1),
    ('Weronika', 'Konieczna', 1),
    ('Szymon', 'Czarnecki', 1),
    ('Magdalena', 'Wojciechowska', 1),
    ('Filip', 'Pawlak', 1);

-- Wstawianie danych nauczyciela do klasy 1A
INSERT INTO Tablica_Nauczyciel (Nauczyciel_Imie, Nauczyciel_Nazwisko, Nauczyciel_Klucz_Obcy_Klasa) 
VALUES ('ImięNauczyciela', 'NazwiskoNauczyciela', 1);
