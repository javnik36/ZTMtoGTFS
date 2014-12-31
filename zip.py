import zipfile

files = ["agency.txt", "calendar.txt", "feed_info.txt", "routes.txt", "stop_times.txt", "stops.txt", "trips.txt"]
zf = zipfile.ZipFile("gtfs.zip", 'w')

for file in files:
    zf.write(file)

zf.close()
