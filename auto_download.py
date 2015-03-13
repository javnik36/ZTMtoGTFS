import datetime
import urllib.request as urllib
#import socket
import os

#socket.setdefaulttimeout(120)

now = datetime.datetime.now()
now_str = now.strftime("%y%m%d")

url = "ftp://rozklady.ztm.waw.pl/RA"
path = "ztm_pack.7z"
ziper = ".7z"

i = False
s = 0
while i == False:
    try:
        if s == 0:
            go = url + now_str + ziper
        else:
            now_int = int(now_str) - s
            go = url + str(now_int) + ziper
        s += 1
        print(str(s) + "   :   " + go)
        urllib.urlretrieve(go, path)
        i = True
    except Exception as e:
        print(str(e))
        continue

os.chdir("C:\Program Files\/")
os.chdir("7-Zip")
os.system("7z e -oE:\Git\GTFS E:\Git\GTFS\ztm_pack.7z")
