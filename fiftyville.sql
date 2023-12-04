-- Keep a log of any SQL queries you execute as you solve the mystery.

-- Look in description for 'theft':
SELECT DISTINCT(street) FROM crime_scene_reports
WHERE description LIKE '%theft%';
-- Humphrey Street appears.

-- Look for the description with the information of 'theft'and 'Humphrey Street':
SELECT description FROM crime_scene_reports
WHERE description LIKE '%theft%' AND street = 'Humphrey Street';
-- Theft of the cs50 duck took place at 10:15am at the Humphrey Street bakery.
-- Interviews were conducted today with three witnesses who were present at the time - each of their interview transcripts mentions the bakery.

-- Look up name of the witnesses:
SELECT name FROM interviews
WHERE transcript LIKE '%bakery%' AND year = 2021 AND month = 7 AND day = 28;
-- Three names appear:
-- Ruth
-- Eugene
-- Raymond

-- Look up the transcripts from the interviews with Ruth, Eugene and Raymond:
SELECT name, transcript FROM interviews
WHERE name = 'Ruth' AND transcript LIKE '%bakery%' AND year = 2021 AND month = 7 AND day = 28;
-- Transcript:
-- Ruth: Within 10 minutes of the teft, thief left bakery parkinglot.
SELECT name, transcript FROM interviews
WHERE name = 'Eugene' AND transcript LIKE '%bakery%' AND year = 2021 AND month = 7 AND day = 28;
-- Transcript:
-- Eugene: recognized, someone he had seen in the morning at the ATM on Leggett Street, withdrawing some money.
SELECT name, transcript FROM interviews
WHERE name = 'Raymond' AND transcript LIKE '%bakery%' AND year = 2021 AND month = 7 AND day = 28;
-- Transcript:
-- Raymond: As the thief was leaving the bakery, they called someone who talked to them for less than a minute.
-- In the call I heard the thief say that they were planning to take the earliest flight out of Fiftyville tomorrow.
-- The tief then asked the person on the other end of the phone to purchase the flight ticket.

-- Look up the license_plate by the bakery, year 2021, month 7, day 28, hour 10, minute 15 + 10 min:
SELECT license_plate, minute FROM bakery_security_logs
WHERE year = 2021 AND month = 7 AND day = 28 AND hour = 10;
-- 13FNH73 10:14
-- 5P2BI95 10:16
-- 94KL13X 10:18
-- 6P58WS2 10:18
-- 4328GD8 10:19
-- G412CB7 10:20
-- L93JTIZ 10:21
-- 322W7JE 10:23
-- ONTHK55 10:23

-- Get the account_number of the one withdrawing money at the ATM on Leggett Street:
SELECT account_number FROM atm_transactions
WHERE atm_location = 'Leggett Street' AND transaction_type = 'withdraw' AND year = 2021 AND month = 7 AND day = 28;
-- account numbers:
-- 28500762
-- 28296815
-- 76054385
-- 49610011
-- 16153065
-- 25506511
-- 81061156
-- 26013199

-- Get the names of the accountnumbers:
SELECT people.name, bank_accounts.account_number
FROM people
JOIN bank_accounts ON bank_accounts.person_id = people.id
WHERE bank_accounts.account_number = 28500762 OR bank_accounts.account_number = 28296815 OR bank_accounts.account_number = 76054385
OR bank_accounts.account_number = 49610011 OR bank_accounts.account_number = 16153065 OR bank_accounts.account_number = 25506511
OR bank_accounts.account_number = 81061156 OR bank_accounts.account_number = 26013199;
-- Bruce    49610011
-- Diana    26013199
-- Brooke   16153065
-- Kenny    28296815
-- Iman     25506511
-- Luca     28500762
-- Taylor   76054385
-- Benista  81061156

-- Get the plate numbers of the people above:
SELECT name FROM people
WHERE license_plate = '13FNH73' OR license_plate = '5P2BI95' OR license_plate = '94KL13X'
OR license_plate = '6P58WS2' OR license_plate = '4328GD8' OR license_plate = 'G412CB7'
OR license_plate = 'L93JTIZ' OR license_plate = '322W7JE' OR license_plate = 'ONTHK55';
-- Same names as the names above (suspects):
-- Iman
-- Luca
-- Diana
-- Bruce

-- Lets take a look at the phonecalls. Names of the people that made a phonecall less then a minute at that date:
SELECT name FROM people
JOIN phone_calls ON phone_calls.caller = people.phone_number
WHERE duration < 60 AND year = 2021 AND month = 7 AND day = 28;
-- Same names as the names above (suspects):
-- Bruce
-- Diana

-- Names of the people dat received a phonecall from Bruce or Diana less then a minute at that date:
--Bruce:
SELECT name FROM people
JOIN phone_calls ON phone_calls.receiver = people.phone_number
WHERE duration < 60 AND year = 2021 AND month = 7 AND day = 28 AND caller =
(SELECT phone_number FROM people
WHERE name = 'Bruce');
-- Robin

-- Diana:
SELECT name FROM people
JOIN phone_calls ON phone_calls.receiver = people.phone_number
WHERE duration < 60 AND year = 2021 AND month = 7 AND day = 28 AND caller =
(SELECT phone_number FROM people
WHERE name = 'Diana');
-- Philip

-- Lets look at earliest flights and the names that were on that flight:
SELECT people.name, flights.hour, flights.minute
FROM people
JOIN passengers ON passengers.passport_number = people.passport_number
JOIN flights ON flights.id = passengers.flight_id
JOIN airports ON flights.origin_airport_id = airports.id
WHERE city = 'Fiftyville' AND year = 2021 AND month = 7 AND day = 29
ORDER BY hour;
-- Same name as above:
-- Bruce 08:20

-- The city the thief escaped to:
SELECT city FROM airports
JOIN flights ON flights.destination_airport_id = airports.id
JOIN passengers ON flights.id = passengers.flight_id
JOIN people ON passengers.passport_number = people.passport_number
WHERE name = 'Bruce';
-- New York City


