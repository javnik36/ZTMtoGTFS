def stops():
    import urllib.request as urllib
    import json

    url = "http://overpass-api.de/api/interpreter?data=%5Bout%3Ajson%5D%3B%28node%5B%22public%5Ftransport%22%3D%22stop%5Fposition%22%5D%5B%22network%22%3D%22ZTM%20Warszawa%22%5D%2851%2E8355%2C20%2E3782%2C52%2E6006%2C21%2E6706%29%3B%29%3Bout%20body%3B%3E%3Bout%20skel%20qt%3B"
    path = 'osm_data.json'
    urllib.urlretrieve(url, path)

    plik = open(path, 'r', encoding="utf-8")
    save = open("stops.txt", 'w', encoding="utf-8")
    data = plik.read()
    plik.close()

    header = "stop_id,stop_code,stop_name,stop_desc,stop_lat,stop_lon,zone_id,stop_url,location_type,parent_station,stop_timezone,wheelchair_boarding"
    save.write(header + '\n')
    koma = ','

    decoded = json.loads(data)

    dane = decoded["elements"]

    for block in dane:
        try:
            lat = str(block["lat"])
            lon = str(block["lon"])
            tagi = block["tags"]

            stop_name = tagi["name"]
            stop_id = tagi["ref"]
            link = "http://www.ztm.waw.pl/rozklad_nowy.php?c=182&l=1&n=" + \
                stop_id[:4] + "&o=" + stop_id[-2:]

            save.write(stop_id + koma * 2 + stop_name + koma * 2 +
                       lat + koma + lon + koma * 2 + link + koma * 4 + '\n')
        except:
            print("BŁONT")
            print(block)

    save.close()
