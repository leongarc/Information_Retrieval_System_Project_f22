from hashdict import *
from abstract import *
from restaurant import Restaurant
import csv

class RestaurantCatalogHashDict(RestaurantAbstract):
  
  def __init(self):
    self.__list_restaurant = HTDict()
