from restaurant import Restaurant
import csv
import uuid
from abstract import *


#class name for csv inventory - Zachary Malloy
class RestaurantCatalog(RestaurantAbstract):

    def __init__(self):
        self.__list_restaurant = []

    def search_id(self, id):
        for restaurant in self.__list_restaurant:
            if restaurant.get_id() == id:
                return restaurant
        return None

    def search_name(self, name):
        for restaurant in self.__list_restaurant:
            if restaurant.get_name() == name:
                return restaurant
        return None

    def search_address(self, address):
        for restaurant in self.__list_restaurant:
            if restaurant.get_address() == address:
                return restaurant
        return None

    def search_category(self, category):
        for restaurant in self.__list_restaurant:
            if restaurant.get_category() == category:
                return restaurant
        return None

    # Restaurant_info - Leo Garcia
    # This function opens and sets restaurant information

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

                self.__list_restaurant.append(restaurant)

    # buisness_id_genarator - Leo Garcia
    # Creates new unique buisness ID
    def buisness_id_generator(self):
        id = uuid.uuid4()
        # Check to see if it's existing
        if (self.search_id(id) == None):
            return id
        else:
            self.buisness_id_generator()

    # edit_buisness - Leo Garcia
    # Be able to change any values for existing restaurants
    def edit_buisness(self, id):
        edit_restaurant = self.search_id(id)
        if restaurant == None:
          return False
        edit_restaurant.set_name()
        edit_restaurant.set_address()
        edit_restaurant.set_city()
        edit_restaurant.set_state()
        edit_restaurant.set_postal_code()
        edit_restaurant.set_stars()
        edit_restaurant.set_review_count()
        edit_restaurant.set_category()
        edit_restaurant.set_hour()
        return edit_restaurant

    # add_restaurant - Leo Garcia
    # Adds new buisness into list
    def add_restaurant(self,new_restaurant):
        name = new_restaurant[0]
        address = new_restaurant[1]
        city = new_restaurant[2]
        state = new_restaurant[3]
        postal_code = new_restaurant[4]
        stars = new_restaurant[5]
        review_count = new_restaurant[6]
        hour = new_restaurant[7]
        category = new_restaurant[8]

        try:
            restaurant = Restaurant()
            restaurant.set_id(self.buisness_id_generator())
            restaurant.set_name(name)
            restaurant.set_address(address)
            restaurant.set_city(city)
            restaurant.set_state(state)
            restaurant.set_postal_code(int(postal_code))
            restaurant.set_stars(int(stars))
            restaurant.set_review_count(int(review_count))
            restaurant.set_hour(hour)
            restaurant.set_category(category)
            self.__list_restaurant.append(restaurant)

        except ValueError:
            print(
                "Please enter only whole values for postal code, stars, and review count"
            )

    # save_restaurant_changes - Leo Garcia
    # Any changes done to list and saves into disk
    def save_restaurant_changes(self, filename):
        try:
            with open(filename, 'w', newline='') as file:
                headers = [
                    'buisness_id', 'name', 'address', 'city', 'state',
                    'postal_code', 'stars', 'review_count', 'attributes',
                    'categories', 'hours'
                ]
                writer = csv.writer(file)
                writer.writeheader(headers)

                for line in self.__list_restaurant:
                    restaurant = Restaurant()
                    writer.writerow([
                        restaurant.get_id, restaurant.get_name,
                        restaurant.get_address, restaurant.get_city,
                        restaurant.get_state, restaurant.postal_code,
                        restaurant.get_stars, restaurant.get_review_count,
                        restaurant.attributes, restaurant.get_categories,
                        restaurant.get_hour
                    ])
        except BaseException as e:
            print("BaseException:", filename)
        else:
            print("Save Sucessful")
