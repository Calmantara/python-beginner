# Challenge 1
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists into one sorted list. 
# The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# =========
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Input: list1 = [], list2 = []
# Output: []
# Input: list1 = [], list2 = [0]
# Output: [0]
def challenge1(arr1 : [int], arr2: [int]) -> [int]:
    arr3 = arr1 + arr2
    arr3.sort()
    return arr3

# Challenge 2
# Complete the solution so that it splits 
# the string into pairs of two characters. 
# If the string contains an odd number of 
# characters then it should replace the 
# missing second character of the final pair with 
# an underscore ('_').
# ==========
# 'abc' =>  ['ab', 'c_']
# 'abcdef' => ['ab', 'cd', 'ef']
def challenge2(s: str) -> [str]:
    res = []
    while len(s) > 0:
        buf = s[0:2]
        if len(buf) < 2:
            buf += "_"
        res.append(buf)
        s = s[2:]
    return res