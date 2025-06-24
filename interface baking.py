interfaces/baking.py

from abc import ABC, abstractmethod

class IBaking(ABC):
    @abstractmethod
    def bake(self): pass