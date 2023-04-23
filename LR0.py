# A dictionary representing the grammar productions
productions = {
    'S': ['A'],
    'A': ['B', 'a'],
    'B': ['C', 'b'],
    'C': ['c']
}

# Define a class for LR(0) items
class LR0Item:
    def __init__(self, production, dot_pos=0):
        self.production = production  # A tuple representing the production rule
        self.dot_pos = dot_pos  # The position of the dot in the production

    def __repr__(self):
        prod = list(self.production)
        prod.insert(self.dot_pos, '.')
        return '{} -> {}'.format(prod[0], ''.join(prod[1:]))

# Function to compute the LR(0) items for a given grammar
def lr0_items(grammar):
    items = []
    start_item = LR0Item(('S', grammar['S'][0]))  # The start item
    items.append(start_item)
    unprocessed_items = [start_item]
    while unprocessed_items:
        item = unprocessed_items.pop()
        prod = item.production
        dot_pos = item.dot_pos
        if dot_pos < len(prod)-1:
            next_symbol = prod[dot_pos+1]
            for rule in grammar.get(next_symbol, []):
                new_item = LR0Item((next_symbol, rule))
                if new_item not in items:
                    items.append(new_item)
                    unprocessed_items.append(new_item)
    return items

# Example usage
items = lr0_items(productions)
for i, item in enumerate(items):
    print(i, item)
