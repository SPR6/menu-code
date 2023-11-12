def display_home_page():
    print("Welcome to Book My Property!")
    print("Please select an option:")
    print("1. Buy")
    print("2. Sell")
    print("3. Rent")

def get_user_choice():
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            return choice
        except ValueError:
            print("Invalid input. Please enter a number.")

def buy_options():
    print("Under Buy, choose a property type:")
    print("1. Land")
    print("2. Building")
    print("0. Back to main menu")
    choice = get_user_choice()

    if choice == 1:
        buy_land_options()
    elif choice == 2:
        buy_building_options()
    elif choice == 0:
        return

def sell_options():
    print("Under Sell, choose a property type:")
    print("1. Land")
    print("2. Building")
    print("0. Back to main menu")
    choice = get_user_choice()

    if choice == 1:
        sell_land_options()
    elif choice == 2:
        sell_building_options()
    elif choice == 0:
        return

def rent_options():
    print("Under Rent, choose a property type:")
    print("1. Land")
    print("2. Building")
    print("0. Back to main menu")
    choice = get_user_choice()

    if choice == 1:
        rent_land_options()
    elif choice == 2:
        rent_building_options()
    elif choice == 0:
        return

def buy_land_options():
    print("Under Land, choose a type:")
    print("1. Residential Plot")
    print("2. Commercial Plot")
    print("3. Industrial Plot")
    print("4. Dry Land")
    print("5. Agriculture Land")
    print("0. Back to Buy menu")
    choice = get_user_choice()

    if choice == 1:
        buy_land_residential()
    elif choice == 2:
        buy_land_commercial()
    elif choice == 3:
        buy_land_industrial()
    elif choice == 4:
        buy_land_dry()
    elif choice == 5:
        buy_land_agriculture()
    elif choice == 0:
        return

def sell_land_options():
    print("Under Land, choose a type:")
    print("1. Residential Plot")
    print("2. Commercial Plot")
    print("3. Industrial Plot")
    print("4. Dry Land")
    print("5. Agriculture Land")
    print("0. Back to Sell menu")
    choice = get_user_choice()

    if choice == 1:
        sell_land_residential()
    elif choice == 2:
        sell_land_commercial()
    elif choice == 3:
        sell_land_industrial()
    elif choice == 4:
        sell_land_dry()
    elif choice == 5:
        sell_land_agriculture()
    elif choice == 0:
        return

def buy_building_options():
    print("Under Building, choose a type:")
    print("1. Residential")
    print("2. Commercial")
    print("3. Industrial")
    print("0. Back to Buy menu")
    choice = get_user_choice()

    if choice == 1:
        buy_building_residential()
    elif choice == 2:
        buy_building_commercial()
    elif choice == 3:
        buy_building_industrial()
    elif choice == 0:
        return

def sell_building_options():
    print("Under Building, choose a type:")
    print("1. Residential")
    print("2. Commercial")
    print("3. Industrial")
    print("0. Back to Sell menu")
    choice = get_user_choice()

    if choice == 1:
        sell_building_residential()
    elif choice == 2:
        sell_building_commercial()
    elif choice == 3:
        sell_building_industrial()
    elif choice == 0:
        return

def rent_land_options():
    print("Under Land, choose a type:")
    print("1. Residential Land")
    print("2. Commercial Land")
    print("3. Industrial Land")
    print("0. Back to Rent menu")
    choice = get_user_choice()

    if choice == 1:
        rent_land_residential()
    elif choice == 2:
        rent_land_commercial()
    elif choice == 3:
        rent_land_industrial()
    elif choice == 0:
        return

def rent_building_options():
    print("Under Building, choose a type:")
    print("1. Residential")
    print("2. Commercial")
    print("3. Industrial")
    print("0. Back to Rent menu")
    choice = get_user_choice()

    if choice == 1:
        rent_building_residential()
    elif choice == 2:
        rent_building_commercial()
    elif choice == 3:
        rent_building_industrial()
    elif choice == 0:
        return

# Buy options
def buy_land_residential():
    print("You chose to buy a residential plot.")

def buy_land_commercial():
    print("You chose to buy a commercial plot.")

def buy_land_industrial():
    print("You chose to buy an industrial plot.")

def buy_land_dry():
    print("You chose to buy dry land.")

def buy_land_agriculture():
    print("You chose to buy agriculture land.")

def buy_building_residential():
    print("You chose to buy a residential building.")

def buy_building_commercial():
    print("You chose to buy a commercial building.")

def buy_building_industrial():
    print("You chose to buy an industrial building.")

# Sell options
def sell_land_residential():
    print("You chose to sell a residential plot.")

def sell_land_commercial():
    print("You chose to sell a commercial plot.")

def sell_land_industrial():
    print("You chose to sell an industrial plot.")

def sell_land_dry():
    print("You chose to sell dry land.")

def sell_land_agriculture():
    print("You chose to sell agriculture land.")

def sell_building_residential():
    print("You chose to sell a residential building.")

def sell_building_commercial():
    print("You chose to sell a commercial building.")

def sell_building_industrial():
    print("You chose to sell an industrial building.")

# Rent options
def rent_land_residential():
    print("You chose to rent residential land.")

def rent_land_commercial():
    print("You chose to rent commercial land.")

def rent_land_industrial():
    print("You chose to rent industrial land.")

def rent_building_residential():
    print("You chose to rent a residential building.")

def rent_building_commercial():
    print("You chose to rent a commercial building.")

def rent_building_industrial():
    print("You chose to rent an industrial building.")

def main():
    menu_stack = []  # To keep track of the main menu
    submenu_stack = []  # To keep track of the sub-menus
    user_choice = -1

    while user_choice != 0:
        display_home_page()
        user_choice = get_user_choice()

        if user_choice == 1:
            buy_options()
            submenu_stack = ["Buy"]
        elif user_choice == 2:
            sell_options()
            submenu_stack = ["Sell"]
        elif user_choice == 3:
            rent_options()
            submenu_stack = ["Rent"]
        elif user_choice == 0 and submenu_stack:
            if len(submenu_stack) > 1:
                submenu_stack.pop()
            else:
                submenu_stack = []
        elif user_choice == 0 and menu_stack:
            submenu_stack = menu_stack.pop()
        elif user_choice == 0:
            print("You are already at the main menu.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
