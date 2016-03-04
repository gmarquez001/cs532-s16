import requests
import json

Friendname = []
Friendnumber = []
i = 0
mean = 0
median = 0
stddev = 0
total = 0
lastline = ' '

for line in open('Parsedtwitter.txt','r'):
    a = line
    b = a.find(' ')
    c = line[b:]
    #c = c[:-1]
    #print c

    #d = str(c)
    #e = d[:-1]
    # print e
    i = i + int(c)
    print line
    #print i
    Friendname.append(a[:-1])
    Friendnumber.append(int(c))

    
total = sum(Friendnumber)
print 'Total: ' + str(total)

mean = total/len(Friendnumber)
print'Mean: ' + str(mean)

SortedFriendnumber = Friendnumber
sorts = sorted(SortedFriendnumber)
length = len(sorts)
if not length % 2:
       median = (sorts[length / 2] + sorts[length / 2 - 1]) / 2.0
median = sorts[length / 2]
print 'Median: ' +  str(median)

ss = sum((x-mean)**2 for x in Friendnumber)

pvar = ss/i # the population variance
stddev = pvar**0.5

print 'Standard Deviation: ' +  str(stddev)
a = 0
b = 0
while a < 181:
    print Friendname[a] 
    a = a + 1
while b < 181:    
    print str(Friendnumber[b]) 
    b = b + 1

