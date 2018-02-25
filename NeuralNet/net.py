import pandas as pd
import numpy as np


class Node:
    def __init__(self, value=None, error=None, weights=None):
        """
        A class for a single node (within a particular layer) of a neural net.

        :param float value: the input value or activation value of the node, depending on the node type
        :param float error: the error value of the node
        :param list weights: a list of weights from this node to the other nodes in the next layer
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


x = [Node() for i in range(3)]
y = [0, 10, 20]

for i, node in enumerate(x):
    node.value = y[i]
    print(node.value)

hidden_shape = [2, 3, 2]
layers = [Layer() for i in (range(len(hidden_shape) + 2))]

for i, number in enumerate(hidden_shape):
    layers[1 + i].nodes = [Node() for j in range(number)]

print(layers)

# initialize weights between the nodes
for i, layer in enumerate(self.layers):
    # the input layer's nodes have no incoming weights
    if i == 0:
        pass
    # #EDITED#: changed the definition of weights -- keeping code here in case things go wrong
    # this layer's nodes map weights to all nodes in the next layer since the output layer has no bias node
    # elif i == len(self.layers) - 2:
    #     for node in layer.nodes:
    #         node.weights = [uniform(-1/math.sqrt(len(layer.nodes)), 1/math.sqrt(len(layer.nodes)))
    #                         for n in range(len(self.layers[i + 1].nodes))]
    # for layers preceding the last two, nodes will not have a weight mapped to the bias node
    else:
        for node in layer.nodes:
            node.weights = [uniform(-1 / math.sqrt(len(layer.nodes)), 1 / math.sqrt(len(layer.nodes)))
                            for n in range(len(self.layers[i - 1].nodes))]

# #NOTE#: a different format of the for-loops above; will test efficiency/functionality
# #NOTE#: follows previous definition of weights (mapped to next nodes, not from previous nodes)
# # initialize weights between the nodes
# for i, layer in enumerate(self.layers):
#     for node in layer.nodes:
#         # the output layer's nodes have no outgoing weights
#         if i == len(self.layers) - 1:
#             break
#         # this layer's nodes map weights to all nodes in the next layer since the output layer has no bias node
#         elif i == len(self.layers) - 2:
#             node.weights = [uniform(-1 / math.sqrt(len(layer.nodes)), 1 / math.sqrt(len(layer.nodes)))
#                             for n in range(len(self.layers[i + 1].nodes))]
#         # for layers preceding the last two, nodes will not have a weight mapped to the bias node
#         else:
#             node.weights = [uniform(-1 / math.sqrt(len(layer.nodes)), 1 / math.sqrt(len(layer.nodes)))
#                             for n in range(len(self.layers[i + 1].nodes) - 1)]