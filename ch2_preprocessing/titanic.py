from typing import List, Union, Tuple

from numpy import *

from scipy import *


def cabin_features(data: 'ndarray[str]') -> List[Tuple[str, int, int]]:
    """This takes in cabin details from the titanic data set and converts it into the list of features: cabin section,
        first cabin number, number of cabins

    Args:
        data: The cabin data array.

    Returns:
        features: The feature list.
    """
    features = []
    for cabin in data:
        cabins = cabin.split(" ")  # Get the list of cabins for this person (space separated)
        n_cabins = len(cabins)  # Get the number of cabins for this person
        # First char is the cabin_char
        try:
            cabin_char = cabins[0][0] # Assume that all cabins have the same section (Letter) which prefixes the cabins themselves
        except IndexError:
            # Could not retrieve the info so we mark it with X and we can assume there are no cabins associated to this person
            cabin_char = "X"
            n_cabins = 0
        # The rest is the cabin number
        try:
            cabin_num = int(cabins[0][1:])  # Parses the first cabin number by removing the section letter
        except:
            cabin_num = -1  # Could not read so we can set it to -1
        # Add 3 features for each passenger
        features.append([cabin_char, cabin_num, n_cabins])
    return features

if __name__ == "__main__":
    print(cabin_features(array(["C65", "", "E36", "C54", "B57 B59 B63 B66"])))
