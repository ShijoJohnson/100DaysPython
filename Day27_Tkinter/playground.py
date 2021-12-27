# def add(*args):
#     sum = 0
#     for i in args:
#         sum+=i
#     return sum
#
# print(add(1,2,3,4,4))


# def calculate(n, **kwargs):
#     # print(kwargs)
#     # for key, value in kwargs.items():
#         # print(key)
#         # print(value)
#     n += kwargs["add"]
#     n *= kwargs["mutiply"]
#     print(n)
#
# calculate(2, add= 3, mutiply =2)

class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        # self.model = kw["model"]
        self.model = kw.get("modelllll") # this way initialization wont fail if no value is not sent


my_car = Car(make ="Toyota", model = "Camry")
print(my_car.make, my_car.model)


