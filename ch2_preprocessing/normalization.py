from typing import Tuple

from numpy import *

from scipy import *


def normalize_feature(data: ndarray, f_min: float = -1.0, f_max: float = 1.0) -> Tuple['ndarray[float]', float]:
    """Normalizes a feature array to be within a set min/max bounds.

    Args:
        data: The data to normalize.
        f_min: The minimum possible value of a feature.
        f_max: The maximum possible value of a feature.

    Returns:
        normalized, factor tuple: A tuple containing the normalized features and the factor that was applied to
            normalize the data.
    """
    d_min, d_max = min(data), max(data)
    factor = (f_max - f_min) / (d_max - d_min)
    normalized = f_min + (data - d_min)*factor
    return normalized, factor

if __name__ == "__main__":
    print(normalize_feature(array([1, 10, 0.5, 43, 0.12, 8])))
