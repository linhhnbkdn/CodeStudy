# import the necessary packages
from __future__ import print_function
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from sklearn import datasets
from skimage import exposure
import numpy as np
import cv2
from sklearn.model_selection import train_test_split

minist = datasets.load_digits()

trainData, testData, trainLabels, testLabels = train_test_split(np.array(minist.data), minist.target, test_size=0.25, random_state=42)

trainData, valData, trainLabels, valLabels = train_test_split(trainData, trainLabels, test_size=0.1, random_state=42)

print('training data points: {}'.format(len(trainData)))
print('validation data points: {}'.format(len(valData)))
print('testing data points: {}'.format(len(testData)))

kVals = range(1, 30, 2)
accurancies = list()

for k in range(1, 30, 2):
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(trainData, trainLabels)
    score = model.score(valData, valLabels)
    print("k = %d, accurancy=%.2f%%"%(k, score*100))
    accurancies.append(score)

# find the value of k that has the largest accuracy
i = int(np.argmax(accurancies))
print("k=%d achieved highest accuracy of %.2f%% on validation data"
        %(kVals[i], accurancies[i] * 100))

model = KNeighborsClassifier(n_neighbors=kVals[i])
model.fit(trainData, trainLabels)
predictions = model.predict(testData)

print('EVALUATION ON TESTING DATA')
print(classification_report(testLabels, predictions))

