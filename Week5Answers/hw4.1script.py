filename='aravg.ann.land_ocean.90S.90N.v4.0.1.201612.asc'
year = []
temperature = []

with open(filename, "r") as f:
    alist = f.read().splitlines()
for line in alist:
    year.append(int(line.split()[0]))
    temperature.append(float(line.split()[1]))

wxdata = list(zip(year,temperature))
wxdata.sort(reverse=True)

print('Ranking	'+'Year	'+'Temperature Anomaly (degrees C)	'\
+'Temperature Anomaly (degrees F)')
