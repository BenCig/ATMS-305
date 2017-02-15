#do a couple diff  lists or do a dictionary?
# then count(-SN), count(SN), count(+SN)
# 2. divide that by total number
# 3. find the high
# 4. oh fun...

filename='CMI.csv'
wxdata={'obs':[], 'temperature':[]}

with open (filename, "r") as f:
    first_line = f.readline()
    alist = f.read().splitlines()
for line in alist:
     wxdata['temperature'].append(line.split(',')[2])
     wxdata['obs'].append(line.split(',')[10])

# count up all types of snow (done like this bc count('SN') gave incorrect
lightsnow = int(wxdata['obs'].count('-SN'))
brlsnow = int(wxdata['obs'].count('-SN BR'))
bllsnow = int(wxdata['obs'].count('-SN BLSN'))
frzlsnow = int(wxdata['obs'].count('-SN FZFG'))
blsnow = int(wxdata['obs'].count('SN BLSN'))
fgsnow = int(wxdata['obs'].count('SN FG'))
fzsnow = int(wxdata['obs'].count('SN FZFG'))
brsnow = int(wxdata['obs'].count('SN BR'))
heavysnow = int(wxdata['obs'].count('+SN FG'))
totalsnow = lightsnow + brlsnow + bllsnow + frzlsnow + blsnow + fgsnow +\
    fzsnow + brsnow + heavysnow

totalobs = (len(wxdata['obs']))
print(totalobs)

# total snow for # of snow obs
# total snow / total obs for fraction of reports


