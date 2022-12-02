# by Leo Garcia
from dictionary_ll import *
from abstract import *
from restaurant import Restaurant
import csv
import random

class RestaurantCatalogLLDict(RestaurantAbstract):
  def __init__(self):
    self.__list_restaurant = LLDict()

  def search_id(self, id):
    if id in self.__list_restaurant: 
      return self.__list_restaurant[id]

  def restaurant_info(self, restaurant_file):
        with open(restaurant_file, 'r') as opened_restaurant_file:
            read_csv = csv.reader(opened_restaurant_file)

            for line in read_csv:
                restaurant = Restaurant()
                restaurant.set_id(line[0])
                restaurant.set_name(line[1])
                # Need to figure out how to add the complete address
                # Address, City, State, and Postal Code are in seperate columns
                # Note: Complete address goes from elements 2 through 5 respectively
                restaurant.set_address(line[2])
                restaurant.set_hour(line[10])
                restaurant.set_category(line[9])

                self.__list_restaurant[restaurant.get_id()] = restaurant

  
  def pop_restaurant(self, key):
    self.__list_restaurant.pop(key)
    
  def save_restaurant(self):
    with open('test24.csv', 'w+', newline = '') as file:
      write = csv.writer(file)
      for x in range(21):
        # rest = self.__list_restaurant[x]
        # convert rest into a list of 
        write.writerow(self.__list_restaurant[x])
        
  def add_restaurant(value):
      if self.search_id(key) == None:
        self.__list_restaurant._insert(key, value)
      
  def search_address(self, address):
    if address in  self.__list_restaurant:
      return self.__list_restaurant[address]
    
  def search_category(self, category):
    if category in self.__list_restaurant:
      return self.__list_restaurant[category]
    
  def search_name(self, name):
    if name in self.__list_restaurant:
      return self.__list_restaurant[name]
        