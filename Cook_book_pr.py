
with open('rec.txt', encoding="utf-8") as f:
    text = f.read()
recipe_text = text.split('\n\n')

for i in range(len(recipe_text)):
    recipe_text[i] = recipe_text[i].split('\n')

for i in range(len(recipe_text)):
    for j in range(2, len(recipe_text[i])):
        recipe_text[i][j] = recipe_text[i][j].split(' | ')
        ingrid_prop = recipe_text[i][j]
        recipe_text[i][j] = {'ingridient_name': ingrid_prop[0], 'quantity': int(ingrid_prop[1]), 'measure': ingrid_prop[2]}

d = {}
for elem in recipe_text:
    d[elem[0]] = elem[2:]


def get_shop_list_by_dishes(dishes, person_count):
    basket_dict = {}
    if not type(person_count) == int or person_count <= 0:
        return 'Incorrect count'
    for dish in dishes:
        if dish not in d.keys():
            return 'Incorrect dish name.'
        for ingrid in d[dish]:
            if ingrid['ingridient_name'] not in basket_dict.keys():
                basket_dict[ingrid['ingridient_name']] = {'measure': ingrid['measure'], 'quantity': ingrid['quantity']*person_count}
            else:
                basket_dict[ingrid['ingridient_name']]['quantity'] += ingrid['quantity']*person_count
    return basket_dict

get_shop_list_by_dishes(['Фахитос', 'Омлет'], '1')
get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)