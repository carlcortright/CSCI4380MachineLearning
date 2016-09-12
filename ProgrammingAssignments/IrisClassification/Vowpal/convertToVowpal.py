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

# Open the relevant files
vowpal_output = open("vowpal.iris.test.data.vw", "r+")
iris = open("iris.test.data", "rt")
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
    new_data_entry += str(label) + " |"
    new_data_entry += " SepalLength:" + str(row[0])
    new_data_entry += " SepalWidth:" + str(row[1])
    new_data_entry += " PedalLength:" + str(row[2])
    new_data_entry += " PedalWidth:" + str(row[3])
    new_data_entry += "\n"
    data_entries.append(new_data_entry)

random.shuffle(data_entries)
for entry in data_entries:
    vowpal_output.write(entry)


iris.close()
vowpal_output.close()
