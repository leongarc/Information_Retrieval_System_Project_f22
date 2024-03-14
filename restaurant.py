#Constructor/Getter and Setters - Zachary
# Added remaining restaurant values
# city, state, postal code ,stars, and, review count with their respective setters and getters - Leo Garcia
#Class name
class Restaurant:
    #Constructor
    def __init__(self):
        self.__id = ""
        self.__name = ""
        self.__address = ""
        self.__city = ""
        self.__state = ""
        self.__postal_code = ""
        self.__stars = ""
        self.__hour = ""
        self.__category = ""

    #Get to set id
    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    #Get to set name
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    #Get to set address
    def get_address(self):
        return self.__address

    def set_address(self, address):
        self.__address = address

    # Get city
    def get_city(self):
        return self.__city

    # Set city
    def set_city(self, city):
        self.__city = city

    # Get state
    def get_state(self):
        return self.__state

    # Set state
    def set_state(self, state):
        self.__state = state

    # Get postal code
    def get_postal_code(self):
        return self.__postal_code

    # Set postal code
    def set_postal_code(self, postal_code):
        self.__postal_code = postal_code

    # Get stars
    def get_stars(self):
        return self.__stars

    # Set stars
    def set_stars(self, stars):
        self.__stars = stars

    #Get to set Category
    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    #Get to set hour
    def get_hour(self):
        return self.__hour

    def set_hour(self, hour):
        self.__hour = hour
  
    # Magic Method to quickly print restaurant information
    def __str__(self):

      line = "\nName: " + self.__name + "\nAddress: " + self.__address + "\nHours: " + self.__hour
      return line
