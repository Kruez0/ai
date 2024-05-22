itemA = {'weight': 10, 'value': 60}
itemB = {'weight': 20, 'value': 100}
itemC = {'weight': 30, 'value': 120}

items = [itemA, itemB, itemC]

max_weight_limit = 50  

def fractional_knapsack(items, capacity):
    for item in items:
        weight = item['weight']
        value = item['value']
        item['value_per_unit'] = value / weight 

    sorted_items = sorted(items, key=lambda x: x['value_per_unit'], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity

    for item in sorted_items:
        if remaining_capacity <= 0:
            break

        item_weight = item['weight']
        item_value = item['value']

        if item_weight <= remaining_capacity:
            print(f"Item Values:",item_value)
            total_value += item_value
            remaining_capacity -= item_weight
        else:
            fraction = remaining_capacity / item_weight
            total_value += fraction * item_value
            print(f"Fractional item Values:",fraction*item_value)

            remaining_capacity = 0

    return total_value
max_value = fractional_knapsack(items, max_weight_limit)
print(f"Maximum value obtainable: {max_value}")
