interfaces/packaging.py

from abc import ABC, abstractmethod

class IPackaging(ABC):
    @abstractmethod
    def pack(self): pass