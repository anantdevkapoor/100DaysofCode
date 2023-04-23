# A dictionary representing the grammar productions
productions = {
    'S': ['AB', 'bC'],
    'A': ['aA', 'a'],
    'B': ['bB', 'c']
    'C': ['cC', 'd']
}

# A dictionary representing the nullable symbols
nullable = {'A': True, 'B': False, 'C': False}

# Function to compute the leading set of a symbol
def leading(symbol):
    lead = set()
    if symbol in nullable:
        for prod in productions[symbol]:
            for i in range(len(prod)):
                if prod[i] in nullable:
                    lead |= leading(prod[i])
                    if i < len(prod)-1 and not nullable[prod[i]]:
                        break
                else:
                    lead.add(prod[i])
                    if i < len(prod)-1 and not nullable[prod[i]]:
                        break
    return lead

# Function to compute the trailing set of a symbol
def trailing(symbol):
    trail = set()
    if symbol in nullable:
        for prod in productions[symbol]:
            for i in range(len(prod)-1, -1, -1):
                if prod[i] in nullable:
                    trail |= trailing(prod[i])
                    if i > 0 and not nullable[prod[i]]:
                        break
                else:
                    trail.add(prod[i])
                    if i > 0 and not nullable[prod[i]]:
                        break
    return trail

# Example usage
print("Leading of A:", leading('A'))
print("Trailing of A:", trailing('A'))
