from restaurant import Restaurant
from restaurant_catalog import RestaurantCatalog
from restaurant_catalog_lldict import RestaurantCatalogLLDict
from restaurant_catalog_sldict import RestaurantCatalogSLDict
from restaurant_catalog_hashdict import RestaurantCatalogHashDict
from simple_term_menu import TerminalMenu
import random


class MainFunctions:
    def magic_method_str_test():
      restaurant = RestaurantCatalogLLDict()
      restaurant.restaurant_info("restaurant_file.csv")
      print(str(restaurant))
      
    #resturant_class_test - Zachary
    #Test for class(restraurant.py)
    def class_test():
        #Creating object
        new_restaurant = Restaurant()
        #Inputting information from user
        id = input("Enter id:  ")
        name = input("Enter the name:  ")
        address = input("Enter address:  ")
        category = input("Enter category:  ")

        #Set
        new_restaurant.set_id(id)
        new_restaurant.set_name(name)
        new_restaurant.set_address(address)
        new_restaurant.set_category(category)

        #Print
        print("Here is the restaurant information: \n")
        print("Name: " + new_restaurant.get_id() + "," + "Id: " +
              new_restaurant.get_name() + "," + "Name: " +
              new_restaurant.get_address() + ","
              "Category: " + new_restaurant.get_category() + "\n")

    # restaurant_catalog_test - Leo Garcia
    # Test for opening and reading restaurant catalog
    def restaurant_catalog_test():
        restaurant = RestaurantCatalog()
        restaurant.restaurant_info("restaurant_file.csv")
        id = input("Enter unique ID: ")
        restaurant_info = restaurant.search_id(id)

        if restaurant_info == None:
            print("Restaurant not found, please try again\n")
            print("")
            MainFunctions.restaurant_catalog_test()
        else:
            print("Name: " + restaurant_info.get_name() + ", " + "Address: " +
                  restaurant_info.get_address() + ", " + "Hours: " +
                  restaurant_info.get_hour())

    # Restaurant catalog test LLDict version
    # Uses linked list dictionary - Leo Garcia
    def restaurant_catalog_test_lldict():
        restaurant = RestaurantCatalogLLDict()
        restaurant.restaurant_info("restaurant_file.csv")
        id = input("Enter unique ID: ")
        key = restaurant.search_id(id)
        if key == None:
            print("Restaurant not found, please try again\n")
            print("")
            MainFunctions.restaurant_catalog_test()
        else:
            print(key)

    #Zachary Malloy
    def restaurant_insert_test_lldict():
        restaurant = RestaurantCatalogLLDict()
        restaurant.restaurant_info("restaurant_file.csv")
        while True: # Generate unique buisness id/key - Leo
          id = random.randint(0,9999)
          key = restaurant.search_id(id)
          if key == None:
            key = id
            break
        # New restaurant object - Leo
        new_rest = Restaurant()
        new_rest.set_id(key)
        new_rest.set_name(input("Enter name of buisness: "))
        new_rest.set_address(input("Enter address: "))
        new_rest.set_hour(input("Enter hours of buisness: "))
        restaurant.add_restaurant(key, new_rest)
        
            
        # call add_restaurant function to test the insertion
  
        # you are going to ask the user for the restaurant information
        # take the information, create a restaurant object using this information and then
          
        # send that object to the add_restaruant function

    def restaurant_pop_test_lldict():
        restaurant_list = RestaurantCatalogLLDict()
        restaurant_list.restaurant_info("restaurant_file.csv")
        print("Number of restaurants: " ,len(restaurant_list))
        key = input("Enter ID of restaurant to delete: ")
        restaurant_list.pop_restaurant(key)
        print("Number of restaurants: " ,len(restaurant_list))
        

        # use the id as input to the delete_restaurant function to remove the restaurant
        '''
        key = restaurant_list.search_id(id)
        if key == None:
            print("Not found")
        else:
          print("Restaurant deleted")
          restaurant_list.pop_restaurant(key)
          print(restaurant_list)
        '''


      #Hash Table Function- Zachary

    def restaurant_catalog_test_htdict():
        restaurant = RestaurantCatalogHashDict()
        restaurant.restaurant_info("restaurant_file.csv")
        #print(len(restaurant))
        id = input("Enter Unique ID: ")
        key = restaurant.search_id(id)
        if key == None:
            print("Restaurant not found, please try again\n")
            print("")
            MainFunctions.restaurant_catalog_test_htdict()
        else:
            print(key)
        # restaurant_catalog_multisearch_test - Zachary Malloy
        # Test for opening and reading restaurant catalog through             different means
    def search():
        print("Enter a number to search via" + "\n1 for id" + "\n2 for name" +
              "\n3 for address" + "\n4 for catagories")
        #Allows user input
        userInput = int(input())
        #If Input 1, search by id
        if userInput == 1:
            restaurant = RestaurantCatalog()
            restaurant.restaurant_info("restaurant_file.csv")
            id = input("Enter unique ID: ")
            restaurant_info = restaurant.search_id(id)
            print("Name: " + restaurant_info.get_name() + ", " +
                  "\nAddress: " + restaurant_info.get_address() + ", " +
                  "\nHours: " + restaurant_info.get_hour())

        #If Input 2, search by name
        if userInput == 2:
            restaurant = RestaurantCatalog()
            restaurant.restaurant_info("restaurant_file.csv")
            name = input("Enter name: ")
            restaurant_info = restaurant.search_name(name)
            print("Name: " + restaurant_info.get_name() + ", " +
                  "\nAddress: " + restaurant_info.get_address() + ", " +
                  "\nHours: " + restaurant_info.get_hour())

        #If Input 3, search by address

        if userInput == 3:
            restaurant = RestaurantCatalog()
            restaurant.restaurant_info("restaurant_file.csv")
            address = input("Enter Andress: ")
            restaurant_info = restaurant.search_address(address)
            print("Name: " + restaurant_info.get_name() + ", " +
                  "\nAddress: " + restaurant_info.get_address() + ", " +
                  "\nHours: " + restaurant_info.get_hour())

        #If Input 4, search by category
        if userInput == 4:
            restaurant = RestaurantCatalog()
            restaurant.restaurant_info("restaurant_file.csv")
            category = input("Enter Catagories: ")
            restaurant_info = restaurant.search_category(category)
            print("Name: " + restaurant_info.get_name() + ", " +
                  "\nAddress: " + restaurant_info.get_address() + ", " +
                  "\nHours: " + restaurant_info.get_hour())

    # add_restaurant_test - Leo Garcia
    # Tests to add new restaurant to database
    def add_restaurant_test():
        count = 0
        new_restaurant = []
        fields = [
            'Name: ', 'Address: ', 'City: ', 'State: ', 'Postal Code: ',
            'Stars: ', 'Review Count: ', 'Attributes: ', 'Categories: ',
            'Hours: '
        ]
        print("Edit Restuarnt information")
        for field in fields:
            new_restaurant.append(input(fields[count]))
            count += 1
        restaurant = RestaurantCatalog()
        restaurant.add_restaurant(new_restaurant)

    # edit_restaurant_test - Leo Garcia
    # Be able to edit existing restaurant
    def edit_restaurant_test():
        pass

    #terminal_menu_test
    #Terminal functions - Zachary Malloy
    #Terminal functions to be able to use arrow keys from simple_term_menu
    def terminal_search():
        options = [
            "Search via id", "Search via name", "Search via address",
            "Search via catagory", "Add restaurant", "Edit restaurant"
        ]
        terminal_menu = TerminalMenu(options)
        menu_entry_index = terminal_menu.show()

        if menu_entry_index == 0:
            restaurant = RestaurantCatalog()
            restaurant.restaurant_info("restaurant_file.csv")
            id = input("Enter unique ID: ")
            restaurant_info = restaurant.search_id(id)
            print("Name: " + restaurant_info.get_name() + ", " +
                  "\nAddress: " + restaurant_info.get_address() + ", " +
                  "\nHours: " + restaurant_info.get_hour())

        #If Input 2, search by name
        if menu_entry_index == 1:
            restaurant = RestaurantCatalog()
            restaurant.restaurant_info("restaurant_file.csv")
            name = input("Enter name: ")
            restaurant_info = restaurant.search_name(name)
            print("Name: " + restaurant_info.get_name() + ", " +
                  "\nAddress: " + restaurant_info.get_address() + ", " +
                  "\nHours: " + restaurant_info.get_hour())

        #If Input 3, search by address
        if menu_entry_index == 2:
            restaurant = RestaurantCatalog()
            restaurant.restaurant_info("restaurant_file.csv")
            address = input("Enter Andress: ")
            restaurant_info = restaurant.search_address(address)
            print("Name: " + restaurant_info.get_name() + ", " +
                  "\nAddress: " + restaurant_info.get_address() + ", " +
                  "\nHours: " + restaurant_info.get_hour())

        #If Input 4, search by category
        if menu_entry_index == 3:
            restaurant = RestaurantCatalog()
            restaurant.restaurant_info("restaurant_file.csv")
            category = input("Enter Catagories: ")
            restaurant_info = restaurant.search_category(category)
            print("Name: " + restaurant_info.get_name() + ", " +
                  "\nAddress: " + restaurant_info.get_address() + ", " +
                  "\nHours: " + restaurant_info.get_hour())

        if menu_entry_index == 4:
            count = 0
        field_input = []
        fields = [
            'Name: ', 'Address: ', 'City: ', 'State: ', 'Postal Code: ',
            'Stars: ', 'Review Count: ', 'Attributes: ', 'Categories: ',
            'Hours: '
        ]

        for field in fields:
            field_input.append(input(fields[count]))
            count += 1

        new_restaurant = RestaurantCatalog()
        new_restaurant.restaurant_info("test.csv")
        new_restaurant.save_restaurant_changes("test.csv")


