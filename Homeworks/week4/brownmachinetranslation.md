Week 4 Assignment
--
Author: Carl Cortright
Date: 9/16/2016

Does this model accurately translate phrases longer than a single word?  Explain.

Yes, they were able to get an accuracy of 60% on sentences.

How is the Markov assumption being used in this paper?

In this paper, they are assuming, for a sequence of words:

p(s1, s2, ... , sn) = p(s1) x p(s2|s1) x ... x p(sn|s1,s2,...,sn-1)

This is a somewhat naive assumption, because it means they are assuming that s1, s2 ... sn are independent events. In reality, these events are somewhat dependent on each other. In practice, it works though.


They suggest that a trigram model would improve the performance of their system.  Why would this be?

They think that it will reduce the perplexity which is a measure of complexity, making the model easier to train.

What is the "generative story" of the translation model?  That is, how does the model suppose that translations are generated, and how does this relate to the noisy channel model?

The model assumes that the translations are generated using a random variable, which in this case would be the translators for the congress. This relates somewhat to a noisy channel model, because the translators themselves will include some error.  

What are the prior and posterior in the first equation, and what do they signify?

Prior - The sentence T
Posterior - The sentence S

What is the formula that describes the process of selecting the "best sentence" in section 4?

The algorithm is called "stack search" and what it does, is basically follow that looks like it is going to produce the highest probability. It only explores the possibilities that are producing fairly high probabilities.

What are the parameters in the translation model, and how are they estimated?

The probabilities of certain n-grams appearing. They are estimated using bayes rule.

What is a "distortion?"

When a word in a translation is "far away" from the word in the translated language that produced it.

What is an "alignment?"

The order in which words appear in different languages.

B.

Graphically, what effect does the bias term have on the logistic function in logistic regression?

I'm not totally sure, but I think that graphically, they move the prediction towards the point of highest probability on the function L.

Describe the difference(s) between stochastic gradient descent and gradient descent.

Gradient Descent - Approximates the gradient using all of the examples.

Stochastic Gradient Decent - Approximates the gradient using a randomly picked example.

Given a convex problem surface, what do we use to find the direction of steepest ascent?

The gradient vector

Which beta terms can be skipped during the update stage of logistic regression with SGD?

I think all of them still need to be updated. The gradient is going to be treated the same as in regular GD. 

I think all of the beta terms can be skipped

What are the elements of the gradient vector?

Partial derivatives with respect to the various dimensions.
