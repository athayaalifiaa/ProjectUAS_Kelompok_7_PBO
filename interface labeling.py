interfaces/labeling.py

from abc import ABC, abstractmethod

class ILabeling(ABC):
    @abstractmethod
    def label(self): pass