####################################################### - Zachary Malloy

    def terminal_subsearch_test():
        #Introduction Menu
        main_menu_title = "Main Menu"
        main_menu_items = [
            "Search for restaurant", "Add new restaurant",
            "Edit existing restaurant"
        ]
        main_menu_exit = False
        #Naming for Menu
        main_menu = TerminalMenu(
            menu_entries=main_menu_items,
            title=main_menu_title,
        )
        #Sub Menu after clicking first (start search)
        edit_menu_title = "Main Menu"
        edit_menu_items = [
            "Search via ID", "Search via Name", "Search via Address",
            "Search via Catagory"
        ]
        #Naming for Sub Menu
        edit_menu_back = False
        edt_menu = TerminalMenu(
            edit_menu_items,
            title=edit_menu_title,
        )

        while not main_menu_exit:
            main_sel = main_menu.show()
            if main_sel == 0:
                while not edit_menu_back:
                    edit_sel = edt_menu.show()
                    if edit_sel == 0:
                        #If method to search for different ways (Zack's Code)
                        restaurant = RestaurantCatalog()
                        restaurant.restaurant_info("restaurant_file.csv")
                        id = input("Enter unique ID: ")
                        restaurant_info = restaurant.search_id(id)
                        return restaurant
                    if edit_sel == 1:
                        restaurant = RestaurantCatalog()
                        restaurant.restaurant_info("restaurant_file.csv")
                        name = input("Enter name: ")
                        restaurant_info = restaurant.search_name(name)
                        return restaurant
                    if edit_sel == 2:
                        restaurant = RestaurantCatalog()
                        restaurant.restaurant_info("restaurant_file.csv")
                        address = input("Enter Andress: ")
                        restaurant_info = restaurant.search_address(address)
                        return restaurant
                    if edit_sel == 3:
                        restaurant = RestaurantCatalog()
                        restaurant.restaurant_info("restaurant_file.csv")
                        category = input("Enter Catagories: ")
                        restaurant_info = restaurant.search_category(category)
                        return restaurant

            #If didn't click first and instead second (then edit) (Leo's Code)
            elif main_sel == 1:
                count = 0
            field_input = []
            fields = [
                'Name: ', 'Address: ', 'City: ', 'State: ', 'Postal Code: ',
                'Stars: ', 'Attributes: ', 'Categories: ',
                'Hours: '
            ]

            for field in fields:
                field_input.append(input(fields[count]))
                count += 1

            new_restaurant = RestaurantCatalog()
            new_restaurant.restaurant_info("restaurant_file.csv")
            new_restaurant.save_restaurant_changes("restaurant_file.csv")
