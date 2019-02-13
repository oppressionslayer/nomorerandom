#!/usr/bin/python
#
# Randomness has a structure, more proof for you statistic and data heads
# Randomness has a structure, numbers are interconnected by distance from previous
# numbers. We know that based on a previous result, that the next card a Random
# {0: 4614594, 1: 9231939, 2: 9229865, 3: 4616544, 4: 2307059}
# number generator picks, will be 1 Away 30% of the time, 2 Away, 30% of the time,
# 0 Away, 15% of the time, etc, etc.
#
# Using max of 13 simulates a deck of Cards.
# Remember, this is a wrapped set of numbers. if min/max is 1,13 and your cards are:
# ('previous: ', 9, 'new number: ', 13, 'Guess #1: ', 5, 'Guess #2: ', 13, 'distance from Guesses: ', 0)
# from the previous card, it add and subtracts 4, to give you Guess 5 and 13. Now the new number is 
# generated, and it is 13. 13 is 0 away from Guess #2, so that is the result. Our Guess is exactly the
# new RNG generated number.
# 
# The following calculates a distance from two previous numbers of a Randomly Generated
# number. We can see that the results are not completely random but rather, structured,
# by distance from the sum or difference of the two previous numbers. 
#
# An example:
# ('previous: ', 5, 'new number: ', 8, 'Guess #1: ', 1, 'Guess #2: ', 9, 'distance from Guesses: ', 1)
# If these were Cards, that would be our previous card we calculate our guesses from will be '5'.
# Guess #1 = 5 - 4 = 1
# Guess #2 = 5 + 4 = 9
# We generate the new number and compare the distance from 1 and 9. I this case the new number is 8
# and 8 is 1 away from Guess #2. So the distance is 1 Away
#
# You can see from debugging, which cards are most likely to be 0 Away, 1 Away, etc.
# The results are profound, not only can you make better card predictions, you also find
# that randomness is not completly disordered, but rather structured by distance!!!!
# 
# Randomness is an illusion, All RNG's, even TRUE Random, will follow this structure.
#  
# You can modify this program so that the previous and current are always the same 2 numbers
# to see that the results still follow this structure.
#
# {0: 4614594, 1: 9231939, 2: 9229865, 3: 4616544, 4: 2307059}
# 
# 0-4 Away Total: 30,000,000
# 0 Away:  15.38 %
# 1 Away:  30.77 %
# 2 Away :  30.77 %
# 3 Away:  15.39 %
# 4 Away:  7.69 %%

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

def randDistance(current, distance, low, high):
  newResult = current #random.randint(low,high)
  #if newResult > distance:
  #  guessOne , _ = wrap(newResult-distance, low, high, newResult)
  #else:
  #  guessOne , _ = wrap(distance-newResult, low, high, newResult)
  current = random.randint(low,high)
  guessOne , distOne = wrap(newResult-distance, low, high, current)
  guessTwo , distTwo  = wrap(newResult+distance, low, high, current)
  #guessThree , distThree  = wrap(guessTwo-guessOne, low, high, current)
  #guessFour , distFour  = wrap(guessOne-guessTwo, low, high, current)
  #_ , distAddOne = wrap(guessOne+current, low, high, current)
  #_ , distSubOneL = wrap(current-guessOne, low, high, current)
  #_ , distSubOneH = wrap(guessOne-current, low, high, current)
  #_ , distAdd = min(wrap(guessOne, low, high, current), wrap(guessFour, low, high, current)) #min(distAddOne, distSubOneL, distSubOneH)
  #distAdd = min(distAddOne, distSubOneL, distSubOneH)
  distAdd = min(distOne,distTwo) #,distThree,distFour)
  #_ , distAddTwo = wrap(guessTwo+current, low, high, current)
  #_ , distSubTwoL = wrap(current-guessTwo, low, high, current)
  #_ , distSubTwoH = wrap(guessTwo-current, low, high, current)
  #_ , distSub = min(wrap(guessTwo, low, high, current), wrap(guessThree, low, high, current))
  #distSub = min(distAddTwo, distSubTwoL, distSubTwoH)
  distSub = min(distOne,distTwo) #,distThree,distFour)
  newDistance = min(distAdd, distSub) #min(distAddOne, distSubOneL, distSubOneH, distAddTwo, distSubTwoL, distSubTwoH)
  return newResult, current, guessOne, guessTwo, newDistance

dist = int(highDefault * .33)
closeness = []

previous, current, _, _, newdistance = randDistance(5, dist, lowDefault,highDefault)
closeness.append(newdistance)
previous, current, _, _, newdistance = randDistance(5, dist, lowDefault,highDefault)
closeness.append(newdistance)

for x in range (1, 300000):
   closeness.append(newdistance)
   previous, current, distAdd, distSub, newdistance =  randDistance(current, dist, lowDefault, highDefault)
   if debug == 'TRUE':
       print ( 'previous: ', previous, 'new number: ', current, 'Guess #1: ', distAdd, 'Guess #2: ', distSub, 'distance from Guesses: ', newdistance)
   #if newdistance == 5:
   #   print ( 'previous: ', beforeprevious, 'current: ', previous, 'newCard: ', current, 'distance: ', newdistance)
   #if newdistance == 6:
   #   print ( 'previous: ', beforeprevious, 'current: ', previous, 'newCard: ', current, 'distance: ', newdistance)

a = dict()
a = dict(Counter(closeness))
print(a)
