# Homework 7
##### Student: Carl Cortright

### Part A)

1. The number of neurons in the hidden layer is usually somewhere between the number of nodes in the input layer and the number of nodes in the output layer. The best way to determine the absolute best is by trying a bunch of configurations and picking the one with the least error when generalized.

2. To prevent over fitting, L2 regularization is commonly used. Basically, this method prevents over fitting by penalizing large weights. This is different than linear classifiers where we normally penalize predictions with very high likelyhood.

3. Forward propagation data is propagated from the inputs through the network to produce an output. Then, while training, error is calculated and backpropagated back to the inputs to train the model.

4. The vanishing gradient problem only really happens in deep neural nets when there are lots of layers. The result is gradients that are computed by calculating derivatives by multiplying lots of small numbers together during backpropagation, and by the end, the gradient becomes very small, causing the first layers to train very slowly.

5. It's hard to understand what is happening. Might not be appropriate for the dataset. Training neural nets becomes more trial and error than anything else.

### Part B)

For both parts, it seems like the upper bound on accuracy for the neural network is the logistic model. On the iris dataset, with a train:test ratio of 2:1 I was able to get a maximum accuracy of around 93.5%, which is reasonable for our experience with this dataset. For the sports dataset, I a number much lower ~78%  accuracy. I think this is due to my training:testing ratio. For both models, after a while, the number of passes stops effecting the result. Interestingly for the iris dataset, I was able to get slightly better accuracy when I increased the number of hidden nodes to between 6-8, but then the accuracy significantly dropped off.
