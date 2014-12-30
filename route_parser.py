import re
import time

time.clock()

file = open("RA141219.txt", 'r', encoding="utf-8")
save_route = open("routes.txt", 'w', encoding="utf-8")
save_trips = open("trips.txt", 'w', encoding="utf-8")
save_times = open("stop_times.txt", 'w', encoding="utf-8")
route_header = "route_id,agency_id,route_short_name,route_long_name,route_desc,route_type,route_url,route_color,route_text_color"
trips_header = "route_id,service_id,trip_id,trip_headsign,trip_short_name,direction_id,block_id,shape_id,wheelchair_accessible,bikes_allowed"
times_header = "trip_id,arrival_time,departure_time,stop_id,stop_sequence,stop_headsign,pickup_type,drop_off_type,shape_dist_traveled"
#DATA EXAMPLE
#RUTE-ID,,NR-LiNII,,,TYPE,URL,,
#RUTE-ID,SERVICE-ID,TRIP-ID,DOKĄD,,,,,,
#TRIP-ID,PRZYJAZD(HH:MM:SS),ODJAZD,STOP-ID,SEKWENCJA,,NŻ?,NŻ?,


save_route.write(route_header + "\n")
save_trips.write(trips_header + "\n")
save_times.write(times_header + "\n")

route_id = ""
nr_linii = ""
route_type = ""

temp = []

inLL = False
inTR = False
inLW = False
inRP = False
inTD = False
inWG = False
inOD = False
inOP = False
inWK = False

iterator = 0

for line in file:
  line = line.rstrip().lstrip()

  starter = re.compile("\*LL\s\d+")
  start = starter.match(line)

  ender = re.compile("\#LL")
  end = ender.match(line)

  sWKer = re.compile("\*WK\s+\d+")
  sWK = sWKer.match(line)

  eWKer = re.compile("\*WK")
  eWK = eWKer.match(line)


  koma = ','


  if start != None:
    inLL = True
  elif end != None:
    inLL = False
    break
  elif sWK != None:
    inWK = True
    temp.clear()
    iterator = 0
  elif eWK != None:
    inWK = False
    temp.clear()
    iterator = 0
  elif inLL == True:
    iterator += 1
    #MATCHING ROUTE
    linier = re.compile("\w{5}\:\s(.+)\-.+")
    linia = linier.match(line)

    if linia != None:
      nr_linii = linia.group(1).rstrip().lstrip()
      if (nr_linii.isnumeric() and len(nr_linii) < 3) or nr_linii == 'T':
        route_type = "0"
      elif nr_linii.isnumeric() and len(nr_linii) == 3:
        route_type = "3"
      elif nr_linii.startswith("E") or nr_linii.startswith("L") or nr_linii.startswith("N") or nr_linii.startswith("Z"):
        route_type = "3"
      elif nr_linii.startswith("KM") or nr_linii.startswith("S") or nr_linii == "WKD":
        route_type = "2"
      else:
        #raise ValueError
        print("Nie rozpoznałem linii nr: " + nr_linii)

      #RUTE-ID,,NR-LiNII,,,TYPE,URL,,
      route_id = nr_linii
      url = "http://www.ztm.waw.pl/rozklad_nowy.php?c=182&l=1&q=" + nr_linii
      save_route.write(route_id + koma*2 + nr_linii + koma*3 + route_type + koma + url + koma*2 + '\n')

    if inWK == True:
      tekst_sam = re.compile("(.{17})\s+(\d{6})\s(\w{2})\s+(\d+\.\d+)")
      tekst_zP = re.compile("(.{17})\s+(\d{6})\s(\w{2})\s+(\d+\.\d+)\s+\P")
      macz_sam = tekst_sam.match(line)
      macz_zP = tekst_zP.match(line)

      #RUTE-ID,SERVICE-ID,TRIP-ID,xDOKĄDx,,,,,,

      if macz_sam != None:
        service_id = macz_sam.group(3)
        trip_id = macz_sam.group(1)

        print_trip_id = nr_linii + '/' + trip_id

        #TRIP-ID,PRZYJAZD(HH:MM:SS),ODJAZD,STOP-ID,SEKWENCJA,,xNŻx,xNŻx,


        arr_temp = macz_sam.group(4).split('.')
        arrival = arr_temp[0] + ":" + arr_temp[1] + ":00"
        departure = arrival
        stop = macz_sam.group(2)

        save_times.write(print_trip_id + koma + arrival + koma + departure + koma + stop + koma + str(iterator) + koma*4 + '\n')


        if trip_id in temp:
          continue
        elif trip_id not in temp:
          temp.append(trip_id)
          save_trips.write(route_id + koma + service_id + koma + print_trip_id + koma*7 + '\n')

      elif macz_zP != None:
        service_id = macz_zP.group(3)
        trip_id = macz_zP.group(1)

        print_trip_id = nr_linii + '/' + trip_id


        arr_temp = macz_zP.group(4).split('.')
        arrival = arr_temp[0] + ":" + arr_temp[1] + ":00"
        #departure = arrival
        stop = macz_zP.group(2)

        save_times.write(print_trip_id + koma + arrival + koma*2 + stop + koma + str(iterator) + koma*4 + '\n')


        if trip_id in temp:
          continue
        elif trip_id not in temp:
          temp.append(trip_id)
          save_trips.write(route_id + koma + service_id + koma + print_trip_id + koma*7 + '\n')

      else:
        continue



  else:
    continue

file.close()
save_route.close()
save_trips.close()
print("juz...")
print("Czas działania: " + str(time.clock()/60) + " minut")
