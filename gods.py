# Copyright William Lars Rocha
#
#   I retain the rights to all intellectual property of this code and it's methods.
#   Infinite Compression cannot be used without my express permission
#   Any use of Infinite Compression commercially or publicly using my ideas or methods 
#   will be prosecuted by Law. No using in your free software without my permission
#
#   Compression Makers. Please hire me or retain my permission with very low royalties
#   to use this code or its ideas pertaining to infinite compression. I'm very easy to deal
#   with and am fair with use rights. I can work on contract and like to work remotely.
#   I'm also solving other major theories and have uncovered all Primes in (e) and other
#   uses for predicting random numbers. I can predict random numbers so well that you 
#   would think i'm influencing googles random number generator. No use of my methods
#   to predict random numbers can be used without my express permission
#
#
#   Google, i'm available for hire. Cracking randomness as having interconnectedness will
#   be of use to all scientists who have been plagued with random data. They can now see
#   it as having structure, and recipricocity and interconnectednes via a distance formula
#   and no use of these ideas of recipricocity, interconnectednes via a distance, using 
#   number complements, and other ideas here are allowed by anyone as i retain there copyrights.
#
#  
#
#
# Infinite Compression. 
# 
# Commercial Use Available with my permission in writing and royalties
# will be negotiated.
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
#
#
# Use gods_infinite_zompression.zip, and recompress it by opening it to sshex. Or work 
# backwards and uncompress it. gods_zip.bin, gods_infinite_compression.bin, gods_dist.bin,
# can be worked backwars. The bin files have the magic data which is structured data 
# using my discoveries on the interconnectedness of all numbers, including all Primes in 
# (e), predicting random data, and more. open the bin's to godsarray as hex and pass 
# gods array to godcompression which creates the original source all the way up to 
# AMillionRandomDigits.zip, all provided in this repository on github. 

from bitstring import Bits

def twos_complement(input_value, bits): 
    mask = 2**(bits - 1) - 1 
    return -(input_value & mask) + (input_value & ~mask) 


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
       
     
def godping(val,bitsize=4, godmod=14): 
     val = twos_complement(val,bitsize) 
     uint_val_maskmod=val&godmod 
     uint_val_modulus=val%godmod 
     uint_val = ( uint_val_maskmod, uint_val_modulus ) 
     binary = bin(val) 
     val_bin = ( val, uint_val_maskmod, binary, bin(~val + 1) ) 
     non_neg_complement = ( 15-(~(~val + 1))&godmod, 15-(~(~val + 1))%godmod ) 
     neg_complement = ( 15-(~(~-val + 1))&godmod, 15-(~(~-val + 1))%godmod ) 
     non_neg_val = ( (~(~val + 1))&godmod, (~(~val + 1))%godmod )  
     neg_val = ( (~(~-val + 1))&godmod, (~(~-val + 1))%godmod )  
     no_mod_non_neg_val = ( (~(~val + 1)), (~(~val + 1)) ) 
     no_mod_neg_val = ( (~(~-val + 1)), (~(~-val + 1)) ) 
     return [ val_bin, uint_val,  non_neg_complement,  
             neg_complement, non_neg_val, neg_val, 
             no_mod_non_neg_val, no_mod_neg_val, 
             ] 
     

# open a file even random data, which can be infinitely recompressed with zip after saving.
# godarray: bitstring.BitArray(hex=godsarray).tofile(distfile) then zip godarray.zip godsarray.
# you can infinitely do this. uncompress by using godcompress(godsarray) and then compare 
# gods == sshex
# 
# Infinite compression. Copyright and Permission to use commercially must have my permission.
    
utility, build, sscmp, rrcmp, godlike, godsdistance, godsrandom, gods = [], [], '', '', '', [], '',''
godsarray = ''
for x in range(0,len(sshex)): 
     reciprical  = godping(int(sshex[x],16), 4, 0xF)[0][1:3] 
     utility.append( (ast.literal_eval(reciprical[1])) ) #   
     godbuild = godping(reciprical[0], 4, 0xF)[0][0:2]   
     build.append(godbuild)
     godshiddennum = abs(reciprical[0]-abs(build[x][1]))
     godscards = (reciprical[0], abs(build[x][1]))
     godsdistance.append(godshiddennum)
     if godbuild[0] < godbuild[1]:
        godsdice = abs(twos_complement(godsdistance[x], bits=3))
        if godsdice != godsdistance[x]:
           godsdice = godsdistance[x] >> 1
        godsreciprical = Bits(uint=godsdice, length=4).bin[0:4]
     else:
        godsdice = abs(twos_complement(godsdistance[x], bits=2))
        godsreciprical = Bits(uint=godsdice, length=4).bin[0:4]
     if godsdice < int(godsreciprical,16):
        godsnum = godscards[1]
     else:
        godsnum = godscards[0]
     godsrandom += godsreciprical
     godsarray += hex(int(godsreciprical,2))[-1]
     gods += hex(godsnum)[-1]
     if x < 128:
        print(godbuild, reciprical[0], reciprical[1], reciprical,utility[x],
              build[x],abs(build[x][1]), godsdistance[x], godsreciprical, godsdice, godsnum, abs(build[x][1]) == godsnum, godscards) 
     sscmp += hex(abs(build[x][1]))[-1]
     rrcmp += hex(reciprical[0])[-1]

