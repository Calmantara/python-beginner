def length_last(string):
    words = string.split()
    return len(words[-1])

result = length_last("luffy is still joyboy")
print(result)
print(length_last("   fly me   to   the moon  "))