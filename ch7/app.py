# single responsibiliy:
# bagaimana kita memisahkan code 
# berdasarkan domain atau specific function

class Order():
    def __init__(self):
        pass
    def create_order(self):
        pass

class Product():
    def __init__(self):
        pass
    def check_product(self):
        pass

def add(a, b):
    # func ini hanya melakukan
    # penjumlahan
    a = a**2
    return a + b

# Open close principle
# open untuk diinheritkan 
# close untuk dimodif / diubah

# contoh salah
# class Shape():
#     def __init__(self, type, **kwargs):
#         self.type = type
#     def area(self):
#         if self.type == "circle":
#             return 
#         else self.type == "square":
#             return 

class Shape():
    def __init__(self):
        pass
    def area(self):
        pass

class Circle(Shape):
    def __init__(self):
        pass
    def area(self):
        pass
