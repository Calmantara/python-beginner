# membuat virtual environment:
# python -m venv <<name env>>

# Data Type:
#   - integer
#   - float
#   - string
#   - bool 
#   - char
#   - dictionary
#   - list
#   - tuple

# python convention
# variable -> snake case
integer_var = 1
print(type(integer_var),integer_var)

number_var = 4.0
print(type(number_var), number_var)

string_var1 = "python class"
string_var2 = 'python class'
print(type(string_var1), string_var1)

bool_var1 = True
bool_var2 = False
print(type(bool_var1), bool_var1)

tuple_var = (1,2,3,4)
list_var = [1,2,3,4]
dictionary_var = {1:1}

# variable declarations
a = b = c = 4
print(a, b, c)

e, f = 1, 2
print(e, f)

# Convention in Programming
# Camel Case, Example: numberOfCollegeGraduates
# Pascal Case, Example: NumberOfCollegeGraduates
# Snake Case,Example: number_of_college_graduates

# Operations
# * / + - % **
num1 = 10
num2 = 20
div = num1 / num2
print(num1+num2, num1-num2, num1*num2, type(div))

float_num1 = 11.5
float_num2 = 10.5
# tebak hasil dari
print(num1 * float_num1) # 115.0
print(num1 + float_num1) # 21.5
print(num1 / float_num1) # 0.8
print(float_num2 % num2) # 10.5

str_1 = "1"
print(str_1 + str(num1))
print(int(str_1) + num1)

print(2 ** 2.1)

# Comparison
print(num1 == 10)
print(num1 != 20)
print(num1 <= 20)
print(num1 >= 5)

print(bool_var1 is True)
print(bool_var1 is not True)
# perbedaan is / is not dengan == / !=
# perbedaannya adalah memory address
# ketika membandingkan tuple, list, dictionary

print("====================")
list1 = [1,2,3,4]
list2 = list1       # list 2 kita copy persis dengan list 1
list3 = list(list1) # list 3 copy dari list 1 tapi hanya value saja
print(list1, list2, list3)
print(list1 == list2, list1 == list3) # True True
print(list1 is list2 , list1 is list3) # True False
print(id(list1), id(list2), id(list3))

list2 = [4,5,3,2]
print(id(list1), id(list2), id(list3))
print("====================")

# append
list1.append(5)
print(list1, list2, list3)

str_manipulation = "This Is very long string"
print(str_manipulation.capitalize())
print(str_manipulation.title())
print(str_manipulation.upper())
print(str_manipulation.lower())
print(str_manipulation.swapcase())
print(str_manipulation.index("Is"))
print(str_manipulation[10])
print(str_manipulation[10:])
print(str_manipulation.split(" "))

# List vs Tuple vs Dictionary
list_var1 = [4,5,1,2,6,2,4,7]
tup_var1 = (1,2,3)
dictionary_var1 = {"one":1, "two":1}

list_var1[1] # 5
print(list_var1[3:6])
# print(list_var1[8]) error
print(list_var1[-8])
print(list_var1.count(2))
print(len(list_var1))
list_var1.sort()
print(list_var1)
list_var2 = [9,0,8,4,5,1,2,3,1,1]
list_var3 = list_var1 + list_var2 # merged from list_var1 & list_var2
print(list_var3)

dictionary_var1["tup1"] = tup_var1
print(dictionary_var1["one"])
dictionary_var1["dic1"] = {"user":"user1", "address": "address1"}
dictionary_var1["dic1"]["grade"] = {"math":90, "physic":100}
print(dictionary_var1)
# bagaimana cara akses user di dalam dictionary_var1
print(dictionary_var1["dic1"]["user"])
print(dictionary_var1["dic1"]["grade"])
print(dictionary_var1["dic1"]["grade"]["math"])

# id in variable
num3 = 1
num4 = 1
print(id(num3), id(num4))

num4 = 10
print(id(num3), id(num4))

# id in tuple
tup1 = (1,2,3)
tup2 = tup1
tup3 = tuple(tup1)
print(id(tup1), id(tup2), id(tup3))

# tuple is immutable
# list is mutable