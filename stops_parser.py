import re

file = open("RA141219.txt", 'r', encoding="utf-8")
save = open("stops_ztm.txt", 'w', encoding="utf-8")
fehler = open("BAD-STOPS.txt", 'w', encoding="utf-8")
header = "stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station,stop_timezone,wheelchair_boarding"
#DATA EXAMPLE
#ID,,NAME,,LAT,LON,ZONE,URL,,,,

save.write(header + "\n")

zone = 1
stop_name = ""

inZP = False
inPR = False
for line in file:
  line = line.rstrip().lstrip()

  starter = re.compile("\*ZP\s\d+")
  start = starter.match(line)

  ssekcjoner = re.compile("\*PR")
  ssekcja = ssekcjoner.match(line)

  esekcjoner = re.compile("\#PR")
  esekcja = esekcjoner.match(line)

  ender = re.compile("\#ZP")
  end = ender.match(line)



  if start != None:
    inZP = True
  elif ssekcja != None:
    inPR = True
  elif esekcja != None:
    inPR = False
  elif end != None:
    inZP = False
    break
  elif inZP == True:
    #placer = re.compile("\d{4}\s{3}(.+)\,\s+(.{2})\s{2}.+")
    placer = re.compile("\d{4}\s{3}(.+)\,\s+(.{2})\s{2}.+")
    long_placer = re.compile("\d{4}\s{3}(.+)\s+(.{2})\s{2}.+")
    place = placer.match(line)
    l_place = long_placer.match(line)

    if place != None:
      stop_name = place.group(1)
      if place.group(2) == '--':
        zone = 1
      else:
        zone = 2
    elif l_place != None:
      stop_name = l_place.group(1).rstrip()
      if l_place.group(2) == '--':
        zone = 1
      else:
        zone = 2


    if inPR == True:
      datas = re.compile("(\d{4})(\d{2}).+\Y=\s(\d{2}\.\d{6})\s+\X=\s(\d{2}\.\d{6})")
      bad_datas = re.compile("(\d{4})(\d{2}).+\Y=(\w{3}\.\w{8})\s+\X=(\w{3}\.\w{8})")
      m_data = datas.match(line)
      m_b_data = bad_datas.match(line)

      if m_data != None:
        stop_id = m_data.group(1) + m_data.group(2)
        name_str = stop_name + ' ' + m_data.group(2)
        lat = m_data.group(3)
        lon = m_data.group(4)
        url = "http://www.ztm.waw.pl/rozklad_nowy.php?c=182&l=1&n=" + m_data.group(1) + "&o=" + m_data.group(2)
        koma = ','
        #ID,,NAME,,LAT,LON,ZONE,URL,,,,

        save.write(stop_id + koma*2 + name_str + koma*2 + lat + koma + lon + koma + str(zone) + koma + url + koma*4 + '\n')
      elif m_b_data != None:
        stop_id = m_b_data.group(1) + m_b_data.group(2)
        name_str = stop_name + ' ' + m_b_data.group(2)
        fehler.write(stop_id + ' >> ' + name_str + '\n')

    



  else:
    print("?")
    #print(line)

file.close()
save.close()
fehler.close()
print("juz...")
