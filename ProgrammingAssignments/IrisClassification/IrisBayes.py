################################################################################
# A naive bayes classifier for classifying iris data.
#
# Author: Carl Cortright
# Date: 9/10/2016
#
################################################################################
import csv
import math

#
# Returns a dictionary of probabilities of a feature given a class in the form:
# {class:{(position, value): probability ... }...}
#
def getIrisModel(inFile):
    # Set up the CSV file
    iris_data = open(inFile, "rb")
    iris_data_csv = csv.reader(iris_data, delimiter=',')
    # Read the CSV file into a 3d dict
    iris_dict = {"Iris-setosa":{}, "Iris-versicolor":{}, "Iris-virginica":{}}
    for i, row in enumerate(iris_data_csv):
        if(row[4] == "Iris-setosa"):
            iris_dict["Iris-setosa"][i%50] = row[0:4]
        elif(row[4] == "Iris-virginica"):
            iris_dict["Iris-virginica"][i%50] = row[0:4]
        elif(row[4] == "Iris-versicolor"):
            iris_dict["Iris-versicolor"][i%50] = row[0:4]

    # Compute the conditional probabilities of feature x_i given C
    # Each entry is in the form of (position, value): probability
    feature_probabilities = {"Iris-setosa":{}, "Iris-versicolor":{}, "Iris-virginica":{}}
    for classification in iris_dict:
        for entry in iris_dict[classification].values():
            for i, value in enumerate(entry):
                if(not feature_probabilities[classification].has_key((i,value))):
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
    IRIS_SETOSA_P = float(1)/3
    IRIS_VERSICOLOR_P = float(1)/3
    IRIS_VIRGINICA_P = float(1)/3
    for i, f_i in enumerate(v):
        # Using log-space
        if(model["Iris-setosa"].has_key((i, f_i))):
            setosa_p += math.log(model["Iris-setosa"][(i, f_i)] + 1)
        if(model["Iris-versicolor"].has_key((i, f_i))):
            versicolor_p += math.log(model["Iris-versicolor"][(i, f_i)] + 1)
        if(model["Iris-virginica"].has_key((i, f_i))):
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
    test_data = open(test_data_file, "rb")
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
        else:
            print("Predicted: " + classify(entry, naive_bayes_model) + " Actual: " + entry[4])

    print("Accuracy=" + str(float(correct_count)/len(test_data_dict)))


calcAccuracy("iris.training.data", "iris.test.data")
