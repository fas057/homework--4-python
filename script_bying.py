purchases = [
    {"item": "Яблоки", "category": "фрукты", "price": 4.2, "quantity": 15},
    {"item": "Бананы", "category": "фрукты", "price": 2.5, "quantity": 35},
    {"item": "Молоко", "category": "молочные продукты", "price": 1.5, "quantity": 4},
    {"item": "Хлеб", "category": "выпечка", "price": 2.8, "quantity": 3},
]

def total_revenue(purchases):
    return sum(p['price'] * p['quantity'] for p in purchases)

def items_by_category(purchases):
    category_items = {}
    for purchase in purchases:
        category = purchase['category']
        item = purchase['item']
        if category not in category_items:
            category_items[category] = []
        if item not in category_items[category]:
            category_items[category].append(item)
    return category_items

def expensive_purchases(purchases, min_price):
    return [p for p in purchases if p['price'] >= min_price]

def average_price_by_category(purchases):
    category_prices = {}
    for p in purchases:
        category = p['category']
        price = p['price']
        if category not in category_prices:
            category_prices[category] = {'total': 0.0, 'count': 0}
        category_prices[category]['total'] += price
        category_prices[category]['count'] += 1
    avg_prices = {}
    for cat, data in category_prices.items():
        avg_prices[cat] = round(data['total'] / data['count'], 2)
    return avg_prices

def most_frequent_category(purchases):
    category_quantities = {}
    for p in purchases:
        category = p['category']
        quantity = p['quantity']
        if category not in category_quantities:
            category_quantities[category] = 0
        category_quantities[category] += quantity
    max_quantity = max(category_quantities.values())
    for cat, q in category_quantities.items():
        if q == max_quantity:
            return cat

# Расчет данных
revenue = total_revenue(purchases)
items_cat = items_by_category(purchases)
min_price = 1.0
expensive = expensive_purchases(purchases, min_price)
avg_prices = average_price_by_category(purchases)
most_freq_cat = most_frequent_category(purchases)

# Вывод отчета
print(f"Общая выручка: {revenue}")
print(f"Товары по категориям: {items_cat}")
print(f"Покупки дороже {min_price}: {expensive}")
print(f"Средняя цена по категориям: {avg_prices}")
print(f"Категория с наибольшим количеством проданных товаров: {most_freq_cat}")