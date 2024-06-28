PROBLEM_LIST = [
    ('Engine', 2000),
    ('Breaks', 1000),
    ('5000 km treatment', 500),
    ('10,000 km treatment', 1000),
    ('Filters + Oil', 250),
    ('Gear', 1000)
]

def get_all_problems():
    return PROBLEM_LIST

def calculate_total_price(selected_problems):
    return sum(price for _, price in selected_problems)