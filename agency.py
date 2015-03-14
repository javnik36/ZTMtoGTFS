def create_agency():
  file = open("agency.txt", 'w', encoding='utf-8')
  header = "agency_id,agency_name,agency_url,agency_timezone,agency_lang,agency_phone,agency_fare_url"
  file.write(header)
  file.write('\n')
  file.write(",Zarząd Tansportu Miejskiego w Warszawie,http://www.ztm.waw.pl,Europe/Warsaw,pl,19115,http://www.ztm.waw.pl/?c=110&l=1")
  file.close()
  print("Stworzono plik agency.txt")

def create_feedinfo():
  file = open("feed_info.txt", 'w', encoding='utf-8')
  header = "feed_publisher_name,feed_publisher_url,feed_lang,feed_start_date,feed_end_date,feed_version"
  file.write(header)
  file.write('\n')
  file.write("Javnik,https://github.com/javnik36/ZTMtoGTFS,pl,,,0.3")
  file.close()
  print("Stworzono plik feed_info.txt")
