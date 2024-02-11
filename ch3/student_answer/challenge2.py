def split(string):
    if len(string) % 2 != 0:
        string += '_'
    pairs = [string[i:i+2] for i in range(0, len(string), 2)]
    return pairs

result = split('abc')
print(result)