import wave, struct, os, sys, numpy, time, random, operator
from scipy.io import wavfile
rootTrue = "C:\\Users\\felixdgaypc\\Desktop\\wav class 0\\"
rootFalse = "C:\\Users\\felixdgaypc\\Desktop\\wav class 1\\"
MAX_VALS = 13333333
MAX = 36767
MIN = -32768
##########################TEST ALGORITHM BEGINS#########################
start = time.time()

#Read in weights
with open('weights.txt', 'r') as weightFile:
    weights = weightFile.read().split(',')
weights.pop()
for i in range(len(weights)):
    weights[i] = float(weights[i])
#read in used files
with open('used.txt', 'r') as usedFile:
    used = usedFile.read().split('\n')
with open('class 0 data\\1.txt', 'r') as usedFile:
    a1 = usedFile.read().split(',')
    print(a1[-10:])
    print(len(a1))
with open('class 1 data\\1.txt', 'r') as usedFile:
    a1 = usedFile.read().split(',')
    print(a1[-10:])
    print(len(a1))
    

'''
main loop:
    seed = random.randint(0,1)
    choose random txt from that folder
    guess(based on data)
    if guess == seed right / != seed wrong 
    adjust weights
    save weights in file
    mark filename as used
'''     





done = time.time()
print(done-start)
'''INITIALIZE NEW WEIGHTS, USE WITH  CAUTION
weights = [0]*2666667
with open('weights.txt', 'w') as weightFile:
    for i in weights:
        weightFile.write(str(i))
        weightFile.write(',')
'''