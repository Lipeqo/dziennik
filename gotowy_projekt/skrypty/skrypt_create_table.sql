-- Tworzenie bazy danych, jeśli nie istnieje
CREATE DATABASE IF NOT EXISTS Szkola;

USE Szkola;
CREATE TABLE Tablica_Klasa (
    Klasa_Id INT AUTO_INCREMENT PRIMARY KEY, 
    Klasa_Nazwa VARCHAR(100)  
);

CREATE TABLE Tablica_Uczen (
    Uczen_Id INT AUTO_INCREMENT PRIMARY KEY, 
    Uczen_Imie VARCHAR(100), 
    Uczen_Nazwisko VARCHAR(100),
    Uczen_Klucz_Obcy_Klasa INT,
    FOREIGN KEY (Uczen_Klucz_Obcy_Klasa) REFERENCES Tablica_Klasa(Klasa_ID)
);

CREATE TABLE Tablica_Nauczyciel
(
    Nauczyciel_ID INT AUTO_INCREMENT PRIMARY KEY, 
    Nauczyciel_Imie VARCHAR(100), 
    Nauczyciel_Nazwisko VARCHAR(100),
    Nauczyciel_Klucz_Obcy_Klasa INT,
    FOREIGN KEY (Nauczyciel_Klucz_Obcy_Klasa) REFERENCES Tablica_Klasa(Klasa_ID)
);
