# Challenge 3
# Given a string s consisting of words and spaces, 
# return the length of the last word in the string.
# A word is a maximal substring 
# consisting of non-space characters only.
# ==========
# Input: s = "luffy is still joyboy"
# Output: 6
# Input: s = "   fly me   to   the moon  "
# Output: 4
# Input: s = "Hello World"
# Output: 5
def challenge3(s: str) -> int:
    sarr = s.split(" ")
    while (sarr[-1] == ""):
        sarr = sarr[:len(sarr)-1]
    return len(sarr[-1])

# Challenge 4
# In this Kata, you will be given a string that may have mixed uppercase and lowercase letters and your task is to convert that string to either lowercase only or uppercase only based on:
# make as few changes as possible.
# if the string contains equal number of uppercase and lowercase letters, 
# convert the string to lowercase.
# =========
# solve("coDe") = "code". Lowercase characters > uppercase. Change only the "D" to lowercase.
# solve("CODe") = "CODE". Uppercase characters > lowecase. Change only the "e" to uppercase.
# solve("coDE") = "code". Upper == lowercase. Change all to lowercase.
def challenge4(s:str) -> str:
    a, b = 0, 0
    for i in s:
        if i.islower(): a += 1
        else: b += 1
    return s.upper() if b > a else s.lower() 