import numpy as np
import pandas as pd

def Triangle(stars_num):
    """ Draws an isosceles triangle using asterisks
        :param:
        - stars_num (int) number of stars to the left and right of the center star on the underside"""
    
    space_num = stars_num

    while space_num >= 0:
        print( " " * space_num + "*" * (stars_num - space_num) + "*" + "*" * (stars_num - space_num) + " " * space_num)
        space_num -= 1
    return None

def HistDistanse(hist1, hist2) -> float:
    """ Calculates the Euclidean metric between two histograms
    :param:
    - hist1 (list) first histogram
    - hist2 (list) second histogram"""

    hist1, hist2 = np.array(hist1,  dtype=float), np.array(hist2,  dtype=float)
    
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