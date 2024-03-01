# ITERTOR
mytup = (1, 2, 3, 4, 5)
print("accessing memory directly")
print(mytup[0])  # 0
print(mytup[1])  # 0 1
print(mytup[2])  # 0 1 2
print(mytup[3])  # 0 1 2 3
print(mytup[4])  # 0 1 2 3 4

myiter = iter(mytup)
print("accessing memory using iterator")
try:
    print(next(myiter))  # last visit = 0
    print(next(myiter))  # last visit = 1
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))
    print(next(myiter))  # would be error, end of iterator
except:
    print("end of iterator")

mytup2 = (1, 2, 3, 4, 5)
myiter2 = iter(mytup2)
for tup in myiter2:
    print(tup)
# apakah kita memerlukan efficiency dalam CPU?
# if yes, use iterator
# if tolerable, it's okay not to use iterator
# conclusion: best practice to use iterator


# GENERATOR
# benefit dari iterator ketika kita menggunakan
# generator akan sama saja
def genIter():
    yield 1
    yield 2
    yield 3
    yield 4


myiter3 = genIter()
try:
    print("iterate using generator")
    print(next(myiter3))
    print(next(myiter3))
    print(next(myiter3))
    print(next(myiter3))
    print(next(myiter3))
except:
    print("end of iteration")


# Decorator
# dalam python
# kita melihat semua dalam bentuk OBJECT:
#   Function
#   Class
#   String


def add(a, b):
    return a + b


def sub(a, b):
    return b - a


a = 10
b = 100
print("DECORATOR EXAMPLE")
execute = add
if a < b:
    execute = sub
print(execute(a, b))

dic = {"add": add, "sub": sub}
print(dic["add"](a, b))


# Assignment: STYLE DECORATOR
# buatlah suatu program python
# yang akan menerima masukan dari user
# berupa shape type
# if shape circle => meminta masukan berupa jari jari
# if shape square => dia akan meminta masukan berupa side
# memberikan output area
