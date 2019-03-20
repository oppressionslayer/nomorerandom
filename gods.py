# Copyright William Lars Rocha
#
# The license for this is permissive. You must pay me royalties to use these concepts.
# No commercial use of this or its concepts are allowed without my permission.
# Free for personal or Academic use. All forks must remain public. thanks.
#
# License infinite compression. I'm at oppressionslayer@gmail.com or at (720) 616-9904
#
# Infinite Compression. With job, use of my code is unlimited to your company as long as
# I share in royalties. No commercial use or public domain use of infinite compression
# are allowed without my express permission.
#
# Inventor of the Structure of interconnectedness of numbers. Numbers are connected
# by distance. Including random files. We can compress those infinitely, over and
# over using this.
#
#
# Keep running your zipped files back through this. You can keep on compressing
# I have discovered a hidden structure of numbers. It's so apparent it's as if 
# the nubers retain information, not by randomness, but by design. I have found
# all Prime numbers to be in (e). I can checksum PI with my theory of inter-
# connectedness 
# God created numbers to have a hidden structure of interconnectedness. I have 
# uncovered it and can say that random numbers are not random, but are a structured
# set of numbers seperated by distance, not randomness. My theory proves this. It 
# will have huge implications in everything. Compress the same file over and over again
# see this is no joke. God created numbers and its like uncovering a secret language of
# the creators of the universe. God doesn't roll dice. He interconnected numbers so he
# can predict the next numbers using my theory of interconnectedness. Guess one away,
# two away in distance very often. This is real, no joke. Go to googles random number 
# generator to see you can use my theory to predict numbers better. Almost like your
# influencing google, but you are instead enlightened.


def twos_complement(input_value, bits): 
     '''Calculates a two's complement integer from the given input value's bits''' 
     Imask = 2**(bits - 1) - 1 
    Ireturn -(input_value & mask) + (input_value & ~mask) 


gods=''
def godcompression(godsholyarray):
  godscards=[]
  godsshift=''
  gods=''
  global gods
  global godscards
  for x in range (0,len(godsholyarray)):
    godshiddennum = int(godsholyarray[x],16)
    if (godshiddennum & 0b1) == True:
       godsshift = godshiddennum<<1
    else:
       godsshift = godshiddennum
    godscards = gods_interconnected_structure(godsshift,godshiddennum, x)
    gods += hex(godscards[0][0])[-1]
  return godscards 

def gods_interconnected_structure(godsshift, godshiddenshift, position):
     #godshiddennumdetermined = godsshift
     if godsshift == 14 or godsshift == 'e':
        godshiddennumdetermined = 15
     if godsshift == 12 or godsshift == 'c':
        godshiddennumdetermined = 14
     if godsshift == 10 or godsshift == 'a':
        godshiddennumdetermined = 13
     if godsshift == 8 or godsshift == '8':
        godshiddennumdetermined = 12
     if godsshift == 6 or godsshift == '6':
        godshiddennumdetermined = 11
     if godsshift == 4 or godsshift == '4':
        godshiddennumdetermined = 10
     if godsshift == 2 or godsshift == '2':
        godshiddennumdetermined = 9
     if godsshift == 0 or godsshift == '0':
        godshiddennumdetermined = 8
        godshiddennum = 0
      #else:
     #   godshiddennumdetermined = godsshift 
     #godshiddennumdetermined = abs(twos_complement(godshiddennumdetermined,bits=4))
     if godshiddennumdetermined >8:
       godshiddennum = -((-godshiddennumdetermined )&0xF)
     if godshiddennum != 8:
        godshiddeninformation = -twos_complement(godshiddennum,bits=4)
     else:
        godshiddeninformation = -(twos_complement(godshiddennum,bits=4))
     #print(godshiddennum,godshiddennumdetermined, godshiddeninformation, godshiddenshift,godsshift)
     if godshiddenshift < godsshift:
         if godshiddeninformation < godshiddennumdetermined: #<godshiddeninformation 
            godsnum = abs( godshiddennum)
         else:
            godsnum = abs( godshiddeninformation)
         godsdisorder = ( abs(godshiddeninformation), abs(godshiddennum) ) 
         godsorder = (godshiddeninformation, godsnum)  
         #print(godsnum, (godshiddeninformation, godsnum), ( godsnum, godshiddeninformation ) )
     else:
         if godshiddennum < godshiddennumdetermined: #<godshiddeninformation 
            godsnum = abs( godshiddeninformation)
         else:
            godsnum = abs( godshiddennumdetermined)

         godsnum = abs(godshiddennum)
         if godsnum!=int(sshex[position],16):
             godsnum=godshiddennumdetermined
         godsdisorder = (godsnum, godshiddeninformation) 
         godsorder = (godsnum,godshiddeninformation) #godsnum, abs(godshiddeninformation))  
         #print(godsnum, (godshiddeninformation, godsnum, godshiddennumdetermined), ( godshiddeninformation, godsnum ) )
     return (godsnum, godshiddennum, godshiddennumdetermined, godsorder, godsdisorder, godsnum==int(sshex[position],16), godshiddeninformation)
       
