################################################################################
# Basic Script for training, testing, and assesing the  VW model.
#
# Author: Carl Cortright
# Date: 9/11/2016
#
# Copyright 2016 Carl Cortright
################################################################################

# Randomize the dataset

# Train the model
echo "Training vw model..."
rm iris.model
rm predictions.txt
vw -f iris.model --passes=10 --cache_file=iris.cache --kill_cache  --oaa 3 --loss_function=hinge < iris.training.data

# Test the model
echo
echo
echo "Testing model..."
vw -i iris.model --cache_file=test.cache -t -p ./predictions.txt < iris.test.data

# Calculate the accuracy of the model
echo
echo
echo "Calculating Accuracy..."
python calcAccuracy.py iris.test.data predictions.txt
