def solve(string):
    upper = sum(1 for char in string if char.isupper())
    lower = sum(1 for char in string if char.islower())
    if upper > lower:
        return string.upper()
    else:
        return string.lower()
    
result = solve("coDe")
print(result)
