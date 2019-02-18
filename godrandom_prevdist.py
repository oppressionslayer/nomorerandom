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
# Example, for any number in Base 10
# Let's choose '1' as an example.
# '1'
# Boundries in base10 are 8 and 4. Determined by int(Base10 * .33) which is 3 and 
# 1 minus the boundry is 8 and 1 plus the boundry is 4
#
# 3 Away -- _ , 1 . ( _ represents a duplicate number, so it is removed )
# 2 Away -- _ , 10
# 1 Away -- 5 , 9
# 0 Away -- 4 , 8   ( A number following '1' will follow this algorithim, with 4 , 8 being 0 Away )
# 1 Away -- 3 , 7
# 2 Away -- 2 , 6
# 3 Away -- _ , _
#
# Statitistics to confirm this ordered structure:
# Grouped by Away. 0: is 0 Away, 1: is 1 Away, etc.
# {0: 6000832, 1: 12002397, 2: 8996037, 3: 3000735}
# 
# 0-3 Away Total: 30,000,000
# 0 Away:  20.00 %
# 1 Away:  40.00 %
# 2 Away :  29.998679 %
# 3 Away:  10.00 %
# 
# Here are two runs using min=1, max=50. DISTANCE FROM PREVIOUS RANDOM NUMBER for the first run is 5, second run is 10.
# That means if a random number is 30, We use 25 and 35 for our guesses. You can see that setting the distance, 
# between 5 and 10 had an affect on how often close numbers are randomly generated. Just by changing our two numbers 
# that we have more chances to guess close than further away. 2 to 1 almost
# 
# NOTICE BELOW THAT MODIFICATIONS MADE TO DISTANCE CHANGE THE STATISTICS OF THE RNG'S CLOSENESS TO THE GUESSES. BY 
# CHANGING DISTANCE YOU AFFECT THE STRUCTURE OF THE RANDOMNESS SHAPE INA VISIBLE WAY. IF THE STASTICS WAD NOT 
# INTERCONNECTED, WE WOULD EXPECT THE DISTRIBUTION TO REMAIN EVEN ACROSS THE DATA. THIS HELPS VISIBLY SEE
# THAT RANDOM DATA CAN BE SEEN TO HAVE STRUCTURE BOUNDED AND BASED BY DISTANCE TO PREVIOUS NUMBERS
# 
# By distance 5 ( If 50 is the random number, our guesses for the next random are 45 and 65 ) See how our odds of getting < 5
# Away compare to the next set of data. Guessing within a bounds affects the odds that our guess will be close or not
# {0: 6081, 1: 11850, 2: 11919, 3: 11983, 4: 12065, 5: 8901, 6: 6085, 7: 6063, 8: 6026, 9: 5989, 10: 5998, 11: 5984,
#;12: 6045, 13: 5978, 14: 5914, 15: 6005, 16: 5945, 17: 6024, 18: 5877, 19: 6179, 20: 5927, 21: 6225, 22: 5991, 
# 23: 5923, 24: 6091, 25: 6035, 26: 6026, 27: 5971, 28: 5843, 29: 6049, 30: 5955, 31: 5912, 32: 5986, 33: 6056,
# 34: 6047, 35: 6186, 36: 5946, 37: 6070, 38: 6075, 39: 5844, 40: 6048, 41: 5930, 42: 6001, 43: 6055, 44: 5924, 45: 2974}
#
#
# By distance 10 ( If 50 is the random number, our guesses for the next random are 40 and 60 ) We have an almost 40% chance 
# of getting close to our guesses. 
# {0: 5930, 1: 12123, 2: 12075, 3: 11824, 4: 12057, 5: 11921, 6: 12154, 7: 12280, 8: 12000, 9: 11943, 10: 8945, 11: 5998,
# 12: 6024, 13: 6141, 14: 6066, 15: 5922, 16: 5985, 17: 6058, 18: 5881, 19: 6030, 20: 6028, 21: 5897, 22: 6004, 23: 5976,
# 24: 6032, 25: 6022, 26: 5993, 27: 5952, 28: 6021, 29: 5921, 30: 5924, 31: 5970, 32: 6068, 33: 6030, 34: 6041, 35: 5887,
# 36: 5920, 37: 5998, 38: 6036, 39: 5916, 40: 3008}
# 

import random
import argparse
from collections import Counter


maxmin = 1
maxmax = 10
defdist = int(maxmax * .33)
definterval = 300000
defdebug = 'FALSE'

parser = argparse.ArgumentParser(description='Process random numbers with structured order. ' +
                   'For an intersting example of a deck of cards use: ' +
                   'godrandom_bydistance.py --min 1 --min 13 --dist 2 --debug TRUE')
parser.add_argument('--min', dest='lowDefault',type=int,
                    default=maxmin,
                    help='the minimum for your data set, default is 1')
parser.add_argument('--max', dest='highDefault', type=int,
                    default=maxmax,
                    help='the maximum for your data set, default is 10')
parser.add_argument('--dist', dest='defDist', type=int,
                    default=argparse.SUPPRESS,
                    help='The distance of your boundries. Default to max * .33')
parser.add_argument('--interval', dest='defInterval', type=int,
                    default=definterval,
                    help='How many iterations to run. Default is 300,000')
parser.add_argument('--debug', dest='defDebug',
                    default=defdebug,
                    help='Default is FALSE. Set to TRUE to print results')

args = parser.parse_args()

# Default is 1,13 ehich is the size of a deck of cards
lowDefault = args.lowDefault
highDefault = args.highDefault
interval = args.defInterval

# Change to choose an exact distance to see hoe distance influences rhe
# closeness of your guess by twofold bounded by your distance.
try:
  dist = args.defDist
except:
  dist = int(round(args.highDefault *  .33))

# debug = 'TRUE' or 'FALSE'
debug = args.defDebug

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

def randDistance(current, distance, low, high):
  distOne=50
  distTwo=50
  distPrevious=50
  newResult = current
  current = random.randint(low,high)
  guessOne , distOne = wrap(newResult-distance, low, high, current)
  guessTwo , distTwo  = wrap(newResult+distance, low, high, current)
  if current == (newResult, guessOne , guessTwo):
      _, distOne = wrap(current, low, high, guessOne)
      _, distTwo = wrap(current, low, high, guessTwo)
  guessPrevious, distPrevious = wrap(newResult,low,high,current)
  distOne = min(wrap(guessOne, low, high, current)[1], distOne)
  distTwo = min(wrap(guessTwo, low, high,current)[1], distTwo)
  distPrevious = min(wrap(newResult, low, high, current)[1], distPrevious)
  distAdd = min(distOne,distTwo,distPrevious) #,distThree,distFour)
  distSub = min(distOne,distTwo) #,distThree,distFour)
  newDistance = min(distAdd, distSub)
  return newResult, current, guessOne, guessTwo, newDistance

closeness = []

previous, current, _, _, newdistance = randDistance(50, dist, lowDefault,highDefault)
closeness.append(newdistance)
previous, current, _, _, newdistance = randDistance(50, dist, lowDefault,highDefault)
closeness.append(newdistance)

for x in range (1, interval):
   closeness.append(newdistance)
   previous, current, distAdd, distSub, newdistance =  randDistance(current, dist, lowDefault, highDefault)
   if debug == 'TRUE':
       print ( 'RNG Number: ', current, 'Main Guess: ', previous, 'Guess #1: ', distAdd, 'Guess #2: ', distSub, 'distance from RNG to Guesses: ', newdistance)

a = dict()
closeness = sorted(closeness)
a = dict(Counter(closeness))
print(a)
