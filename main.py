def display(name, color='white'):
    return '"display":{"Name":\'{"text":"' + name + '", "color": "' + color +'"}\'}'


def give_command(target, item_id, amount, attr_s=''):
    return f'/give {target} minecraft:{item_id}{attr_s} {amount}'


print(display('frick', 'red'))

#attr = load_dict('buffer.json')
#print(give_command('@p', 'netherite_sword', attr, 1))