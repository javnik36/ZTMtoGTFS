from agency import *
from auto_download import *
from calendar import *
from route_parser import *
from stops_from_osm import *
from zip import *
import time

time.clock()
liner = "_____________________________________________________________"
print("WITAJ w programie do tworzenia pliku gtfs z danych ZTM Warszawa i OSM!")
print(liner)
print("Przystępuje do działania!")
print("Pobieram dane ZTMu...")
download_now()
print(liner)
print("Wypakowuję...")
dane_ztm = unzip_download()
print(liner)
print("Przetwarzam na gtfs...")
make(dane_ztm)
print(liner)
print("Pobieram przystanki z OSM...")
stops()
print(liner)
print("Tworzę kalendarz...")
make_calendar(20000101,20200202)
print(liner)
print("Tworzę pliki pomocnicze...")
create_agency()
create_feedinfo()
print(liner)
print("Pakuję pliki...")
zip()
print(liner)
print("Kończę działanie programu...;)")
print(liner)
print(liner)
print(liner)
print("Czas działania programu gtfs_main: " + str(time.clock()/60) + " minut")
