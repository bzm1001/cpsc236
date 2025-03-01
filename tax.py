tax = 0.06

def salesTax(total):
    return round(total * tax, 2)

def totalAfterTax(total):
    return round(total + salesTax(total), 2)