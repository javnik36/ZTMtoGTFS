def download_now():
    import datetime
    import urllib.request as urllib

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


def unzip_download(save_path=None):
    import os

    dir_1 = os.listdir()
    cwdir = os.getcwd()
    file_path = cwdir + "\ztm_pack.7z"

    if save_path == None:
        save_path = cwdir

    os.chdir("C:\Program Files\/")
    os.chdir("7-Zip")
    os.system("7z e -o" + save_path + " " + file_path)
    os.chdir(cwdir)

    dir_2 = os.listdir()
    if len(dir_2) != len(dir_1):
        for el in dir_2:
            if el not in dir_1:
                return el
