purchases = [
    {"item": "apple", "category": "fruit", "price": 1.2, "quantity": 10},
    {"item": "banana", "category": "fruit", "price": 0.5, "quantity": 5},
    {"item": "milk", "category": "dairy", "price": 1.5, "quantity": 2},
    {"item": "bread", "category": "bakery", "price": 2.0, "quantity": 3},
]

min_price = 1.0

def total_revenue(purchases):
    result = 0
    for dict in purchases:
        revenue = dict['price'] * dict['quantity']
        result += revenue
    return result


def items_by_category(purchases):
    result = {}
    for dict in purchases:
        category = dict['category']
        item = dict['item']
        
        if category not in result:
                result[category] = []
            
        if item not in result[category]:
            result[category].append(item)
    return result


def expensive_purchases(purchases, min_price):
     result = []
     for dict in purchases:
          if dict['price'] >= min_price:
               result.append(dict)
     return result


def average_price_by_category(purchases):
    category_prices = {}
    category_counts = {}
    
    for purchase in purchases:
        category = purchase["category"]
        price = purchase["price"]
        
        if category not in category_prices:
            category_prices[category] = 0
            category_counts[category] = 0
        
        category_prices[category] += price
        category_counts[category] += 1
    
    return {category: category_prices[category] / category_counts[category] for category in category_prices}


def most_frequent_category(purchases):
    category_quantities = {}
    
    for purchase in purchases:
        category = purchase["category"].lower()
        quantity = purchase["quantity"]
        
        if category not in category_quantities:
            category_quantities[category] = 0
        
        category_quantities[category] += quantity
    
    return max(category_quantities)

print(f"Общая выручка: {total_revenue(purchases)}\nТовары по категориям: {items_by_category(purchases)}\nПокупки дороже {min_price}: {expensive_purchases(purchases, min_price)}\nСредняя цена по категориям: {average_price_by_category(purchases)}\nКатегория с наибольшим количеством проданных товаров: {most_frequent_category(purchases)}")