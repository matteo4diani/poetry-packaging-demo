from typing import Callable
from numpy import ndarray;

def for_each(list: ndarray, function: Callable[[any, int, ndarray], None]):
    for i, v in enumerate(list):
        function(v, i, list)
        
def log(message: str):
    print(message)
    
def say_hello(name: str):
    #print(f'Hello {name}!')
    pass