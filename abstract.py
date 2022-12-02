from abc import abstractmethod
from abc import ABC

##Abstract class - Zachary Malloy/Leo Garcia
class RestaurantAbstract(ABC):

    @abstractmethod
    def search_id(self, id):
        pass

    @abstractmethod
    def search_name(self, name):
        pass

    @abstractmethod
    def search_address(self, address):
        pass

    @abstractmethod
    def search_category(self, category):
        pass

    @abstractmethod
    def restaurant_info(self, restaurant_file):
        pass

# DictAbstract class - Leo Garcia
class DictAbstract(ABC):
    
    @abstractmethod
    def __len__(self):
        pass

    @abstractmethod
    def __contains__(self, key):
        pass

    @abstractmethod
    def __getitem__(self, key):
        pass

    @abstractmethod
    def __setitem__(self, key, value):
        pass
  
    @abstractmethod
    def pop(self, key):
        pass
