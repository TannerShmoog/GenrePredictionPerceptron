import wave, struct, os, sys, numpy, time, random, operator
from scipy.io import wavfile
rootTrue = "wav class 0\\"
rootFalse = "wav class 1\\"
#Take every other data point needle dropping for 30 seconds at random
#44100Hz * 30 /  2 = 661500
MAX_VALS = 661500 
MAX = 36767
MIN = -32768
l_rate = 0.2
######################################################################
start = time.time()

#Read in accuracy information
def read_accuracy():
    with open('accuracy.txt', 'r') as accFile:
        acc = accFile.read().split('\n')
    return acc

#Read in weights
def read_weights():
    with open('weights.txt', 'r') as weightFile:
        weights = weightFile.read().split(',')
    weights.pop()
    for i in range(len(weights)):
        weights[i] = float(weights[i])
    return weights

def write_to_file(weights, num_predictions, num_correct):
    with open('weights.txt', 'w') as weightFile:
        for i in weights:
            weightFile.write(str(i))
            weightFile.write(',')
    with open('accuracy.txt', 'w') as accFile:
        accFile.write('Total\t'+str(num_predictions))
        accFile.write('\n')
        accFile.write('Correct\t'+str(num_correct))
    
#Resets all weights to zero
def new_weights():
    weights = [0] * (MAX_VALS + 1)
    with open('weights.txt', 'w') as weightFile:
        for i in weights:
            weightFile.write(str(i))
            weightFile.write(',')

#Returns an array of amplitudes normalized to 0.0 to 1.0
def get_data_point(filename, root):  
    print(root+filename)
    fs, datainit = wavfile.read(root+filename)
    data = datainit.tolist()
    
    last_possible_frame = len(data) - (MAX_VALS * 2) - 2
    start_frame = random.randint(0,last_possible_frame)
    end_frame = start_frame + (MAX_VALS * 2)
    
    arr =  data[start_frame:end_frame]
    #Normalize values
    for i in range(len(arr)):
        arr[i] = (arr[i] - MIN) / (MAX - MIN)
    #Take every other value from array
    arr = arr[1::2]
    #insert bias
    arr.insert(0,1)
    return arr

#Make a prediction based on 30 second clip from a wav file
def predict(data_point, weights):
    activation = 0.0
    for i in range(len(data_point)):
        activation += weights[i] * data_point[i]
    print(activation)
    return 1 if activation >= 0.0 else 0

#Train the weights for an incorrect prediction
def train_weights(data_array, weights, l_rate, 
                  num_predictions, num_correct, seed, prediction):
    current_accuracy = num_correct / num_predictions
    error = seed - prediction
    if current_accuracy >= 99.0:
        return None
    for i in range(len(weights)):
        weights[i] = weights[i] + (l_rate * error * data_array[i])
    return weights

#TODO: graph and gui to start/stop training maybe?
new_weights()
accuracy = read_accuracy()
num_predictions = int(accuracy[0].split('\t')[1])
num_correct = int(accuracy[1].split('\t')[1])
weights = read_weights()
pred_count = 0
#Main loop to train the weights
for i in range(1000):
    #1 is of the desired class, 0 is not of the desired class
    seed = random.randint(0,1)
    if seed == 1:
        root = rootTrue
    elif seed == 0:
        root = rootFalse
    filename = random.choice(os.listdir(root))
    data_array = get_data_point(filename, root)
    prediction = predict(data_array, weights)
    num_predictions += 1
    pred_count += 1
    if seed != prediction:
        #Train the weights for wrong answer
        weights = train_weights(data_array, weights, l_rate, 
                                num_predictions, num_correct, seed, prediction)
        if weights == None:
            break
    else:
        num_correct += 1
    if pred_count%10 == 0:
        print('Writing to file...')
        print('Accuracy: '+str(num_correct/num_predictions)+'%')
        write_to_file(weights, num_predictions, num_correct)
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