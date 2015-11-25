from collections import Counter

def is_vampirenumber(multiplicand1, multiplicand2):
    if multiplicand1 == None or multiplicand2 == None:
        return False
        
    concatenated_multiplicands = Counter(str(multiplicand1) + str(multiplicand2))
    product = Counter(str(multiplicand1 * multiplicand2))
    for key, value in concatenated_multiplicands.items():
        if key in product.keys() and value in product.values():
            continue
        else:
            return False
    return True

print is_vampirenumber(21, 6)
    