# CSC591-Project1
Neural Net - Machine Learning Project1
Project 1 - Implementation of Backpropagation
The goal of this project is to make you better understand the backpropagation.
You will ask to implement the sigmoid function and the backpropagation for a multilayer perceptron with sigmoid activations.
Recommend Environment
Python3
Numpy
Matplotlib
Dataset
Download MNIST dataset in this repository from here. Note that this has a different format as you used for the homework02, since we want to use the data loading functions in the code directly.
Assignment Description
1. Get the code
The incomplete code for this project can be found here. The code is modified from an online tutorial.
Read the code and make sure to understand what happened here.
2. Check the data
Change DATA_PATH in experiment/mlp.py to be the path where you put the MNIST data, then run
python mlp.py --input
If everything is correct, you will see the output shows 3,000 samples in training, 10,000 samples in validation and 10,000 samples in testing.

3. Implement the sigmoid function
Complete the implementation of the sigmoid function and derivative of sigmoid in src/activation.py.
sigmoid(z) returns the value of sigmoid function and sigmoid_prime(z) returns the value of derivative of sigmoid.
Test the sigmoid function
python mlp.py --sigmoid
If everything is correct, you will see the plot like this:



4. Implement the backpropagation
Follow the comments in src/bp.py to complete the implementation of backpropagation.
You do not have to exactly follow the comments. But make sure the function returns the correct format of data.
To make things easier, you can use a very small network to test your implementation by modifying the input here.
Use gradient check (ref1, ref2) to check whether your implementation is correct or not. Here we provide a simple implementation of gradient check for one of the weights and you can try it through:
python mlp.py --gradient
You can check other weights by changing the values of layer_id, unit_id and weight_id from here.
The detailed usage can be found here.
Please refer here for the interpretation of the result.
Note this is only a very simple implementation of gradient check and it is only for weights. You can implement your own version of gradient check as well and please let me know if you find any issues or bugs of this implementation.
5. Train the network
After finishing implementation of sigmoid function and backpropagation, you can train the network through:
python mlp.py --train
You will see something like this:



- You can play with the hyperparameters (number of layers, number of hidden units, learning rate ...) to get better results.
6. Record the learning curve and result on testing data
Record the learning curve for both training set and validation set during training
Test the trained model on testing set. There are implementations of save and load the model. You can utilize them for testing. But you may encounter some issues and have to fix them, since the original code is on Python2 and I did not test this part on Python3.
Deliverable
Source code
Report should includes (Use this template):
Show derivation of  \nabla_{a} L(\sigma(a)), where L is the binary cross entropy loss and sigma is the sigmoid function as mentioned in the lecture on Jan. 30;
Final structure of the network and other hyperparameters;
learning curve (loss and accuracy) on both training and validation set;
accuracy on testing set.
Put the source code, report and a name.csv file containing unityID of your group members in moodle as a zip folder named proj01.
Note
It should be easy to find the code online, but please try to do it by yourself.
Useful links:
http://cs231n.github.io/neural-networks-3/#sgd
