-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Czas generowania: 11 Sty 2023, 15:11
-- Wersja serwera: 10.4.27-MariaDB
-- Wersja PHP: 8.2.0

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Baza danych: `wypozyczalnia_samochodow`
--

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `dane_logowania`
--

CREATE TABLE `dane_logowania` (
  `id` int(3) NOT NULL,
  `email` text NOT NULL,
  `haslo` int(4) NOT NULL,
  `pracownik` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `dane_logowania`
--

INSERT INTO `dane_logowania` (`id`, `email`, `haslo`, `pracownik`) VALUES
(1, 'andersik@wp.pl', 1110, 'yes'),
(2, 'nowacki_m@onet.pl', 1111, 'yes'),
(3, 'mrozno_andrej@wp.pl', 1112, 'yes'),
(4, 'gwoliczka_f@gmail.com', 1113, 'yes'),
(5, 'anetka_pawlak@wp.pl', 1114, 'yes'),
(6, 'stelmaszczyk@wp.pl', 1115, 'No'),
(7, 'wrzosek_adam@gmail.com', 1116, 'No'),
(8, 'mati_25@onet.pl', 1117, 'No'),
(10, 'konstytycja_jest_ok@gmail.com', 1119, 'No'),
(11, 'mlody_stary@wp.pl', 1120, 'No'),
(12, 'monia21@gmail.com', 1121, 'No'),
(13, 'ecza_pecza@onet.pl', 1122, 'No'),
(14, 'marunio@wp.pl', 1123, 'No'),
(15, 'karwowski_tomek@gmail.com', 1124, 'No'),
(16, 'witkowa17@onet.pl', 1125, 'No'),
(17, 'zbusiu@wp.pl', 1126, 'No'),
(18, 'stefanek_m@wp.pl', 1127, 'No'),
(19, 'wiolka_f@onet.pl', 1128, 'No'),
(20, 'malcze_fr@gmail.com', 1129, 'No'),
(21, 'mro_wik@gmail.com', 1130, 'No');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `dane_wypozyczen`
--

CREATE TABLE `dane_wypozyczen` (
  `id_wypozyczenia` int(11) NOT NULL,
  `id_klienta` int(11) NOT NULL,
  `id_samochodu` int(11) NOT NULL,
  `data_wyp` date DEFAULT NULL,
  `data_zwr` date DEFAULT NULL,
  `suma` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `dane_wypozyczen`
--

INSERT INTO `dane_wypozyczen` (`id_wypozyczenia`, `id_klienta`, `id_samochodu`, `data_wyp`, `data_zwr`, `suma`) VALUES
(1, 2, 6, '2023-01-10', '2023-01-24', 4200),
(2, 2, 1, '2023-01-10', '2023-01-26', 2400);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `klienci`
--

CREATE TABLE `klienci` (
  `id_klienta` int(11) NOT NULL,
  `imie_klienta` varchar(45) DEFAULT NULL,
  `nazwisko_klienta` varchar(45) DEFAULT NULL,
  `telefon_klienta` varchar(14) DEFAULT NULL,
  `email_klienta` varchar(50) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `klienci`
--

INSERT INTO `klienci` (`id_klienta`, `imie_klienta`, `nazwisko_klienta`, `telefon_klienta`, `email_klienta`) VALUES
(1, 'Damian', 'Stelmach', '985-746-350', 'stelmaszczyk@wp.pl'),
(2, 'Adam', 'Wrzosek', '756-358-068', 'wrzosek_adam@gmail.com'),
(3, 'Mateusz', 'Karwowski', '674-968-785', 'mati_25@onet.pl'),
(4, 'Anna', 'Ajewska', '455-734-224', 'konstytycja_jest_ok@gmail.com'),
(5, 'Dawid', 'Stary', '485-236-150', 'mlody_stary@wp.pl'),
(6, 'Monika', 'Młoda', '985-749-607', 'monia21@gmail.com'),
(7, 'Weronika', 'Eczarska', '185-716-150', 'ecza_pecza@onet.pl'),
(8, 'Marek', 'Marecki', '856-368-028', 'marunio@wp.pl'),
(9, 'Tomasz', 'Karwowski', '485-769-617', 'karwowski_tomek@gmail.com'),
(10, 'Grażyna', 'Witkowska', '345-726-354', 'witkowa17@onet.pl'),
(11, 'Zbigniew', 'Swawolny', '726-358-088', 'zbusiu@wp.pl'),
(12, 'Stefan', 'Maciejewski', '785-729-647', 'stefanek_m@wp.pl'),
(13, 'Wioletta', 'Frywolna', '685-700-323', 'wiolka_f@onet.pl'),
(14, 'Franciszek', 'Malczewska', '746-318-168', 'malcze_fr@gmail.com'),
(15, 'Wiktoria', 'Mrozek', '985-249-628', 'mro_wik@gmail.com');

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `pracownicy`
--

CREATE TABLE `pracownicy` (
  `id_pracownika` int(11) NOT NULL,
  `imie_pracownika` varchar(45) DEFAULT NULL,
  `nazwisko_pracownika` varchar(45) DEFAULT NULL,
  `miasto_pracownika` varchar(45) DEFAULT NULL,
  `telefon_pracownika` varchar(14) DEFAULT NULL,
  `email_pracownika` varchar(50) DEFAULT NULL,
  `szef_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `pracownicy`
--

INSERT INTO `pracownicy` (`id_pracownika`, `imie_pracownika`, `nazwisko_pracownika`, `miasto_pracownika`, `telefon_pracownika`, `email_pracownika`, `szef_id`) VALUES
(1, 'Wojciech', 'Anders', 'Wrocław', '185-256-340', 'andersik@wp.pl', NULL),
(2, 'Modest', 'Nowacki', 'Brzeg', '868-456-351', 'nowacki_m@onet.pl', 1),
(3, 'Andrzej', 'Mróz', 'Kąty Wrocławskie', '185-286-850', 'mrozno_andrej@wp.pl', 2),
(4, 'Franciszka', 'Gwolik', 'Wrocław', '285-897-250', 'gwoliczka_f@gmail.com', 2),
(5, 'Aneta', 'Pawlak', 'Wrocław', '485-757-223', 'anetka_pawlak@wp.pl', 2);

-- --------------------------------------------------------

--
-- Struktura tabeli dla tabeli `samochody`
--

CREATE TABLE `samochody` (
  `id_samochodu` int(11) NOT NULL,
  `marka` varchar(20) DEFAULT NULL,
  `model` varchar(20) DEFAULT NULL,
  `data_prod` year(4) DEFAULT NULL,
  `dostepnosc` int(11) DEFAULT NULL,
  `cena` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Zrzut danych tabeli `samochody`
--

INSERT INTO `samochody` (`id_samochodu`, `marka`, `model`, `data_prod`, `dostepnosc`, `cena`) VALUES
(1, 'opel', 'astra', 2000, 2, 150),
(2, 'mercedes', 'CLK', 2011, 3, 200),
(3, 'audi', 'A4', 2012, 1, 150),
(4, 'bmw', '3', 2015, 3, 250),
(5, 'renault', 'clio', 2022, 3, 300),
(6, 'opel', 'corsa', 2022, 1, 300),
(7, 'mercedes', 'S', 2021, 4, 500),
(8, 'audi', 'A8', 2019, 5, 350),
(9, 'bmw', 'X6', 2018, 3, 300),
(10, 'renault', 'megane', 2017, 2, 300),
(11, 'ford', 'mondeo', 2005, 1, 100);

--
-- Indeksy dla zrzutów tabel
--

--
-- Indeksy dla tabeli `dane_logowania`
--
ALTER TABLE `dane_logowania`
  ADD PRIMARY KEY (`id`);

--
-- Indeksy dla tabeli `dane_wypozyczen`
--
ALTER TABLE `dane_wypozyczen`
  ADD PRIMARY KEY (`id_wypozyczenia`);

--
-- Indeksy dla tabeli `klienci`
--
ALTER TABLE `klienci`
  ADD PRIMARY KEY (`id_klienta`);

--
-- Indeksy dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  ADD PRIMARY KEY (`id_pracownika`);

--
-- Indeksy dla tabeli `samochody`
--
ALTER TABLE `samochody`
  ADD PRIMARY KEY (`id_samochodu`);

--
-- AUTO_INCREMENT dla zrzuconych tabel
--

--
-- AUTO_INCREMENT dla tabeli `dane_logowania`
--
ALTER TABLE `dane_logowania`
  MODIFY `id` int(3) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=22;

--
-- AUTO_INCREMENT dla tabeli `dane_wypozyczen`
--
ALTER TABLE `dane_wypozyczen`
  MODIFY `id_wypozyczenia` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=83;

--
-- AUTO_INCREMENT dla tabeli `klienci`
--
ALTER TABLE `klienci`
  MODIFY `id_klienta` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT dla tabeli `pracownicy`
--
ALTER TABLE `pracownicy`
  MODIFY `id_pracownika` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT dla tabeli `samochody`
--
ALTER TABLE `samochody`
  MODIFY `id_samochodu` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=12;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
