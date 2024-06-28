from . import actions

def main_menu(cars):
    print("\nMain Menu:")
    print("1. List all cars")
    print("2. Add a car")
    print("3. Delete car")
    print("4. Search car")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == '1':
        actions.list_cars(cars)
    elif choice == '2':
        cars = actions.add_car(cars)
    elif choice == '3':
        cars = actions.delete_car(cars)
    elif choice == '4':
        actions.search_car(cars)
    elif choice == '5':
        print("Exiting the program. Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")
    
    return cars