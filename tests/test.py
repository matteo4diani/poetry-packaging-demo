"""This module contains tests.
"""
import unittest
import numpy as np

from poetry_packaging_demo import for_each

class Test(unittest.TestCase):
    """Base Class for all test functions."""
    def test_for_each(self):
        """Test function."""
        array = np.asarray([1, 2, 3])
        for_each(array, lambda v, i, list: print(i, v))