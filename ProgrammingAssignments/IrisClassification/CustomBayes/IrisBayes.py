################################################################################
# A naive bayes classifier for classifying iris data.
#
# Author: Carl Cortright
# Date: 9/10/2016
# Updated: 9/12/2016
#
# Copyright 2016 Carl Cortright
################################################################################
import csv
import math
import random
import matplotlib.pyplot as plt
import numpy as np

#
# Returns a dictionary of probabilities of a feature given a class in the form:
# {class:{(position, value): probability ... }...}
#
def getIrisModel(inFile):
    # Set up the CSV file
    iris_data = open(inFile, "rt")
    iris_data_csv = csv.reader(iris_data, delimiter=',')
    # Read the CSV file into a 3d dict
    iris_dict = {"Iris-setosa":{}, "Iris-versicolor":{}, "Iris-virginica":{}}
    for i, row in enumerate(iris_data_csv):
        if(row[4] == "Iris-setosa"):
            iris_dict["Iris-setosa"][i] = row[0:4]
        elif(row[4] == "Iris-virginica"):
            iris_dict["Iris-virginica"][i] = row[0:4]
        elif(row[4] == "Iris-versicolor"):
            iris_dict["Iris-versicolor"][i] = row[0:4]

    iris_data.close()

    # Calculate all of the probabilities we need
    feature_probabilities = {"Iris-setosa":{}, "Iris-versicolor":{}, "Iris-virginica":{}}
    # Store the overall probability of a class
    NUM_ENTRIES = NUM_ENTRIES = len(iris_dict["Iris-setosa"]) + len(iris_dict["Iris-versicolor"]) + len(iris_dict["Iris-virginica"])
    feature_probabilities["Iris-setosa-p"] = float(len(iris_dict["Iris-setosa"]))/NUM_ENTRIES
    feature_probabilities["Iris-virginica-p"] = float(len(iris_dict["Iris-virginica"]))/NUM_ENTRIES
    feature_probabilities["Iris-versicolor-p"] = float(len(iris_dict["Iris-versicolor"]))/NUM_ENTRIES

    # Compute the conditional probabilities of feature x_i given C
    # Each entry is in the form of (position, value): probability
    for classification in iris_dict:
        for entry in iris_dict[classification].values():
            for i, value in enumerate(entry):
                if(not (i,value) in feature_probabilities[classification]):
                    feature_count = 0
                    for entry in iris_dict[classification].values():
                        if(entry[i] == value):
                            feature_count += 1
                    feature_probabilities[classification][(i,value)] = float(feature_count)/50

    return feature_probabilities

#
# Classify a given vector v based on the model.
# Returns the predicted classification.
#
def classify(v, model):
    # Probabilities of each class
    setosa_p = 0
    versicolor_p = 0
    virginica_p = 0
    # Probabilities of each class across the whole dataset
    IRIS_SETOSA_P = model["Iris-setosa-p"]
    IRIS_VERSICOLOR_P = model["Iris-versicolor-p"]
    IRIS_VIRGINICA_P = model["Iris-virginica-p"]
    for i, f_i in enumerate(v):
        # Using log-space
        if((i, f_i) in model["Iris-setosa"]):
            setosa_p += math.log(model["Iris-setosa"][(i, f_i)] + 1)
        if((i, f_i) in model["Iris-versicolor"]):
            versicolor_p += math.log(model["Iris-versicolor"][(i, f_i)] + 1)
        if((i, f_i) in model["Iris-virginica"]):
            virginica_p += math.log(model["Iris-virginica"][(i, f_i)] + 1)
    setosa_p *= IRIS_SETOSA_P
    versicolor_p *= IRIS_VERSICOLOR_P
    virginica_p *= IRIS_VIRGINICA_P
    probabilities = {setosa_p:"Iris-setosa", versicolor_p:"Iris-versicolor", virginica_p:"Iris-virginica"}
    return probabilities[max(probabilities)]

#
# Calculates the accuracy of the model
#
def calcAccuracy(training_data_file, test_data_file):
    naive_bayes_model = getIrisModel(training_data_file)
    test_data = open(test_data_file, "rt")
    test_data_csv = csv.reader(test_data, delimiter=",")
    test_data_dict = {}
    for i, row in enumerate(test_data_csv):
        test_vector = []
        for j in range(0,5):
            test_vector.append(row[j])
        test_data_dict[i] = test_vector

    correct_count = 0
    for entry in test_data_dict.values():
        if(classify(entry, naive_bayes_model) == entry[4]):
            correct_count += 1
    accuracy = float(correct_count)/len(test_data_dict)
    test_data.close()
    return accuracy

#
# Shuffles the dataset based on a ratio training:test
#
def shuffleData(training, test):
    iris_data = open("iris.data", "r+")
    iris_training = open("iris.training.data", "w")
    iris_test = open("iris.test.data", "w")

    all_data = iris_data.readlines()
    random.shuffle(all_data)
    all_data_len = len(all_data)


    split_point = int( all_data_len * ( float(training) / (training + test)))
    for i in range(0, split_point):
        iris_training.write(all_data[i])
    for j in range(split_point, all_data_len - 1):
        iris_test.write(all_data[j])

    iris_data.close()
    iris_training.close()
    iris_test.close()

#
# Calculates the accuracy distribution given an iris data file, returns dict
#
def calcAccuracyDist():
    ratio_max = 15
    accuracyDist = {}
    for ratio in range(1, ratio_max):
        total = 0
        tests = 5000
        for trial in range(0, tests):
            shuffleData(ratio, 1)
            total += calcAccuracy("iris.training.data", "iris.test.data")
        average = total/tests
        average = average * 100
        print("(" + str(ratio) + ":1) = " + str(average) + "%")
        accuracyDist[ratio] = average
    return accuracyDist


dist = calcAccuracyDist()

# Plot the Results
x = dist.keys()
y = dist.values()
plt.plot(np.unique(x), np.poly1d(np.polyfit(x, y, 4))(np.unique(x)), label="Best Fit Line")
plt.scatter(x,y)
plt.xlabel("Ratio")
plt.ylabel("% Accuracy")
plt.show()
