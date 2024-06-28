from . import problems

def choose_problems():
    all_problems = problems.get_all_problems()
    selected_problems = []
    print("Choose problems for the car (enter the number corresponding to the problem, type 'done' when finished):")
    for i, (name, price) in enumerate(all_problems, 1):
        print(f"{i}. {name} - {price} NIS")
    
    while True:
        choice = input("Enter problem number (or 'done'): ")
        if choice.lower() == 'done':
            break
        try:
            index = int(choice) - 1
            if 0 <= index < len(all_problems):
                selected_problems.append(all_problems[index])
                print(f"Added: {all_problems[index][0]}")
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    
    total_price = problems.calculate_total_price(selected_problems)
    problem_names = [name for name, _ in selected_problems]
    return problem_names, total_price