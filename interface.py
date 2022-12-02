from restaurant_catalog import RestaurantCatalog
from simple_term_menu import TerminalMenu
from main_functions import MainFunctions

class Interface:

    @staticmethod
    def menu_cl():
        #Introduction Menu
        main_menu_title = "**************************************************************\n*      Welcome to restaurant information retrival system     *\n**************************************************************"
        main_menu_items = [
            "  Search for restaurant", "  Add new restaurant",
            "  Edit existing restaurant", "  Exit Program"
        ]
        # Styling settings - Leo Garcia
        main_menu_cursor = ">"
        main_menu_cursor_style = ("fg_red", "bold")
        current_selection_color = ("fg_red", "fg_yellow")
        main_menu_exit = False
        # Apply styling to main menu - Leo Garcia
        main_menu = TerminalMenu(
            menu_entries=main_menu_items,
            title=main_menu_title,
            menu_cursor=main_menu_cursor,
            menu_cursor_style=main_menu_cursor_style,
            menu_highlight_style=current_selection_color,
            cycle_cursor=True,
            clear_screen=True,
        )
        #Sub Menu after clicking first (start search) - Zachary Malloy
        search_sub_menu_title = "Main Menu"
        search_sub_menu_items = [
            "Search via ID", "Search via Name", "Search via Address",
            "Search via Catagory", "Back"
        ]
        #Naming for Sub Menu - Zachary Malloy
        edit_menu_back = False
        edt_menu = TerminalMenu(
            search_sub_menu_items,
            title=search_sub_menu_title,
            menu_cursor=main_menu_cursor,
            menu_cursor_style=main_menu_cursor_style,
            menu_highlight_style=current_selection_color,
            cycle_cursor=True,
            clear_screen=False,
        )
        # Leo
        add_menu_items = ["Yes", "No"]
        while not main_menu_exit:
            main_sel = main_menu.show()
            if main_sel == 0:
                while not edit_menu_back:
                    sub_sel = edt_menu.show()
                    if sub_sel == 0:
                        #If method to search for differents way - Zachary Malloy
                        restaurant = RestaurantCatalog()
                        restaurant.restaurant_info("restaurant_file.csv")
                        id = input("Enter unique ID: ")
                        restaurant_info = restaurant.search_id(id)
                        print("Name: " + restaurant_info.get_name() + ", " +
                              "\nAddress: " + restaurant_info.get_address() +
                              ", " + "\nHours: " + restaurant_info.get_hour())
                    if sub_sel == 1:
                        restaurant = RestaurantCatalog()
                        restaurant.restaurant_info("restaurant_file.csv")
                        name = input("Enter name: ")
                        restaurant_info = restaurant.search_name(name)
                        print("\nName: " + restaurant_info.get_name() + ", " +
                              "\n\nAddress: " + restaurant_info.get_address() +
                              ", " + "\n\nHours: " + restaurant_info.get_hour())
                    if sub_sel == 2:
                        restaurant = RestaurantCatalog()
                        restaurant.restaurant_info("restaurant_file.csv")
                        address = input("Enter Andress: ")
                        restaurant_info = restaurant.search_address(address)
                        print("Name: " + restaurant_info.get_name() + ", " +
                              "\nAddress: " + restaurant_info.get_address() +
                              ", " + "\nHours: " + restaurant_info.get_hour())
                    if sub_sel == 3:
                        restaurant = RestaurantCatalog()
                        restaurant.restaurant_info("restaurant_file.csv")
                        category = input("Enter Catagories: ")
                        restaurant_info = restaurant.search_category(category)
                        print("Name: " + restaurant_info.get_name() + ", " +
                              "\nAddress: " + restaurant_info.get_address() +
                              ", " + "\nHours: " + restaurant_info.get_hour())
                    if sub_sel == 4:
                      edit_menu_back = True
                edit_menu_back = False

            # Add restaurant selection - Leo Garcia
            elif main_sel == 1:
              MainFunctions.add_restaurant_test()
            # Edit restaurant selection - Leo Garcia
            elif main_sel == 2:
              MainFunctions.edit_restaurant_test()
            # Exit Program - Leo Garcia
            elif main_sel == 3:
              print("Sucessfully Exited")
              main_menu_exit = True