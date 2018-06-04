import wave, struct, os, sys, numpy, time, random, operator, pickle
from scipy.io import wavfile
rootTrue = "C:\\Users\\felixdgaypc\\Desktop\\wav class 0\\"
rootFalse = "C:\\Users\\felixdgaypc\\Desktop\\wav class 1\\"
MAX_VALS = 2646000
MAX = 36767
MIN = -32768
#pcm_s16le mono channel wav files 44100hz
#0 represents gachi, 1 represents non-gachi


#returns an array of amplitudes normalized to 0.0 to 1.0
#max frequency i care about is ~10k, 
def get_data_point(filename, root):  
    global used
   # try:
    fs, datainit = wavfile.read(root+filename)
    data = datainit.tolist()
   
    arr =  []
    print(root+filename)
    
    if len(data) < MAX_VALS:
        i = 0
        j = len(data)
        while len(data) < MAX_VALS:
            data.append(data[i%j])
            i += 1
        arr = data
        
    elif len(data) > MAX_VALS:
        arr = data[:MAX_VALS]
    #normalize values
    for i in range(len(arr)):
        arr[i] = (arr[i] - MIN) / (MAX - MIN)
    return arr[1::4]
   # except:
      #  print('Skipped:' + filename)    
       # return None



##########################TEST ALGORITHM BEGINS#########################
start = time.time()


fileIndex = 1
for i in os.listdir(rootTrue):
    if str(fileIndex)+'.txt' not in os.listdir('C:\\Users\\felixdgaypc\\Desktop\\class 0 data\\'):
        newData = get_data_point(i, rootTrue)
        with open(str(fileIndex)+'T.txt', 'w') as trueFile:
            trueFile.write(str(newData))
            print(len(newData))
    fileIndex += 1

print('Done True')

fileIndex = 1
for i in os.listdir(rootFalse):
    if str(fileIndex)+'.txt' not in os.listdir('C:\\Users\\felixdgaypc\\Desktop\\class 1 data\\'):
        newData = get_data_point(i, rootFalse)
        with open(str(fileIndex)+'F.txt', 'w') as falseFile:
            falseFile.write(str(newData))
            print(len(newData))
    fileIndex += 1

print('Done False')





done = time.time()
print(done-start)


