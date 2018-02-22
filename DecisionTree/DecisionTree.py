"""
CS450 - Machine Learning
Implementation of a decision tree classifier and model
(Incomplete: not yet fully functional; needs debugging)
"""

import pandas as pd
import numpy as np
from sklearn import datasets
from sklearn.model_selection import train_test_split
from scipy import stats
from copy import deepcopy


class DTmodel:
    def __init__(self, data_test, targets_test):
        self.data_test = data_test
        self.targets_test = targets_test

    def find_leaf(self, row, tree):
        for child in tree.children:
            if row[tree.name] == child:
                if tree.children[child].children == 'LEAF':
                    return tree.children[child].name
                else:
                    subtree = tree.children[child]
                    name = self.find_leaf(row, subtree)
                    if isinstance(name, str):
                        return name

    def predict(self, tree):
        predictions = []
        for ix, row in enumerate(self.data_test):
            prediction = self.find_leaf(row, tree)
            predictions.append(prediction)
        return predictions


class Node:
    def __init__(self):
        self.name = ""
        self.children = {}


# assumes data is in the form of a numpy array
class DTclassifier:
    def __init__(self, data=None, targets=None, data_train=None, data_test=None, targets_train=None, targets_test=None, header=False):
        self.data = data
        self.targets = targets
        self.data_train = data_train
        self.data_test = data_test
        self.targets_train = targets_train
        self.targets_test = targets_test
        # if header is TRUE this stores the column names
        # stores the remainder of the data without the header in self.data
        if header:
            self.header = data[0,:]
            self.data = data[1:,:]

    def set_header(self, header):
        if isinstance(header, list):
            self.header = header
        else:
            print("<header> must be a list")

    def feature_name(self, feature):
        if self.header == None:
            return feature
        else:
            return self.header[feature]

    # separates data from target values if needed
    def sep_data_targets(self, target_column):
        if isinstance(target_column, str):
            index = np.nonzero(self.header == target_column)[0][0]
            self.targets = self.targets[:,index]
            self.data = np.delete(self.data, index, axis=1)
        elif isinstance(target_column, int):
            self.targets = self.data[:, target_column]
            self.data = np.delete(self.data, target_column, axis=1)
        else:
            print("<target_column> must be a string or an integer")

    # splits training and test data if needed
    def train_test_split(self, train_size=.7):
        self.data_train, self.data_test, self.targets_train, self.targets_test = \
            train_test_split(self.data, self.targets, train_size=train_size, test_size=1-train_size)

    def calc_entropy(self, set, targets=None):
        if hasattr(targets, '__iter__') == False:
            targets = self.targets_train

        # feature_types are the values a feature can assume
        feature_types, totals = np.unique(set, return_counts=True)

        # the classes are the values the target feature can assume
        classes = np.unique(targets)

        # this array will be filled in with the counts for each class per feature type
        # where the row is feature type, and column is the class
        ntypes = np.zeros(shape=(len(feature_types), len(classes)), dtype=int)

        # this iterates through the data and fills in the 'ntypes' array with the appropriate counts
        for ix1, f_type in enumerate(feature_types):
            for ix2, c_type in enumerate(classes):
                ntypes[ix1, ix2] = np.count_nonzero((set == f_type) & (targets == c_type))

        entropy = 0
        for ix1, f_type in enumerate(ntypes):

            # the inner loop calculates the entropy of each type (t_entropy)
            t_entropy = 0
            for ix2, count in enumerate(f_type):
                t_entropy -= 0 if count == 0 else count / totals[ix2] * np.log2(count / totals[ix2])

            # this calculates the weighted average
            entropy += totals[ix1] / len(set) * t_entropy

        return entropy

    def build_node(self, set=None, targets=None, avail_features=None):

        current_node = Node()

        # this just makes sure that in the first iteration of build_node it is working with the original data/targets
        if hasattr(set, '__iter__') == False:
            set = self.data
        if hasattr(targets, '__iter__') == False:
            targets = self.targets_train

        # similarly, this makes sure in the 1st iteration we start with all of the features
        all_features = [feature for feature in range(np.size(set, axis=1))]
        if hasattr(avail_features, '__iter__') == False:
            avail_features = all_features[:]

        # these conditions break the recursion and return a LEAF node
        if avail_features == []:
            current_node.name = stats.mode(targets)[0][0]
            current_node.children = 'LEAF'
            return current_node
        if np.size(np.unique(targets)) == 1:
            current_node.name = np.unique(targets)[0]
            current_node.children = 'LEAF'
            return current_node
        if np.size(set) == 0:
            # if we arrive at an unknown branch because the data is scarce,
            # we set the leaf node to the most common target value
            current_node.name = stats.mode(self.targets_train)[0][0]
            current_node.children = 'LEAF'
            return current_node

        # removed features helps me keep track of the indices of the features,
        # since it is the index of the feature that is initially recorded in the node class
        removed_features = [x for x in all_features if x not in avail_features]
        entropies = []
        for ix, feature in enumerate(set.T):
            if ix in removed_features:
                entropies.append(float('inf'))
            else:
                entropies.append(self.calc_entropy(feature, targets))

        # chooses minimum entropy and sets node name to that feature
        feature = np.argmin(entropies)
        current_node.name = feature

        # subsets the data based on feature type and recursively calls the build_node function
        feature_types = np.unique(set[:,feature])
        for type in feature_types:
            available = avail_features[:]
            # if feature in avail_features:
            available.remove(feature)
            subset = set[set[:,feature] == type]
            sub_targets = targets[set[:,feature] == type]
            # at the end of each loop we set the parent node's children
            # to the node that was built in with the subsetted data
            node = self.build_node(subset, sub_targets, available)
            current_node.children[type] = deepcopy(node)

        # after iterating through each feature type, we return the node
        return current_node

    # attempts to provide a visual form of the tree (it's not very effective)
    def print_tree(self, tree, node_names):
        names = dict(zip([z for z in range(len(node_names))], node_names))
        print(names[tree.name])
        for child in tree.children:
            print(child)
            subtree = tree.children[child]
            if subtree.children == 'LEAF':
                print(subtree.name)
            else:
                self.print_tree(subtree, node_names)
