from msdict import *
from restaurant_catalog_lldict import RestaurantCatalogLLDict

class RestaurantCatalogSLDict(RestaurantCatalogLLDict):
  def __init__(self):
    self.__list_restaurant = MSDict()