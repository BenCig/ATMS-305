filename='CMI.csv'
day = []
obs = []
temp = []
with open (filename, "r") as f:
    first_line = f.readline()
    alist = f.read().splitlines()
for line in alist:
    obs.append(line.split(',')[10])
    day.append(line.split(',')[1])
    temp.append(line.split(',')[2])

day.remove('2016-12-20 11:53')
day.remove('2016-05-01 00:00')
temp.remove('M')
temp.remove('M')

floattemp = [float(i) for i in temp]
tempsum = sum(floattemp)
average = tempsum / (len(day))

wxdata = dict(zip(floattemp[:],day[:]))

hightemp = [i for i in wxdata if i >= 90]
hightemp.sort(reverse = True)

# count up all types of snow (done like this bc count('SN') gave incorrect
lightsnow = int(obs.count('-SN'))
brlsnow = int(obs.count('-SN BR'))
bllsnow = int(obs.count('-SN BLSN'))
frzlsnow = int(obs.count('-SN FZFG'))
blsnow = int(obs.count('SN BLSN'))
fgsnow = int(obs.count('SN FG'))
fzsnow = int(obs.count('SN FZFG'))
brsnow = int(obs.count('SN BR'))
heavysnow = int(obs.count('+SN FG'))
totalsnow = lightsnow + brlsnow + bllsnow + frzlsnow + blsnow + fgsnow + fzsnow+\
    brsnow + heavysnow

totalobs = (len(obs))
snowfrac = float(totalsnow/totalobs)

print("1. There were",totalsnow,"snow reports last year.")
print("2. The fraction of reports with snow was:", snowfrac)
print("3. The highest temperature of", hightemp[0], "occured at"\
    ,wxdata[hightemp[0]])
print("4. The mean temperature of all reports was:", \
    average, "degrees Fahrenheit.")
