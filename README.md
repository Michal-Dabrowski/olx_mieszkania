# OLX Mieszkania

OLX Mieszkania to prosty program pomagający w szukaniu mieszkań do wynajęcia. Zrobiony był na potrzeby szybkiej reakcji na nowe ogłoszenia, co czasem jest decydującym czynnikiem;)

## Konfiguracja

W pliku config.py należy skonfigurować cenę maksymalną poszukiwanego mieszkania, miasto oraz dane dotyczące naszego konta pocztowego, z którego program będzie rozsyłał wiadomości email. Najlepiej jakby program działał 24/7 np. na Raspberry Pi. W tym celu należy dodać nowe zadanie cron (jeśli korzystamy z systemu Linux). W terminalu wpisujemy:  
'crontab -e'  
Oraz dodajemy na końcu:  
'*/15 * * * * python3 pełna/ścieżka/do/run.py'
W tej opcji program będzie uruchamiał się co 15 minut każdego dnia.

## Jak działa?

Program wchodzi na stronę www.olx.pl/nieruchomosci/mieszkania/ wybranego miasta oraz zapisuje wszystkie oferty do bazy danych. Następnie wybiera z bazy danych wszystkie oferty z ceną równą bądź mniejszą wybranej ceny maksymalnej, tworzy z nich treść maila oraz oznacza je jako archiwalne (aby nie dublować ogłoszeń).
