# FUNCTION
# => blocks of processes

# Javascript
# function FunctionName(){
#     # blocks
# }

# Python
def function_name(args):
    # Argument
    # Result
    return


# Buatlah function untuk
# menyapa nama
print("==========================")


def say_hello(name: str):
    # apa data type dari name?
    print("hello " + name)
    return


say_hello("calman")

# tergantung linter
# beberapa linter bisa
# mendeteksi bahwa function di bawah
# adalah error
# linter: [autopep8, pylint, etc]
# say_hello(1)

# explicit define argument and result type
print("==========================")


def add(n1: int, n2: int) -> int:
    return n1 + n2


print(add(n2=10, n1=11))


# default value
def sub(n1: int = 10, n2: int = 11):
    return n2 - n1


print(sub())


def very_complex_function(n1, n2, n3, n4, n5=100):
    return n1 * n2 - n3**n4 / n5


print(very_complex_function(1, 2, 3, 4, 50))


# function documentation
def call_me(name: str) -> str:
    """call user name
    some long description\n
    Args:
        name (str): user name input
    Returns:
        str: user called
    """
    return name + ", hi"


# multiple variable length
print("==========================")


def sum_all(*args):
    # non key argument
    result = 0
    for num in args:
        result += num
    return result


print(sum_all(1, 2, 3))


# config file
# beragam
def some_function(**kwargs):
    # key argument
    print(kwargs)
    return


some_function(a=1, b=2, c=4, d=3, f=2)

# apakah function bisa mengeluarkan multi type output
print("==========================")


def multi_type(n1: int, n2: int) -> tuple:  # type: ignore
    return n1 * 100, "hello"


print(multi_type(1, 2))
# menangkap multi variable
num, word = multi_type(1, 2)
print(num, word)
num, _ = multi_type(100, 2)
print(num)

# anonymous function
# const func1 = () -> {return}
print("==========================")
func1 = lambda n1, n2: n1 * n2
print(func1(100, 4))

# local and global variable
print()
print("==========================")
global_variable = 100  # global variable


def change_number(input: int):
    global_variable = input  # local variable
    print("inside change_number function", global_variable)


change_number(10)
print("outside change_number function", global_variable)

# closure
print("==========================")


def change_global_number(input: int):
    global global_variable
    global_variable = input
    print("inside change_global_number function", global_variable)


change_global_number(10)
print("outside change_global_number function", global_variable)

# example
print("==========================")
print("confuse")
lamb_conf = 500


def confuse():
    n = 100
    # n = local variable untuk confuse()
    # n = global variable untuk lamb()
    lamb = lambda: n * 100 * lamb_conf
    print(lamb())


confuse()

# answer:
num_conf = 1200


def confuse2():
    n = 200
    print(n * num_conf)


confuse2()
# answer:

print("==========================")
print(type(confuse), type(func1))


# CALLBACK
def callback_func(name: str):
    print(name + " called me", "callback_func called")


def complex_func(name: str, callback):
    callback(name)


complex_func("user", callback_func)
complex_func("user", lambda nm: print(nm + " lambda called"))


# FUNCTION as return from other function
def return_function():
    return lambda: print("hello from lambda")


return_function()()
