import re

osm = open("stops.txt", 'r', encoding="utf-8")
bugs = open("BAD-STOPS.txt", 'r', encoding="utf-8")
still = open("BUGS-NOT-IN-OSM.txt", 'w')

bugi = []

for line in bugs:
    line = line.split(' ')
    bugi.append(line[0])
print(len(bugi))
for line in osm:
    line = line.split(',')
    if line[0].isnumeric():
        stop_nr = line[0]
        if stop_nr in bugi:
            bugi.remove(stop_nr)
            
for item in bugi:
    still.write(item)
    still.write("\n")

osm.close()
bugs.close()
still.close()
    
print(len(bugi))

