filename='aravg.ann.land_ocean.90S.90N.v4.0.1.201612.asc'
wxdata={'year':[],'temperature':[]}
with open(filename, "r") as f: 
    alist = f.read().splitlines()
for line in alist: #iterate through lines
    wxdata['year'].append(int(line.split()[0]))
    wxdata['temperature'].append(float(line.split()[1]))

print('Ranking      '+'Year     '+'Temperature Anomaly (degrees C)     '\
+'Temperature Anomaly (degrees F)')

highesttemps = [i for i in wxdata['temperature'] if i >= .3]
highesttemps.sort(reverse = True)

# convert temp anomaly into F

for i in range (0,10):
    rank = i + 1
    tempF = highesttemps[i] * 1.8 + 32
    print('{0:<12d} {1:<8d} {2:<35f} {3:<10f} '.format(rank,\
    wxdata['year'][wxdata['temperature'].index(highesttemps[i])]\
    ,highesttemps[i], tempF))
