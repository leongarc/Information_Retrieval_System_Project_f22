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
                restaurant.set_address(line[2])
                restaurant.set_postal_code(line[3])
                restaurant.set_stars(line[4])
                restaurant.set_category(line[6])
                restaurant.set_hour(line[7])

                self.__list_restaurant[restaurant.get_id()] = restaurant

    def pop_restaurant(self, key):
        self.__list_restaurant.pop(key)

    def save_restaurant(self):
        fields = [
            'business_id', 'name', 'address', 'city', 'state', 'postal_code',
            'stars', 'review_count', 'attributes', 'categories', 'hours'
        ]
        with open('test24.csv', 'w+', newline='') as file:
            write = csv.writer(file)
        
            rest = self.__list_restaurant
                # convert rest into a list of
            write.writerow(fields)
            write.writerows(rest.get_name())

    def add_restaurant(self, key, value):
        self.__list_restaurant._insert(key, value)

    def search_address(self, address):
        if address in self.__list_restaurant:
            return self.__list_restaurant[address]

    def search_category(self, category):
        if category in self.__list_restaurant:
            return self.__list_restaurant[category]

    def search_name(self, name):
        if name in self.__list_restaurant:
            return self.__list_restaurant[name]

    def __str__(self):
        return str(self.__list_restaurant)

    def __len__(self):
        return len(self.__list_restaurant)

    def __contains__(self, key):
        return key in self.__list_restaurant
