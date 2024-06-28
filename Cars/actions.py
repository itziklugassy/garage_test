import json
import os
from Problems import problem_menu, problems

CARS_FILE = 'cars.json'

def initialize_garage():
    if os.path.exists(CARS_FILE):
        try:
            with open(CARS_FILE, 'r') as file:
                cars = json.load(file)
            print(f"Debug: Loaded {len(cars)} cars from file.")
            return cars
        except json.JSONDecodeError:
            print("Error reading cars.json. Starting with an empty garage.")
    else:
        print("Debug: No cars.json file found. Starting with an empty garage.")
    return []

def save_garage(cars):
    with open(CARS_FILE, 'w') as file:
        json.dump(cars, file)
    print(f"Debug: Saved {len(cars)} cars to file.")

def list_cars(cars):
    if not cars:
        print("No cars in the garage.")
    else:
        print(f"Listing {len(cars)} cars:")
        for car in cars:
            print(f"Car Number: {car['number']}, Problems: {', '.join(car['problems'])}, Price: {car['price']} NIS")

def add_car(cars):
    car_number = input("Enter car number: ")
    car_problems, total_price = problem_menu.choose_problems()
    print(f"The price of this fix is: {total_price} NIS. Do you wish to proceed? yes/no")
    if input().lower() == 'yes':
        new_car = {'number': car_number, 'problems': car_problems, 'price': total_price}
        cars.append(new_car)
        save_garage(cars)
        print(f"Car added successfully. Debug: Current number of cars: {len(cars)}")
    else:
        print("Car not added.")
    return cars

def delete_car(cars):
    car_number = input("Enter car number to delete: ")
    initial_length = len(cars)
    cars = [car for car in cars if car['number'] != car_number]
    if len(cars) < initial_length:
        save_garage(cars)
        print("Car deleted successfully.")
    else:
        print("Car not found.")
    return cars

def search_car(cars):
    car_number = input("Enter car number to search: ")
    for car in cars:
        if car['number'] == car_number:
            print(f"Car Number: {car['number']}, Problems: {', '.join(car['problems'])}, Price: {car['price']} NIS")
            return
    print("Car not found.")

def total_cars(cars):
    return len(cars)

def total_profit(cars):
    return sum(car['price'] for car in cars)