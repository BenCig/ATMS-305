filename='aravg.ann.land_ocean.90S.90N.v4.0.1.201612.asc'
wxdata={'year':[],'temperature':[]}
with open(filename, "r") as f: #read all the lines in the file
    alist = f.read().splitlines()
for line in alist: #iterate through lines
    wxdata['year'].append(int(line.split()[0]))
    wxdata['temperature'].append(float(line.split()[1]))

print('Ranking	'+'Year	'+'Temperature Anomaly (degrees C)	'\
+'Temperature Anomaly (degrees F)')

# try two lists, zip them, sort, shove into dictionary???

