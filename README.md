# nomorerandom
This code helps prove that random is not disordered. It is in fact order structured by distance. This can be proven statistically with the code here or with any RNG, wether it is PRNG or TRUE RANDOMNESS.


This program confirms something awesome about the nature of random number and guesses: You can modify this and now that when you have a number generated, you can guess within a distance, and predict with probability how close that number will be to your guess. Truly, this is a fundamental feature of any RNG you run this programs logic with, but i haven't tried it with any fancy ones yet. Just the pwned Google and your laptops python RNG. Thanks.

Will, Lars or William.

Test the following with the python script attached, or quickly test and confirm here:
https://www.google.com/search?q=random+number+generator

So, when a RNG picks 1 (and you can do this for all numbers), you have a structure of randomness that you can predict the distance from two guesses. for any 1-max, use max * .33 to get the structures boundries, For 1-10, if you start with 1, you have this structure and will know that your guess will always be close to the next random number.

Predicting the next random number with structure.

min = 1
max = 10
boundry = int(round(max *.33)
Boundry = 3
Number 1
Guesses = 1 - boundry abd 1 + boundry which are 8 and 4
So to guess the next random number after a RNG generates a 1, Use 8 and 4 as your guesses.

Starting number: 1
_ -- 1 < 3 Away ( Hey, it's our starting number.
6 -- 2 . < 2 Away
7 -- 3 . < 1 Away
8 -- 4 < 0 Away < Your Guesses
9 -- 5 . < 1 Away
10 -- _ . < 2 Away

If a random number picked 1, it's next result will be stastically closer to your two guesses by a distance of 1, or 2 away. with 0 being next and 3 away been seen least likely. So 1 away. which is 7,3,9,5 are more likely the next number of 2 away which are 6,2 or 10. and those more likely than 3 away of 8,4,

So that's why i can guess so close, and now I know the probability that the RNG will pick next, and it's based on how close those numbers are to my guesses. Almost as if the RNG knows to pick closely to my guesses. How does it know to do that for every number i utilize this test with? I'm not seeding it with anything, the RNG just seems to converge in a statistical way to pick 3 Away only 20 percent of the itme. Huh.

Yeah. Huh.

Huh.

So Randomness is not truly random. It is numbers interconnected by a distance. in a set of 1 to 10, the starting distance
of your guesses is determined by (MAX * .33) and from adding and subtracting my number, we get our guesses. So in a way, every
number 1, 10, contains it's own information on it's interconnectedness. This distance shows shows that randomness isn't random,
but numbers with a structured order determined by distance. 


