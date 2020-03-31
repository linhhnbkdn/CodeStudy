# import the necessary packages
from __future__ import print_function
from sklearn.metrics import classification_report
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import fetch_lfw_people
from sklearn.model_selection import train_test_split

dataSet = fetch_lfw_people(min_faces_per_person=70)

trainData, testData, trainLabels, testLabels = train_test_split(dataSet.data, dataSet.target, test_size=0.25, random_state=42)
trainData, valData, trainLabels, valLabels = train_test_split(trainData, trainLabels, test_size=0.1, random_state=42)

print('[INFO]: Training model')
model = LogisticRegression(verbose=1, max_iter=1000, tol=1e-3)
model.fit(trainData, trainLabels)

score = model.score(valData, valLabels)
print('[INFO]: Accurancy on validation data: {}'.format(score))

predictions = model.predict(testData)
report = classification_report(testLabels, predictions, target_names=dataSet.target_names)
print(report)