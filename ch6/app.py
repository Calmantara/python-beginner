# Membuat class


from abc import ABC, abstractmethod
from ctypes import Array
from pyclbr import Class
from re import sub


class MotorCycle:
    def __init__(self, product: str, wheel: int, fuel: str) -> None:
        """how to declare this class
        this class is using props:
            1. wheel
            2. fuel
        """
        # public property
        self.product = product
        self.wheel = wheel
        self.fuel = fuel

        # protected
        self._product = "protected " + product

        # convention __ private attribute
        # private: hanya bisa diakses di dalam class
        self.__fuel = "private " + fuel

    # public method
    def detail(self):
        print("motor product: " + self.product)
        print("motor wheels: " + str(self.wheel))
        print("motor fuel: " + self.fuel)

    def gas(self):
        # SELF adalah cara kita mendefine
        # props / methods kita dalam scope
        # class object kita
        # print(self.__fuel)
        pass


# product:
# Yamaha -> tune_up()
# Honda -> bore_up()
#   detail: hanya menampilkan product + fuel
# Suzuki -> speed_up()


# Inherit Class
class Honda(MotorCycle):
    def __init__(self, product: str, wheel: int, fuel: str) -> None:
        self.product = product
        self.wheel = wheel
        self.fuel = fuel

    def bore_up(self):
        print("gass bore up: " + self.fuel)

    # function override
    def detail(self):
        print("motor product: " + self.product)
        print("motor fuel: " + self.fuel)


class Yamaha(MotorCycle):
    def __init__(self, product: str, wheel: int, fuel: str) -> None:
        self.product = product
        self.wheel = wheel
        self.fuel = fuel

    def tune_up(self):
        print("tune up:" + self.fuel)


beat = Honda("Honda", 2, "Bensin")
# mio = MotorCycle("Yamaha", 2, "Bensin")
mio = Yamaha("Yamaha", 2, "Bensin")
# calls method
beat.detail()
mio.detail()

# access fuel
# print(beat.__fuel) # gonna be error
beat.gas()
# print(beat._product)


# class as input parameter
def service(motor: MotorCycle):
    print(motor.product, motor.fuel)


service(beat)

# SOLID PROGRAMMING
# https://realpython.com/solid-principles-python/


class User(ABC):
    @abstractmethod
    def greet():
        pass

    @abstractmethod
    def get_name() -> str:
        pass


class Student(User):
    def __init__(
        self,
        first_name: str,
        last_name: str,
    ) -> None:
        super().__init__()
        self.first_name = first_name
        self.last_name = last_name

        # init grade
        self.__grade = []

    def greet(self):
        print("hello, nice to meet you", self.last_name)

    def get_name(self):
        return self.first_name + " " + self.last_name

    def grading(self, subject: str, grade: int):
        self.__grade.append({subject, grade})

    def get_all_grades(self):
        return self.__grade


def TestUser(usr: User):
    print("hello", usr.get_name())


std1 = Student("Student", "1")
TestUser(std1)

std1.grading("Math", 90)
std1.grading("Physics", 100)
std1.grading("Chemistry", 85)
print(std1.get_all_grades())
