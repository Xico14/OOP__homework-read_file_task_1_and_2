def recipe_book():
    cook_book = {}

    with open('recipes.txt', 'r', encoding='utf-8') as file:
        for line in file:
            dish_recipe = line.strip()
            cook_book[dish_recipe] = []
            for i in range(int(file.readline().strip())):
                ingredient_name, quantity, measure = file.readline().strip().split(' | ')
                cook_book[dish_recipe].append({'ingredient_name': ingredient_name,
                                                'quantity': quantity,
                                                'measure': measure})
            file.readline()

    return cook_book


def get_shop_list_by_dishes(dishes, person_count):
    shop_list = {}
    cook_book = recipe_book()

    for dish in dishes:
        for ingredient in cook_book.get(dish, []):
            ingredient_name = ingredient.get('ingredient_name')
            ingredient_quantity = int(ingredient.get('quantity')) * person_count
            ingredient_measure = ingredient.get('measure')
            if ingredient_name in shop_list:
                shop_list[ingredient_name]['quantity'] += ingredient_quantity
            else:
                shop_list[ingredient_name] = {
                    'measure': ingredient_measure,
                    'quantity': ingredient_quantity
                }

    return print(shop_list)


get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)