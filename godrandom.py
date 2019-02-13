#!/usr/bin/python
# Deck of Cards Example.
# Let's say your last number was 3, and the new number is 2. So you hold 3,2 as in a deck of cards
# 0: away from these (3,2, 3+2=5, 3-2=A, 2-3=Q)                             are 5,A,Q
# 1: away from these (3+2+1=6, 3+2-1=4, 3-2+1=2, 3-2-1=K, 2-3+1=K, 2-3-1=J) are 6,4,2,K,K,J
# 2: away from these (3+2+2=7, 3+2-2=3, 3-2+2=3, 3-2-2=Q, 2-3+2=A, 2-3-2=10) are 7,3,3,Q,A,10
# 3: away from these (3+2+3=8, 3+2-3=2, 3-2+3=4, 3-2-3=J, 2-3+3=2, 2-3-3=9) are 8,2,4,J,2,9
# 4: away from these (3+2+4=10, 3+2-4=A, 3-2+4=5, 3-2-4=9, 2-3+4=3, 2-3-4=8) are 10,A,5,9,3,8
# 
# But wait, how are random numbers preferring cards that have a closeness to the difference of your two cards?
# It's impossible right? Unless a super intelligence shuffled the deck to be that way? 
# Lets look at some stats, the RNG seems to prefer cards that are 1 away from 5,A,Q which we determined above
# The likeness these groups above cards will appear are: 
#       {0: 6565609, 1: 10657864, 2: 7454433, 3: 4256672, 4: 1065428}
# 
# So your most likely to see A,Q,3 followed by K,6,4,2,J, followed by 5,7,10, and least likely to see 9 and 8
# Weird, but true due to statistics tying the closeness of cards being more likely to be close to the 
# previous cards due to the Law of Interconnectedness. 
#
# Why aren't the following groupings of closeness ( 0 being exact) more evenly distributed. With 6 cards being
# chosen for each away grouping, you'd expect this to be more uniform. It isn't. Why not?
# $ cat output2.txt
# {0: 6,565,609, 1: 10,657,864, 2: 7,454,433, 3: 4,256,672, 4: 1,065,428}
# {0: 6,564,394, 1: 10,650,336, 2: 7,460,704, 3: 4,260,106, 4: 1,064,466}
# {0: 6,566,673, 1: 10,650,525, 2: 7,453,778, 3: 4,264,690, 4: 1,064,340} 
# {0: 6,569,251, 1: 10,649,288, 2: 7,454,658, 3: 4,260,523, 4: 1,066,286}
# {0: 6,565,562, 1: 10,652,761, 2: 7,456,275, 3: 4,260,745, 4: 1,064,663}
# {0: 6,568,077, 1: 10,653,367, 2: 7,452,381, 3: 4,261,679, 4: 1,064,502}
# {0: 6,565,179, 1: 10,651,757, 2: 7,456,416, 3: 4,260,846, 4: 1,065,808}
#
# Because we wrap around the deck, distance is bounded by 4, and we have to have 3 numbers anchoring our Exact picks
# which we then group off of. In this case exact for 3,2 is A,Q,5. And away from anchors from those. So 1 away from 
# A would be 1,K. 2 away from A would be 2,Q. When we cycle cards through a deck then, if we have 3,2,
# we should expect the next card to be 1 away from it's exact differences, which is why exact is about half of 1
# away, which has 6 results, because 1 away from 3 cards is 6 cards.
#
# Find a deck of cards. Take 3,2 out. Shuffle the rest. Now from each card you pull off the top of the deck, what group
# does it fall into above? Discard that card, and pull the next card off the top of the deck and compare to 3,2 again.
# How does the deck conform to the statistics here? Would it be uniformly random, or shaped like the stats here? How again
# are my randoms not uniform, when I use random() as is, no PRNG code.

import signal, random
from collections import Counter

depth = .33

lowDefault = 1
highDefault = 13

thedistance = int(round(highDefault * depth))

