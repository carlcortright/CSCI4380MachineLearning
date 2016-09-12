################################################################################
# Simple script to calculate the accuracy of the iris-data vw model
#
# Author: Carl Cortright
# Date: 9/12/2016
#
# Copyright 2016 Carl Cortright
################################################################################
import math
import sys

actual = sys.argv[1]
predicted = sys.argv[2]

actual_file = open(actual, "r").readlines()
predicted_file = open(predicted, "r").readlines()

# Find all of the correct predictions
correct_predictions = 0
for line_num, act in enumerate(actual_file):
    actual_class = int(act[0])
    predicted_class = int(float(predicted_file[line_num][0:len(predicted_file[line_num])].rstrip()))
    if(actual_class == predicted_class):
        correct_predictions += 1

total_samples = len(actual_file)
accuracy = float(correct_predictions)/total_samples * 100
print("Accuracy = " + str(accuracy) + "%")
