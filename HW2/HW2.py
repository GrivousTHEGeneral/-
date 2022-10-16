import numpy as np
import json

def Triangle(stars_num):
    """ Draws an isosceles triangle using asterisks
        :param:
        - stars_num (int) number of stars to the left and right of the center star on the underside"""
    
    space_num = stars_num

    while space_num >= 0:
        print( " " * space_num + "*" * (stars_num - space_num) + "*" + "*" * (stars_num - space_num) + " " * space_num)
        space_num -= 1
    return None

def HistDistanve(hist1, hist2) -> float:
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
    """ Save data to json file
        :param:
        - filename (string) name of the file
        - data (list) write data"""

    with open(f"{filename}"+".json", 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    return "Data written successfully!\n"

def ReadFile(filename):
    """ Load data from json file
            :param:
            - filename (string) name of the file"""

    with open(f"{filename}"+".json") as f:
        data_read = json.load(f)
    return data_read