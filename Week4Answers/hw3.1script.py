cars = 100
drivers = 30
passengers = 85

leftcars = cars - drivers
usedcars = drivers
totaltransport = drivers + passengers
averagepass = totaltransport / usedcars

print(leftcars, 'cars will not be used on this day.')
print(usedcars, 'cars will be used on this day.')
print(totaltransport, 'total people will be transported on this day.')
print('The average passenger per car is ', averagepass)

