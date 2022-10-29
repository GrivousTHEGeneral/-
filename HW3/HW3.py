import sys
import numpy as np
import pandas as pd


def HistDistanse(hist1, hist2) -> float:
    """ Calculates the Euclidean metric between two histograms
    :param:
    - hist1 (list) first histogram
    - hist2 (list) second histogram"""

    hist1, hist2 = np.array(hist1, dtype=float), np.array(hist2, dtype=float)

    if hist1.shape == hist2.shape:
        dist = np.linalg.norm(hist1 - hist2)
    else:
        return f"ValueError: Histogram shapes/sizes vary. {hist1.shape} != {hist2.shape}"

    return dist


def WriteFile(filename, data):
    """ Save data to file
        :param:
        - filename (string) name of the file
        - data (list) write data"""
    pd.DataFrame(data).to_csv(filename, header=None, sep=" ", index=None, mode='a')
    return "Data written successfully!\n"


def ReadFile(filename):
    """ Load data from file
            :param:
            - filename (string) name of the file"""
    data_read = pd.read_csv(filename, sep=" ", header=None)
    return data_read


class NNClassifier:
    """ Simple KNN Classifier.

                 :Attributes:
                     -n_neighbors (int) number of neighbors
    """

    def __init__(self, n_neighbors=5):
        self.n_neighbors= n_neighbors

    def read_data(self, filename):
        """ Read input data
                    :param:
                    - filename (string) the name of the file we want to read"""
        return np.array(ReadFile(filename))

    def predict(self, data, lables, target):
        """ Predict class of the target object
                            :param:
                            - data (narray) array of features
                            - labels (narray) array of class labels
                            - target (narray) target object to be classified"""

        distances = [(lables[i], HistDistanse(data[i], target)) for i in range(data.shape[0])]
        distances.sort(key=lambda elem: elem[1])

        neighbors = [distances[i][0] for i in range(self.n_neighbors)]
        
        count = {}
        for instance in neighbors:
            if instance in count:
                count[instance] += 1
            else:
                count[instance] = 1

        return max(count.items(), key=lambda x: x[1])[0]