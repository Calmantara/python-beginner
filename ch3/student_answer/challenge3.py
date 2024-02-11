def length_last(string):
    words = string.split()
    return len(words[-1])

result = length_last("luffy is still joyboy")
print(result)