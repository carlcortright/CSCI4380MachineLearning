# A review of *Learning to Detect Malicious Executables in the Wild* by Jeremy Z. Kolter and Marcus A. Maloof

#### Student: Carl Cortright

##### Part a)

In this study, the authors of the paper uses a variety of techniques, including naive bayes, instance based learners, TFIDF classifiers, support vector machines, and decision trees, to classify malicious executables. The were able to collect data on a variety of executables, including trojan horses, worms, and viruses. They then broke down the executable into 4-byte n-grams where each 4-byte sequence represented a feature. One of the techniques they used to settle on the 4-byte sequence size was small-batch experimentation. They then picked out the 500 most important features based on the information gain of each feature (defined in the paper) to use as in their model.

One of the cool things about this paper is that they decided to use multiple machine learning techniques and then pick the best one. They were able to use true experimentation instead of hand-wavy explanations to show why something worked, and in the end, they came up with a really good model for detecting viruses. I think it would be interesting if an anti-virus company like Norton were to implement something like this with some type of online learning algorithm, constantly keeping an update of what viruses are out there, leaving their users with only the most robust systems.


##### Part B)

###### 1.

A relevant feature is a feature that is highly related to a class. For example, if the n-gram 0011aaff showed up in 90% of the malicious executables, then we know it is important. In the paper they used a information gain function (ig) to determine how relevancy of a feature.

###### 2.

Yes they still have relevant meanings. In a multiclass example, a FP would be falsely identifying a class and a TP would be correctly identifying a class. We could even base the performance of the model on some equation based on the sum of the errors or the largest error if we want our model to be very error free.

###### 2a.

In this case, we care more about recall. We care more about getting all the viruses than we do about misclassifying a good program as a virus.

###### 2b.

A case where we would care more about precision would be something like a program that controlled the United States nuclear arsenal (think wargames) . In this example we would want the program to be precise as possible, only launching when we are attacked and not launching when we are in peacetime.

###### 2c.

ff00ab3e

###### 2d.

The feature space is all possible 4-byte n-grams that show up in the executables. The labels are virus and not virus.

###### 2e.

The support vector machine and what a hyperplane is.

###### 2f.

No, naive bayes is a good method but not always the best. I had a feeling that they would get pretty good accuracy.

###### 2g.

Its like entropy because it measures the distribution of the class, but it also measures the distribution of the features, allowing us to judge which features are most important.

###### 2h.

I'm not totally sure, but I think the prior is p(v_i, C) and it is calculated by taking the number of times v_i shows up in C and dividing it by the C.

###### 2i.

The *argmax* function returns the **class** with the highest probability. The *max* function would return the highest probability itself.  

###### 2j.

The relative performance changed based on the collection size.

###### 2k.

It is important that we spit the tree so it most accurately classifies the data. Most of the time, a *gain ratio* is used to obtain attribute selection. This gain ratio is related to the information gain function disused earlier in the paper.

The *gain ratio* is the measure of the difference between the models value and the expected value. A *KL-difference* measures the sum of the *gain ratio* over the entire dataset.

I'm not totally sure, but I think that it could be used as a measure of the difference between the entropy of the model and the entropy of the dataset itself.

##### Loss Function Definition (naive bayes)

The loss function in naive bayes is a measure of the cost of making an error. It is the sum of a the probabilities of a class being a TP given a new peice of data x* .

##### Zero Probabilities in Logistic Regression

Zero probabilities in logistic regression are not a problem, because the probability of a class given a feature vector is based on the logistic function, which by definition cannot be zero. 
