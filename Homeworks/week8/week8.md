# Homework 8
##### Student: Carl Cortright
##### Date: 10/23/2016

1. The actions the RL algorithm can use are wait, commit, next word which takes a predicted next word and produces an updated translation, and verb which predicts the final verb
2. Figure 5 shows that none of the algorithms used decide to take the action of predicting the final verb often, meaning that predicting the final verb is not very accurate
3. A classifier is used when learning the policy for taking an action, where the loss represents the quality of the action to be taken.
4. The features were designed so that the system would generalize. There were three main types of features, input, prediction and translation features. The labels were actions.
5. The reward is the accuracy of the translation in porportion to the amount of the sentence revealed.
6. The updated policy is the policy at the current iteration plus a step in the direction of the optimal policy.
7. The cost of an action with a given feature vector is the reward gained by the optimal solution minus the reward gained by taking the action a_t 
8. The German-English parallel corpus "de-news" was used to form a baseline and also to train the model.
9. A dynamic programming algorithm was used to generate an oracle policy pi*.
10. The policy is a classifier that chooses one of the actions to either wait, commit, predict the next word, or predict the final verb.
11. The input to the policy is a feature vector that gives the input sentence, possible translations, and the accuracy of those possible translations.
