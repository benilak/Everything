import pandas as pd
import numpy as np
from random import uniform
from sklearn.preprocessing import normalize
from sklearn.model_selection import train_test_split
import math


class Node:
    def __init__(self, value=None, error=None, weights=None):
        """
        A class for a single node (within a particular layer) of a neural net.

        :param float value: the input value or activation value of the node, depending on the node type
        :param float error: the error value of the node
        :param list weights: a list of weights that are mapped to the node from the previous layer
        """

        self.value = value
        self.error = error
        self.weights = weights


class Layer:
    def __init__(self, nodes=None):
        """
        A class for a single layer of a neural net.

        :param list nodes: a list of the nodes within the layer
        """
        self.nodes = nodes


class NetModel:
    def __init__(self, data, targets, net):
        """
        A model for neural net learning, which can make predictions for the classification of given data.

        :param pd.DataFrame data: the testing data used to make predictions
        :param pd.Series targets: the testing targets used for determining the model's accuracy
        :param list net: a list of layers from the NetClassifier, which is a description of the neural net
        """

        self.data = data
        self.data.insert(0, 'Bias', [-1 for i in range(data.shape[0])])
        self.targets = targets
        self.net = net
        self.classes = self.targets.unique()
        self.classes.sort()
        self.predictions = []

    def check_accuracy(self):
        """
        Checks the accuracy of predicted values.

        :return string: a statement describing the accuracy of the model
        """

        correct = len([i for i, j in zip(self.predictions, self.targets) if i == j])
        accuracy = correct / len(self.targets)
        return "{}/{} correct - {:.1f}% accuracy".format(correct, len(self.targets), accuracy * 100)

    def predict(self):
        """
        Makes predictions for the testing data.
        The code itself is essentially just a subset of the training algorithm in the NetClassifier

        :return pd.Series: a series (to be consistent with the training targets) containing the predictions
        """

        # for each row in the data, iterate over each layer
        for r in range(self.data.shape[0]):

            # FEED FORWARD through each layer
            for i, layer in enumerate(self.net):
                # set values for the input nodes
                if i == 0:
                    for j, node in enumerate(layer.nodes):
                        node.value = self.data.iloc[r, j]
                # update values of the remaining nodes
                else:
                    for node in layer.nodes:
                        zipp = zip([node.value for node in self.net[i - 1].nodes], node.weights)
                        product = [j * k for j, k in zipp]
                        node.value = 1 / (1 + math.exp(-math.fsum(product)))

            prediction = self.classes[np.argmax([node.value for node in self.net[-1].nodes])]
            self.predictions.append(prediction)

        accuracy = self.check_accuracy()

        return self.predictions, accuracy


class NetClassifier:
    def __init__(self, data, targets, hidden_shape=None):
        """
        Establishes the base structure of the neural net that can be built using 'build_net()'.

        :param pd.DataFrame data: the training data used to build the net
        :param pd.Series targets: the training targets used to build the net
        :param list hidden_shape: a list containing the desired number of nodes for each hidden layer
        """

        # initialize the data
        self.data = data
        self.data.insert(0, 'Bias', [-1 for i in range(data.shape[0])])
        self.targets = targets
        self.classes = self.targets.unique()
        self.classes.sort()

        # build layers and nodes
        self.layers = [Layer() for i in (range(len(hidden_shape) + 2))]
        self.layers[0].nodes = [Node() for i in range(self.data.shape[1])]
        for i, number in enumerate(hidden_shape):
            self.layers[1 + i].nodes = [Node() for j in range(number)]
        self.layers[-1].nodes = [Node() for i in range(len(self.classes))]

        # initialize weights between the nodes
        for i, layer in enumerate(self.layers):
            # the input layer's nodes have no incoming weights
            if i == 0:
                pass
            else:
                for node in layer.nodes:
                    node.weights = [uniform(-1/math.sqrt(len(layer.nodes)), 1/math.sqrt(len(layer.nodes)))
                                    for n in range(len(self.layers[i - 1].nodes))]

    def build_net(self, rate=0.2, cycles=1000):
        """
        Builds the neural net.

        :param float rate: the learning rate used in this algorithm
        :param int cycles: the number of times to iterate over the entire data set
        :return:
        """

        # run the algorithm over the entire data set many times
        for cycle in range(cycles):
            # for each row in the data, iterate over each layer
            for r in range(self.data.shape[0]):

                # FEED FORWARD through each layer
                for i, layer in enumerate(self.layers):
                    # set values for the input nodes
                    if i == 0:
                        for j, node in enumerate(layer.nodes):
                            node.value = self.data.iloc[r, j]
                    # update values of the remaining nodes
                    else:
                        for node in layer.nodes:
                            values = [node.value for node in self.layers[i - 1].nodes]
                            zipp = zip(values, node.weights)
                            product = [j * k for j, k in zipp]
                            node.value = 1 / (1 + math.exp(-math.fsum(product)))

            # PROPAGATE BACK through each layer
            # TODO: write algorithm to update weights and errors after feed-forward

        # after training, the neural net to be tested on is fully described by the list of layers,
        # because it contains the net structure and the weights of each node
        return self.layers


iris = pd.read_csv('iris.txt')
trash, iris_data, iris_targets = np.hsplit(iris, [1, 5])
iris_data = pd.DataFrame(normalize(iris_data))
iris_targets = iris_targets.iloc[:, 0]
data_train, data_test, targets_train, targets_test = \
    train_test_split(iris_data, iris_targets, train_size=2/3, test_size=1/3)

classifier = NetClassifier(data_train, targets_train, [2, 3, 2])
neuralnet = classifier.build_net()
model = NetModel(data_test, targets_test, neuralnet)
model.predict()
print(model.check_accuracy())
