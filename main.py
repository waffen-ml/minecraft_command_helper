def display(name, color='white', lore='', is_italic=True):
    is_italic = str(is_italic).lower()
    return '"display":{"Name":\'{"text":"' + name + '", "color": "' \
        + color +'", "italic": "' + is_italic +'"}\', Lore:[\'"' + lore + '"\']}'


def item(item_id, amount, attr_s=''):
    return f'minecraft:{item_id}{attr_s} {amount}'


def give_command(target, item):
    return f'/give {target} item'


print(display('frick', 'red', 'lore', False))

#attr = load_dict('buffer.json')
#print(give_command('@p', 'netherite_sword', attr, 1))