# Week6 Homework
##### Student: Carl Cortright

### Part A)

1. False - Instead of voting, the class with the highest probability is chosen
2. True - Error correcting codes always combine multiple classifiers to solve a multiclass problem
3. False - In all vs all each classifier votes using a standard voting method
4. False - All SVMs do is find a hyperplane to shatter the data. You could use the distance to the hyperplane as some type of probability, but it isn't inherently built in to the SVM design
5. True - Logistic regression is very similar to the perception in the way that is uses a weight vector (the beta values) and the features and sums them. The difference is how logistic regression updates it's betas and normalizes the values between 0 and 1.

### Part B)

1. To create models that can predict the verb in a sentence in verb final languages.
2.  This paper uses a discriminative linear classifier to do verb classification
3. A baseline is a benchmark to evaluate our model against. In this paper the baseline is human accuracy which is compared to the accuracy of the model.
4. One-vs-All
5. This is an interesting way of doing things. From what I can tell it is still using one-vs-all, but the confidence changes as the model "reads" the sentence, meaning that the occurrence of certain words increase the probability of a verb happening at the end of the sentence.
6. It is significantly better with accuracies between 25-40% compared to 3.7% and 6.05% respectively for humans.
7. The feature set is the sentence in either discriminative or n-gram form, and the hypothesis space are the verbs themselves.
8. The prior is p(v) and the posterior is p(c|v)
9. The paper mentions some examples where participants choose the wrong answer, but still ended up choosing an answer that was acceptable in their language. If there were enough of these examples, it is possible that the basis is being thrown off slightly. I couldn't find much more in the paper about how the basis might be a bad measure.
10. It means that the probability distribution of the verbs is best modeled with a zipfian distribution, which is a common power law like distribution for language models.

Extra Credit: Yes, while the classifiers are not directly comparable, it is reasonable to assume that the confidences of each classifier are roughly comparable. As each classifier gets more information, it should either become more or less confident in its guess. 
