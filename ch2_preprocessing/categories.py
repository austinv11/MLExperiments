from typing import List

from numpy import *

from scipy import *


def categories_to_numbers(data: ndarray) -> List['ndarray[int]']:
    """Takes a list of discrete categories and converts them into numerical binary feature arrays.
        NOTE: This is unnecessary for certain algorithms which can accept categorical data.

    Args:
        data: The discrete data.

    Returns:
        features: The features list containing binary (1=True, 0=False) representations of the data.
            i.e. [1, 2, 3, 2, 1] -> [[1, 0, 0, 0, 1], [0, 1, 0, 1, 0], [0, 0, 1, 0, 0]]
    """
    categories = unique(data)  # Determines the categories by looking for all the unique values
    features = []
    for cat in categories:
        binary = equal(cat, data)  # Categories is a special type such that doing this will populate an array with boolean values for each element
        features.append(binary.astype("int"))  # Converts the booleans to ints.
    return features

if __name__ == "__main__":
    print(categories_to_numbers(array([1, 2, 3, 1, 2])))
