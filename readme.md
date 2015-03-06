ZTMtoGTFS
-------------

"Szybki" start
-------------
Do uruchomienia potrzebujesz Pythona3.
1. Pobierz ze [strony ZTMu](ftp://rozklady.ztm.waw.pl/) plik z danymi i rozpakuj go do folderu z plikami programu.<br>
2. Uruchom stops_from_osm.py<br>
3. Uruchom route_parser.py (najpierw podmień zmienną file, żeby nazwa zgadzała się z pobranym plikiem z ztmu)<br>
4. Dodatkowo uruchom funkcję make_calendar z pliku calendar.py oraz funkcję create_agency() i create_feedinfo() z agency.py<br>
5. Jak chcesz ładnego zipa uruchom funkcję zip() z zip.py<br>
6. Gotowe! Masz gtfs z danymi z ZTMu i OSM!<br>

Sorka za problemy, będzie prościej, ale muszę to razem wszystko połączyć.

Błędy OSM
-------------
Uruchom skrypt bugs_checker_osm.py.<br>
W pliku BUGS-NOT-IN-OSM.txt dostaniesz nr-y przystankow których nie ma w OSM.


Licencja:
-------------
[Copyright (c) 2014-2015 javnik36](https://github.com/javnik36/ZTMtoGTFS/blob/master/licence)
