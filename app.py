from Cars import menu, actions

def main():
    cars = actions.initialize_garage()
    while True:
        total_cars = actions.total_cars(cars)
        total_profit = actions.total_profit(cars)
        print(f"\nCurrently there are {total_cars} cars. The current profit is: {total_profit} NIS")
        cars = menu.main_menu(cars)

if __name__ == "__main__":
    main()