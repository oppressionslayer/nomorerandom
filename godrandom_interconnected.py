#!/usr/bin/python
#
# Randomness has a structure, more proof for you statistic and data heads
# Randomness has a structure, numbers are interconnected by distance from previous
# numbers. We know that based on a previous result, that the next card a Random
# number generator picks, will be 1 Away 33% of the time, 2 Away, 22% of the time,
# 0 Away, 21% of the time, etc, etc.
#
# Using max of 13 simulates a deck of Cards.
# Remember, this is a wrapped set of numbers. if min/max is 1,13 and your cards are:
# ('previous: ', 8, 'current: ', 8, 'newCard: ', 3, 'distance: ', 0)
# from two previous cards of 8,8, and the new card is 3, then 8 + 8 is 3, because:
# Adding 8 from 8, so start at and count up 8: 9, 10, 11, 12, 13, 1, 2, 3
# 
# The following calculates a distance from two previous numbers of a Randomly Generated
# number. We can see that the results are not completely random but rather, structured,
# by distance from the sum or difference of the two previous numbers. 
#
# An example:
# ('previous: ', 1, 'current: ', 4, 'newCard: ', 5, 'distance: ', 0)
# If these were Cards, that would be Ace and 4. The new card is a 5. 
# Ace + 4 = 5, so the distance is 0
# We also calculated for Ace - 4, and 4 - Ace, and wrapped the deck each time. We only
# keep the result with the lowest distance.
# You can see from debugging, which cards are most likely to be 0 Away, 1 Away, etc.
# The results are profound, not only can you make better card predictions, you also find
# that randomness is not completly disordered, but rather structured by distance!!!!
# 
# Randomness is an illusion, All RNG's, even TRUE Random, will follow this structure.
#  
# You can modify this program so that the previous and current are always the same 2 numbers
# to see that the results still follow this structure.
#
# {0: 2603532, 1: 4042750, 2: 2709888, 3: 1643734, 4: 844314, 5: 311491, 6: 44286}
# 
# python random.randint(min, max) results
# 0-6 Away Total: 12,199,995
# 0 Away:  21.34%
# 1 Away:  33.14 %
# 2 Away :  22.21 %
# 3 Away:  13.47 %
# 4 Away:  6.92 %
# 5 Away:  2.55 %
# 6 Away:  3.63 %
# 
# quantumrandom statistics:
# {0: 225, 1: 346, 2: 255, 3: 117, 4: 43, 5: 14, 6: 1}
# Only 1 1K Data Set, this is due to quantumrandom.randint(min,max) being time consuming
# 0-6 Away Total: 1,000
# 0 Away: 22.5 %
# 1 Away: 34.6 %
# 2 Away: 25.5 %
# 3 Away: 11.7 %
# 4 Away: 4.3 %
# 5 Away: 1.4 %
# 6 Away: 1 %
#

import random
from collections import Counter

lowDefault = 1
highDefault = 13

# debug = 'TRUE' or 'FALSE'
debug = 'FALSE'

def wrap(numberToBeWrapped, start=1, limit=13, origin=1):
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

def randDistance(previous, current, low, high):
  newResult = random.randint(low,high)
  _ , distfromPrevious = wrap(previous-current, low, high, newResult)
  _ , distfromCurrent = wrap(current-previous, low, high, newResult)
  _ , distbyPreviousCurrent = wrap(current+previous, low, high, newResult)
  newDistance = min(distfromPrevious, distfromCurrent, distbyPreviousCurrent)
  return previous, current, newResult, newDistance


closeness = []

beforeprevious, previous, current, newdistance = randDistance(5,8, lowDefault,highDefault)
closeness.append(newdistance)
beforeprevious, previous, current, newdistance = randDistance(8,current, lowDefault,highDefault)
closeness.append(newdistance)

for x in range (1, 300000):
   closeness.append(newdistance)
   beforeprevious, previous, current, newdistance =  randDistance(previous,current, lowDefault, highDefault)
   if debug == 'TRUE':
       print ( 'previous: ', beforeprevious, 'current: ', previous, 'newCard: ', current, 'distance: ', newdistance)
   #if newdistance == 5:
   #   print ( 'previous: ', beforeprevious, 'current: ', previous, 'newCard: ', current, 'distance: ', newdistance)
   #if newdistance == 6:
   #   print ( 'previous: ', beforeprevious, 'current: ', previous, 'newCard: ', current, 'distance: ', newdistance)

a = dict()
a = dict(Counter(closeness))
print(a)
