import datetime

start_clock = datetime.datetime.utcnow()

alist = [3, 2, 1] * 10000
newlist_lc = [alist[i] + i * 2 for i in range(5)]

end_clock = datetime.datetime.utcnow()
print('For loop took {0:12s}'.format(end_clock - start_clock))



