ZTMtoGTFS
============
Krótki opis
-------------
Program z plików rozkładowych dostępnych na stronach ZTM Warszawa i danych przystankowych OpenStreetMap tworzy [plik gtfs.](https://developers.google.com/transit/gtfs/reference)

"Szybki" start
-------------
#####Wymagania programu
Do uruchomienia najnowszej wersji programu potrzebujesz:
    *Pythona3,<br>
    *programu 7-Zip (zainstalowanego w *C:\Program Files\7-Zip\*,<br>
    *i....mniej niż 2 minut czasu wolnego ;)<br>

#####Instrukcja uruchomienia
1. Uruchom plik [gtfs_main.py](https://github.com/javnik36/ZTMtoGTFS/blob/master/gtfs_main.py) i czekaj na koniec wykonywania programu.<br>
#####UWAGA!
Program w wersji 0.3 jest stworzony do pracy na windowsie! Jeśli nie pracujesz na windowsie lub nie spełniasz wymagań, użyj instrukcji poniżej.<br>
Generalnie program robi wszystko automatycznie to co jest poniżej, jednak ma wpisane na sztywno ścieżki do niektórych plików, więc jak czujesz się na siłach to możesz poedytować sobię pliki lokalnie ;)


1. Pobierz ze [strony ZTMu](ftp://rozklady.ztm.waw.pl/) plik z danymi i rozpakuj go do folderu z plikami programu.<br>
2. Uruchom funkcję stops() z pliku stops_from_osm.py<br>
3. Uruchom funkcję make() z pliku route_parser.py<br>
4. Dodatkowo uruchom funkcję make_calendar z pliku calendar.py oraz funkcję create_agency() i create_feedinfo() z agency.py<br>
5. Jak chcesz ładnego zipa uruchom funkcję zip() z zip.py<br>
6. Gotowe! Masz gtfs z danymi z ZTMu i OSM!<br>

~~Sorka za problemy, będzie prościej, ale muszę to razem wszystko połączyć.~~

Błędy OSM
-------------
Uruchom skrypt bugs_checker_osm.py.<br>
W pliku BUGS-NOT-IN-OSM.txt dostaniesz nr-y przystankow których nie ma w OSM.


Licencja:
-------------
[Copyright (c) 2014-2015 javnik36](https://github.com/javnik36/ZTMtoGTFS/blob/master/licence.md)
