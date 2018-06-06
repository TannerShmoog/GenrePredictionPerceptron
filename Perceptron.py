import wave, struct, os, sys, numpy, time, random, operator
from scipy.io import wavfile
rootTrue = "wav class 0\\"
rootFalse = "wav class 1\\"
#going to take every other data point needle dropping for 30 seconds at random
#44100Hz * 30 /  2 = 661500
MAX_VALS = 661500 
MAX = 36767
MIN = -32768
##########################TEST ALGORITHM BEGINS#########################
start = time.time()

#Read in weights
def read_weights():
    with open('weights.txt', 'r') as weightFile:
        weights = weightFile.read().split(',')
    weights.pop()
    for i in range(len(weights)):
        weights[i] = float(weights[i])
    return weights

#resets all weights to zero
def new_weights():
    weights = [0] * (MAX_VALS + 1)
    weights[0] = 1
    with open('weights.txt', 'w') as weightFile:
        for i in weights:
            weightFile.write(str(i))
            weightFile.write(',')

#returns an array of amplitudes normalized to 0.0 to 1.0
#max frequency i care about is ~10k, 
def get_data_point(filename, root):  
    print(root+filename)
    fs, datainit = wavfile.read(root+filename)
    data = datainit.tolist()
    
    last_possible_frame = len(data) - (MAX_VALS * 2) - 2
    start_frame = random.randint(0,last_possible_frame)
    end_frame = start_frame + (MAX_VALS * 2)
    
    arr =  data[start_frame:end_frame]
    #normalize values
    for i in range(len(arr)):
        arr[i] = (arr[i] - MIN) / (MAX - MIN)
    return arr[1::2]

#predict a wav file
def predict(data_point, weights):
    activation = weights[0]
    for i in range(len(data_point)):
        activation += weights[i+1] * data_point[i]
    if activation >= 0.0:
        return 0
    else:
        return 1
    
weights = read_weights()
l_rate = 0.2


for i in range(10):
    seed = random.randint(0,1)
    if seed == 0:
        root = rootTrue
    elif seed == 1:
        root = rootFalse
    filename = random.choice(os.listdir(root))
    data_array = get_data_point(filename, root)
    prediction = predict(data_array, weights)
    if seed != prediction:
        #train the weights for wrong answer
        pass
    print("Expected: " + str(seed) +"\tPredicted: " + str(prediction))

done = time.time()
print(done-start)

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



'''Not using txt files for input anymore
#read an input file into an array of floats
def read_input_file(filename, classN):
    a1 = []
    if classN == 0:
        with open('class 0 data\\'+filename, 'r') as inputFile:
            a1 = inputFile.read().split(',')
            a1[0] = a1[0].replace('[', '')
            a1[-1] = a1[-1].replace(']', '')
            for i in range(len(a1)):
                a1[i] = float(a1[i])                 
    elif classN == 1:
        with open('class 1 data\\'+filename, 'r') as inputFile:
            a1 = inputFile.read().split(',')
            a1[0] = a1[0].replace('[', '')
            a1[-1] = a1[-1].replace(']', '')
            for i in range(len(a1)):
                a1[i] = float(a1[i])
    return a1
'''    