# del boundThis
def boundThis(x, low=lowDefault, high=highDefault, origin=0, anchor=0):
    minL = low
    maxH = high
    boundX = int(x)
    if (boundX == 0):
        boundX = 0
    elif (boundX >= minL) and (boundX <= maxH):
        if origin != 0 and anchor != 0:
           boundXx = abs(origin-boundX) #abs(anchor-boundX)
           boundXy = abs(origin-boundX)
           boundX = min(boundXx, boundXy, x)
    elif (boundX > maxH):
        boundX = boundX % maxH + minL-1
        if (boundX > maxH):
          boundX-=maxH-1
        if (origin != 0 and anchor != 0):
        #   print(boundX, x)
           boundXx = abs(origin-boundX) # abs(anchor-boundX)
           boundXy = abs(origin-boundX)
           boundX = min(boundXx, boundXy)
    elif (x < minL):
          while(boundX < minL):
              boundX += maxH-minL+1
          if origin != 0 and anchor != 0:
             boundXx = abs(origin-boundX) # abs(anchor-boundX)
             boundXy = abs(origin-boundX)
             boundX = min(boundXx, boundXy)
          if origin == 0 and anchor == max:
             boundX = 0
    return boundX

# boundThis(16+5,1,13,5,16)
# boundThis(4-12,1,13,5,16)


result = random.randint(1,13)
newResult = random.randint(1,13)

