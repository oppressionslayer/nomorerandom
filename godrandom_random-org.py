# Created for Arpan to read files
#!/usr/bin/python
import random
from collections import Counter

with open('random-org.txt', 'r') as myfile:
    global PI
    PI=myfile.read().replace('\n', '')

lowDefault = 1
highDefault = 10

# debug = 'TRUE' # or 'FALSE'
debug = 'FALSE'

def wrap(numberToBeWrapped, start=lowDefault, limit=highDefault, origin=1):
  if start == 0:
     boundX = start + (numberToBeWrapped - start ) % (limit + 1 - start)  
  else:
     boundX = start + (numberToBeWrapped - start ) % (limit + 1 - start) 
     if numberToBeWrapped < start:
       if numberToBeWrapped == 0 and boundX == limit:
          boundX = limit
       else:
          if abs(numberToBeWrapped) >= limit:
               next
          else:
               boundX = start + (numberToBeWrapped - start ) % (limit + 1 - start) 
     if numberToBeWrapped < start and abs(numberToBeWrapped) == limit:
         boundX = limit
  return boundX, min(abs(numberToBeWrapped-origin), abs(boundX-origin), start + (numberToBeWrapped - origin - start) % (limit + 1 - start), start + (boundX - origin - start) % (limit + 1 - start), start + (origin - boundX - start) % (limit + 1 - start))

def randDistance(previous, current, low, high, x):
  newResult = int(PI[int(x)]) #random.randint(low,high)
  _ , distfromPrevious = wrap(previous-current, low, high, newResult)
  _ , distfromCurrent = wrap(current-previous, low, high, newResult)
  _ , distbyPreviousCurrent = wrap(current+previous, low, high, newResult)
  newDistance = min(distfromPrevious, distfromCurrent, distbyPreviousCurrent)
  return previous, current, newResult, newDistance


closeness = []

beforeprevious, previous, current, newdistance = randDistance(int(PI[0]),int(PI[1]), lowDefault,highDefault, 2)
closeness.append(newdistance)
beforeprevious, previous, current, newdistance = randDistance(int(PI[1]), int(PI[2]), lowDefault,highDefault, 3)
#closeness.append(newdistance)

for x in range (4, 10000):
   closeness.append(newdistance)
   beforeprevious, previous, current, newdistance =  randDistance(previous,current, lowDefault, highDefault, int(x))
   if debug == 'TRUE':
       print ( 'previous: ', beforeprevious, 'current: ', previous, 'newCard: ', current, 'distance: ', newdistance, x)

a = dict()
a = dict(Counter(closeness))
print(a)
