def zip(path="/"):
    '''(path="/")-->gtfs.zip
    Zipuje wszystkie pliki potrzebne do gtfs'a.
    '''
    import zipfile
    import zlib
    import os.path as sys

    files = ["agency.txt", "calendar.txt", "feed_info.txt", "routes.txt", "stop_times.txt", "stops.txt", "trips.txt"]
    zf = zipfile.ZipFile("gtfs.zip", 'w', compression=zipfile.ZIP_DEFLATED)

    for file in files:
        if sys.isfile(file):
            zf.write(file)
        else:
            print("Brakuje pliku " + file + " w zipie gtfs!")

    zf.close()