# del randDistance
def randDistance(lastguess, low=lowDefault, high=highDefault, distance=thedistance):
  # result = random.randint(low, high)
  print('------------------------------')
  print('midAnchor which is a random number called lastguess: ', lastguess, '(newResult from previous run)')
  midAnchor = lastguess
  newResult = random.randint(low,high)
  print('newResult (random #, how can we prove interconnectedness to lastguess??): ', newResult, ' used in next call to randDistance()')
  print('We prove it by adding/subtracting the distance:', distance, ' from the value and seeing how close our next guess is')
  print('This can only be possible in a quantum state machine that knows the future due to information entaglement')
  print('This knowledge can make you a billionaire in the stock market')
  print('Alphabet/Google will pay me $1,000,000 dollars as a sign on bonus :-)')
  # new distanceExact
  # The deck ( or numbers ) wraps around. So when you get to 0, it loops back to max value. This is why we do the following cases
  #
  # You can test from the python interpreter with. We add and subtract the new random from the last random number, and calculate
  # distance. If last value is 70, and the new random is 1. Then we have 71,69,30(wrap deck 1-70 is basically 13-70 which equals 30)
  # As you can see 71 is 1 away from 70, so the distance of the new random from the last random is 1.
  # >>> boundThis(23-79,1,13,23,79)
  # 21
  # And you can see that due to wrap around, the distance between 23-79 wraps around for a distance between the two numbers being 21
  #
  # Deck of Cards Example.
  # Let's say your last number was 3, and the new number is 2. So you hold 3,2 as in a deck of cards
  # 0: away from these (3,2, 3+2=5, 3-2=A, 2-3=Q)                             are 5,A,Q
  # 1: away from these (3+2+1=6, 3+2-1=4, 3-2+1=2, 3-2-1=K, 2-3+1=K, 2-3-1=J) are 6,4,2,K,K,J
  # 2: away from these (3+2+2=7, 3+2-2=3, 3-2+2=3, 3-2-2=Q, 2-3+2=A, 2-3-2=10) are 7,3,3,Q,A,10
  # 3: away from these (3+2+3=8, 3+2-3=2, 3-2+3=4, 3-2-3=J, 2-3+3=2, 2-3-3=9) are 8,2,4,J,2,9
  # 4: away from these (3+2+4=10, 3+2-4=A, 3-2+4=5, 3-2-4=9, 2-3+4=3, 2-3-4=8) are 10,A,5,9,3,8
  # 
  # But wait, how are random numbers preferring cards that have a closeness to the difference of your two cards?
  # It's impossible right? Unless a super intelligence shuffled the deck to be that way? 
  # Lets look at some stats, the RNG seems to prefer cards that are 1 away from 5,A,Q which we determined above
  # The likeness these groups above cards will appear are:
  #       {0: 6565609, 1: 10657864, 2: 7454433, 3: 4256672, 4: 1065428}
  # 
  # So your most likely to see A,Q,3 followed by K,6,4,2,J, followed by 5,7,10, and least likely to see 9 and 8
  # Weird, but true due to statistics tying the closeness of cards being more likely to be close to the 
  # previous cards due to the Law of Interconnectedness. When we cycle cards through a deck then, if we have 3,2,
  # we should expect the next card to be 1 away from it's exact differences, which is why exact is about half of 1
  # away, which has 6 results, because 1 away from 3 cards is 6 cards.
  #
  # Why aren't the following groupings of closeness ( 0 being exact) more evenly distributed. With 6 cards being
  # chosen for each away grouping, you'd expect this to be more uniform. It isn't. Why not?
  # $ cat output2.txt
  # {0: 6,565,609, 1: 10,657,864, 2: 7,454,433, 3: 4,256,672, 4: 1,065,428}
  # {0: 6,564,394, 1: 10,650,336, 2: 7,460,704, 3: 4,260,106, 4: 1,064,466}
  # {0: 6,566,673, 1: 10,650,525, 2: 7,453,778, 3: 4,264,690, 4: 1,064,340} 
  # {0: 6,569,251, 1: 10,649,288, 2: 7,454,658, 3: 4,260,523, 4: 1,066,286}
  # {0: 6,565,562, 1: 10,652,761, 2: 7,456,275, 3: 4,260,745, 4: 1,064,663}
  # {0: 6,568,077, 1: 10,653,367, 2: 7,452,381, 3: 4,261,679, 4: 1,064,502}
  # {0: 6,565,179, 1: 10,651,757, 2: 7,456,416, 3: 4,260,846, 4: 1,065,808}
  #
  # Because we wrap around the deck, distance is bounded by 4, and we have to have 3 numbers anchoring our Exact picks
  # which we then group off of. In this case exact for 3,2 is A,Q,5. And away from anchors from those. So 1 away from 
  # A would be 1,K. 2 away from A would be 2,Q.
  # How does the deck conform to the statistics here? Would it be uniformly random, or shaped like the stats here? How again
  # are my randoms not uniform, when I use random() as is, no PRNG code.
  if newResult != 0 or newResult != 0:
    distanceLowSubtractRandomFromGuess = boundThis(lastguess-newResult,low,high,lastguess, newResult)
    distanceLowSubtractGuessFromRandom = boundThis(newResult-lastguess,low,high, newResult, lastguess)
    #distanceLowSubtractRandomFromGuess = boundThis(abs(newResult-lastguess),low,high, lastguess, newResult)
    #distanceLowSubtractGuessFromRandom = boundThis(abs(newResult-lastguess),low,high, newResult, lastguess)
    distanceLowAddRandomFromGuess = boundThis(lastguess+newResult,low,high, lastguess)
    distanceLowAddGuessFromRandom = boundThis(newResult+lastguess,low,high, newResult)
    print('lastguess: ', lastguess)
    print("newResult: ", newResult)
    print("lastguess-newResult: '", distanceLowSubtractRandomFromGuess)
    print("newResult-lastguess: ", distanceLowSubtractGuessFromRandom)
    print('lastguess+newResult: ', distanceLowAddRandomFromGuess)
    print('newResult+lastguess: ', distanceLowAddGuessFromRandom)
    distanceExact = min(distanceLowSubtractRandomFromGuess, distanceLowSubtractGuessFromRandom, distanceLowAddRandomFromGuess, distanceLowAddGuessFromRandom)
  else:
    distanceExact = 0
  if distanceExact < 1:
     distancExact = -distanceExact
  print('distanceExact: ', distanceExact)
  print('Added/Subtracted/Wrapped: ', newResult, ' from midAnchor', midAnchor, ' and one of those results are this distanceFromNewRandom: ', distanceExact ) #, distanceMid))
  if (min(newResult, lastguess) == 0):
     next
     print("Exact Guess! Randomly Exact is 3 in 14 or 21% chance hit, but in this case we predict the outcome rather than it being random. Notice that the midAnchor is a random number and we are predicting closeness to that random number. This should be even over all distances, but this proves Entropy is interconnected to the number by a closeness factor. Distance of 0,1,2 come up more than others")
  return newResult, distanceExact

lastguess = 10
closeness = []

lastguess, newdistance = randDistance(lastguess, lowDefault,highDefault)
closeness.append(newdistance)
lastguess, newdistance = randDistance(lastguess, lowDefault,highDefault)
closeness.append(newdistance)

for x in range (1, 300000):
 try:
  closeness.append(newdistance)
  lastguess, newdistance = randDistance(lastguess, lowDefault,highDefault)
 except: 
  continue

a = dict()
a = dict(Counter(closeness))
print(a)

