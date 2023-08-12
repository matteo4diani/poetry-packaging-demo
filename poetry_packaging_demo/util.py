from typing import Callable
from numpy import ndarray;

def for_each(list: ndarray, function: Callable[[any, int, ndarray], None]):
    for i, v in enumerate(list):
        function(v, i, list)