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
for line in open('friends.txt','r'):
    a = ' '
    b = ' '
    #if '</node>'


    #Get all friend information
    if '<node id="' in line:
        a = line[10:-3]
        Friendname.append(a)
        #print 'Name: ' + b
        
    if '<data key="friend_count">' in line and '<data key="mutual_friend_count"' in lastline:
        b = line[35:-11]
        b = int(b)
        Friendnumber.append(b)
        #print 'Number of Friends: ' + b
        print 'Name: ' + Friendname[i]
        print 'Number of Friends: ' + str(Friendnumber[i])
        i = i + 1
        print 'Counter: ' + str(i)
        print '\n'
    if '</node>' in line and '<data key="mutual_friend_count"' in lastline:
        b = 0
        Friendnumber.append(b)
        print 'Name: ' + Friendname[i]
        print 'Number of Friends: ' + str(Friendnumber[i])
        i = i + 1
        print 'Counter: ' + str(i)
        print '\n'
    lastline = line

#
total = sum(Friendnumber)
print 'Total: ' + str(total)

mean = total/i
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
while a < 165:
    print Friendname[a]
    a = a + 1
while b < 165:    
    print str(Friendnumber[b])
    b = b + 1
    











