class MyNum:
    def __init__(self,x):
        self.__x = x
        print(self.__x)

    def __lt__(self, other):
        print("__lt__")
        # return self.__x < other

    def __le__(self, other):
        print("__le__")
        # return self.__x <= other

    def __eq__(self, other):
        print("__eq__")
        # return self.__x == other

    def __ne__(self, other):
        print("__ne__")
        # return self.__x != other

    def __gt__(self, other):
        print("__gt__")
        # return self.__x > other

    def __ge__(self, other):
        print("__ge__")
        # return self.__x >= other

x = MyNum(100)
x < 10
x <= 10
x == 10
x != 10
x > 10
x >= 10