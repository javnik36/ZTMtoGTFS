def make_calendar(start_date, end_date):
  '''Tworzy calendar.txt dla zestawu danych gtfs.
  start_date i end_date w formacie RRRRMMDD'''
  import re

  save = open("calendar.txt", 'w', encoding="utf-8")


  #start_date = 20140918
  #end_date = 20140918
  koma = ','

  save.write("service_id,monday,tuesday,wednesday,thursday,friday,saturday,sunday,start_date,end_date" + '\n' )
  calendar_dict = { "D1" : [1,0,0,0,0,0,0,start_date,end_date],
                    "D2" : [0,1,0,0,0,0,0,start_date,end_date],
                    "D3" : [0,0,1,0,0,0,0,start_date,end_date],
                    "D4" : [0,0,0,1,0,0,0,start_date,end_date],
                    "D5" : [0,0,0,0,1,0,0,start_date,end_date],
                    "D6" : [0,0,0,0,0,1,0,start_date,end_date],
                    "D7" : [0,0,0,0,0,0,1,start_date,end_date],
                    "DP" : [1,1,1,1,1,0,0,start_date,end_date],
                    "DS" : [0,0,0,0,0,0,1,start_date,end_date],
                    "SB" : [0,0,0,0,0,1,0,start_date,end_date],
                    "N1" : [1,0,0,0,0,0,0,start_date,end_date],
                    "N2" : [0,1,0,0,0,0,0,start_date,end_date],
                    "N3" : [0,0,1,0,0,0,0,start_date,end_date],
                    "N4" : [0,0,0,1,0,0,0,start_date,end_date],
                    "N5" : [0,0,0,0,1,0,0,start_date,end_date],
                    "N6" : [0,0,0,0,0,1,0,start_date,end_date],
                    "N7" : [0,0,0,0,0,0,1,start_date,end_date],
                    "NS" : [1,1,1,1,1,0,0,start_date,end_date],
                    "NP" : [0,0,0,0,0,1,1,start_date,end_date],
                    "NO" : [1,1,1,1,1,1,1,start_date,end_date],
                    "TS" : [1,1,1,1,1,1,1,start_date,end_date] }


  for key, value in calendar_dict.items():
    strCal = ""
    for item in value:
      strCal += str(item) + koma
      
    save.write(key + koma + strCal[:-1] + '\n')


  save.close()
  print("już...")

