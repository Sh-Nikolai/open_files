
with open('menu.txt', 'rt', encoding = 'utf-8') as f:
    cook_book = {}
    for line in f:
        dish = line.strip()
        person_count = int(f.readline())
        engridients = []
        for i in range(person_count):
            emp = f.readline()
            emp.split(' | ')
            ingredient_name, quantity, measure = emp.split(' | ')
            engridients.append({
                'ingredient_name': ingredient_name,
                'quantity': int(quantity),
                'measure': measure,
                })
        f.readline()
        cook_book[dish] = engridients


def get_shop_list_by_dishes(dishes, person_count):
    dishes_dict = {}
    for dish in dishes:
        if dish in cook_book:
            for ingredient in cook_book[dish]:
                dishes_dict[ingredient['ingredient_name']] = {'messure':ingredient['measure'], 'quantity': ingredient['quantity']*person_count}
    return dishes_dict












print(get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2))




