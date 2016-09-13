################################################################################
# A simple script to convert the iris training data to the vowpal wabbit format.
#
# Author: Carl Cortright
# Date: 9/10/2016
#
# Copyright 2016 Carl Cortright
################################################################################
import csv
import random
import sys

#
# Converts a file to the vowpal format
#
def convertToVowpal(filename):

    # Open the relevant files
    iris = open(filename, "r+")
    iris_csv = csv.reader(iris, delimiter=",")

    data_entries = []

    # Add the data to the vowpal_output file in the correct format
    for row in iris_csv:
        label = 0
        if(row[4] == "Iris-setosa"):
            label = 1
        elif(row[4] == "Iris-versicolor"):
            label = 2
        elif(row[4] == "Iris-virginica"):
            label = 3
        # Generate the data entry
        new_data_entry = ""
        new_data_entry += str(label) + " | "
        new_data_entry += str(row[0]) + ":1 "
        new_data_entry += str(row[1]) + ":1 "
        new_data_entry += str(row[2]) + ":1 "
        new_data_entry += str(row[3]) + ":1 "
        new_data_entry += "\n"
        data_entries.append(new_data_entry)

    random.shuffle(data_entries)
    for entry in data_entries:
        iris.write(entry)

    iris.close()

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

shuffleData(int(sys.argv[1]), int(sys.argv[2]))
