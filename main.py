from random import randint, choice


def style(name, color='white', lore='', is_italic=False):
    is_italic = str(is_italic).lower()
    lore_inject = f', Lore:[\'"{lore}"\']' if lore else ''
    return '"display":{"Name":\'{"text":"' + name + '", "color": "' \
        + color +'", "italic": "' + is_italic +'"}\'' + lore_inject + '}'


def enchantments(*ench):
    rows = []
    for ench_id, level in ench:
        row = '{id:' + ench_id + ',lvl:' + str(level) + '}'
        rows.append(row)
    return f'Enchantments:[{",".join(rows)}]'


def join_attr(*attr):
    return '{' + ', '.join(attr) + '}'


def chest_inner(items, as_item=True):
    rows = []
    for slot, item_id, count, tag in items:
        tag_code = f',tag:{tag}' if tag else ''
        row = f'Slot:{slot},Count:{count},id:{item_id}' + tag_code
        rows.append('{' + row + '}')
    a = 'Items:[' + ','.join(rows) + ']'
    if as_item:
        return f'BlockEntityTag:{a}'
    return a

def item(idx, *attr):
    return idx + f'{join_attr(*attr)}'

#/give @p chest{BlockEntityTag:{Items:[{Slot:0,id:acacia_boat,Count:1}]}} 1


print(item('chest', style('kit', 'red'), chest_inner([
    (0, 'grass', 2, join_attr(
        style('Excalibur', 'red', 'Fuck'),
        enchantments(
            ('sharpness', 5)
        )
    ))
], False)))
