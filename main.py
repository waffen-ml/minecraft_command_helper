from random import randint, choice


def display(name, color='white', lore='', is_italic=True):
    is_italic = str(is_italic).lower()
    return '"display":{"Name":\'{"text":"' + name + '", "color": "' \
        + color +'", "italic": "' + is_italic +'"}\', Lore:[\'"' + lore + '"\']}'


def join_attr(*attr):
    return '{' + ', '.join(attr) + '}'


def chest(items):
    rows = []
    for slot, item_id, count, tag in items:
        row = f'Slot:{slot},Count:{count},id:{item_id},tag:{tag}'
        rows.append('{' + row + '}')
    return 'chest{Items:[' + ','.join(rows) + ']}'


COLORS = ['white', 'red', 'yellow', 'blue', 'green']
ITEMS = ['iron_sword', 'beef', 'iron_shovel', 'grass']

items = [
    (i, choice(ITEMS), 1, join_attr(display('fuck', color=choice(COLORS), lore='f'))) for i in range(27)
]

print(chest(items))
