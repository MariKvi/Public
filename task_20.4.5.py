import json

with open("orders_july_2023.json", "r") as my_file:
    orders = json.load(my_file)

# 1. Какой номер самого дорогого заказа за июль?
max_price = 0
max_order = ''
for order_num, orders_data in orders.items():
    price = orders_data['price']
    if price > max_price:
        max_order = order_num
        max_price = price
print(f'1.Номер заказа с самой большой стоимостью: {max_order}, стоимость заказа: {max_price}')

# 2. Какой номер заказа с самым большим количеством товаров?
max_quantity = 0
max_order_q = ''
for order_num, orders_data in orders.items():
    quantity = orders_data['quantity']
    if quantity > max_quantity:
        max_order_q = order_num
        max_quantity = quantity
print(f'2.Номер заказа с самым большим количеством товаров: {max_order_q}, количество товаров: {max_quantity}')

# 3. В какой день в июле было сделано больше всего заказов?
date_dict = {}
for order_num, orders_data in orders.items():
    if orders_data['date'] in date_dict.keys():
        date_dict[orders_data.get('date')] += 1
    else:
        date_dict[orders_data.get('date')] = 1
for date in date_dict:
    max_value = max(date_dict.values())
    if date_dict[date] == max_value:
        print(f'3.Больше всего заказов было сделано {date}, количество заказов: {date_dict[date]}')

# 4.Какой пользователь сделал самое большое количество заказов за июль?
users_dict = {}
for order_num, orders_data in orders.items():
    if orders_data['user_id'] in users_dict.keys():
        users_dict[orders_data.get('user_id')] += 1
    else:
        users_dict[orders_data.get('user_id')] = 1
max_order_value = 0
user_id = 0
for key, value in users_dict.items():
    if value > max_order_value:
        user_id, max_order_value = key, value
print(f'4.Самое большое количество заказов было сделано пользователем {user_id}, количество заказов: {max_order_value}.')

# 5.У какого пользователя самая большая суммарная стоимость заказов за июль?
users_total_cost = {}
for order_num, orders_data in orders.items():
    if orders_data['user_id'] in users_total_cost.keys():
        users_total_cost[orders_data['user_id']] += orders_data.get('price')
    else:
        users_total_cost[orders_data['user_id']] = orders_data.get('price')
max_total_cost = 0
user_id = 0
for key, value in users_total_cost.items():
    if value > max_total_cost:
        user_id, max_total_cost = key,value
print(f'5.Самая большая суммарная стоимость заказов за июль: {max_total_cost}, у пользователя {user_id}.')

# 6.Какая средняя стоимость заказа была в июле?
orders_count = len(orders)
total_cost = sum(users_total_cost.values())
print(f'6.Средняя стоимость заказа за июль: {total_cost/orders_count}.')

# 7.Какая средняя стоимость товаров в июле?
total_quantity = 0
for order_num, orders_data in orders.items():
    total_quantity += orders_data['quantity']
print(f'7.Средняя стоимость товаров в июле: {total_cost/total_quantity}')