import tensorflow as tf
import os

model = tf.keras.models.load_model('/Users/morgandixon/Desktop/reviewd')
dir = '/Users/morgandixon/Desktop/Scraped-Conservative/All Conservative.txt'

file_list = []
for root,dirs,files in os.walk(dir):
    for name in files:
        print("Found file: "+str(name))
        file_list.append(os.path.join(root,name))

print("Found "+str(len(file_list))+" target files.")

input_data = []
for filepath in file_list:
    file = open(filepath,'r')
    try:
        text = file.read()
    except:
        continue
    input_data.append(text)
    file.close()

print("Finished extracting input data")
predictions = model.predict(input_data)

results = {
'0.9':0,
'0.8':0,
'0.7':0,
'0.6':0,
'0.5':0,
'0.4':0,
'0.3':0,
'0.2':0,
'0.1':0,
'0.0':0
}

for prediction in predictions:
    if(prediction[0] > 0.9):
        results['0.9'] += 1
    elif(prediction[0] > 0.8):
        results['0.8'] += 1
    elif(prediction[0] > 0.7):
        results['0.7'] += 1
    elif(prediction[0] > 0.6):
        results['0.6'] +=1
    elif(prediction[0] > 0.5):
        results['0.5'] += 1
    elif(prediction[0] > 0.4):
        results['0.4'] += 1
    elif(prediction[0] > 0.3):
        results['0.3'] += 1
    elif(prediction[0] > 0.2):
        results['0.2'] += 1
    elif(predictions[0] > 0.1):
        results['0.1'] += 1
    else:
        results['0.0'] += 1

print(results)
