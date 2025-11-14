def calculate_total_profit(dish_tuple):
    name, cat, cost, price, ordered = dish_tuple
    profit = (price - cost) * ordered
    return profit

def find_most_profitable_dish(menu_data):
    profits = []
    for x in menu_data:
        profit = calculate_total_profit(x)
        profits.append(profit)
    max_profit = max(profits)
    bett_dish = None
    if calculate_total_profit(x) == max_profit:
        if bett_dish is None or x[0] < bett_dish:
            bett_dish = x[0]
    return bett_dish

def get_dishes_in_category(menu_data, category_name):
    better_dishes = []
    for x in menu_data:
        if x[1] == category_name:
            better_dishes.append(x[0])
    better_dishes.sort()
    return better_dishes


def get_category_popularity(menu_data):
    categories = []
    for x in menu_data:
        if x[1] not in categories:
            categories.append(x[1])
    catt_summary = []
    for category in categories:
        total_orders = 0
        for x in menu_data:
            if x[1] == category:
                total_orders += x[4]
        catt_summary.append((category, total_orders))
    catt_summary.sort()
    return catt_summary



def analyze_menu(menu_data):
    most_prof = find_most_profitable_dish(menu_data)
    common_main_dish = get_dishes_in_category(menu_data, 'Main Course')
    catt_summary = get_category_popularity(menu_data)
    return (most_prof, common_main_dish, catt_summary)



menu_data = [
    ('Bruschetta', 'Appetizer', 2.50, 8.50, 150),
    ('Steak Frites', 'Main Course', 9.00, 24.00, 200),
    ('Caesar Salad', 'Appetizer', 3.00, 10.00, 250),
    ('Pasta Carbonara', 'Main Course', 5.50, 18.50, 300),
    ('Tiramisu', 'Dessert', 4.00, 9.00, 400)
]

print(analyze_menu(menu_data))