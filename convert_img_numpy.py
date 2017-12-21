# convert image data into numpy array
import cv2
import numpy as np
from random import shuffle
from tqdm import tqdm
import os

TRAIN_DIR = os.path.join(os.path.expanduser('~'),
                                    'dev',
                                    'fabrics',
                                    'loch',
                                    'crop')


def create_train_data():
    training_data = []

    for img in tqdm(os.listdir(TRAIN_DIR)):
        path = os.path.join(TRAIN_DIR, img)
        img = cv2.imread(path,1);
        training_data.append(np.array(img))


    shuffle(training_data)
    np.save('train_data.npy', training_data)

    return training_data


training_data = np.load('train_data.npy')
print(training_data)
print(len(training_data))
train = training_data[:100]
test = training_data[-100:]
print(len(train))
print(len(test))
#cls = np.argmax([i[1] for i in train], axis=1)

#training_data = create_train_data()
#print(training_data[0])
#print(training_data[0].shape)
