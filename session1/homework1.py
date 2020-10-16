# class MyClass:
#     def __new__(cls, *args):
#         if 'C' in args:
#             return object
#         else:
#             return super().__new__(cls)
#
#     def __init__(self, *args):
#         self.arg = args

class MyClass:
    def __new__(cls, *args):
        print('Class __new__ obj ')
        if ((len(args) == 1) and ('A' in args or 'B' in args)) or (len(args) == 2 and 'A' in args and 'B' in args):
            obj = super().__new__(cls)
        elif (len(args) == 1 and 'C' in args) or (len(args) == 2 and 'C' in args and 'B' in args):
            # obj = object.__new__(cls)
            obj = object()
        else:
            raise Exception('Wrong using')
        return obj

    def __init__(self, *args):
        print('Init of MyClass')

mc1 = MyClass("A")
mc2 = MyClass("A","B")
not_mc1 = MyClass("C")
not_mc2 = MyClass("B","C")

print(mc1)
print(mc2)
print(not_mc1)
print(not_mc2)


"""
Нужно написать класс который будет создавать объект этого же класса если в конструкторе будет присутствовать
 str ""А"" или ""В"" но не что либо другое. 
Если в конструктор передается "С" или с "В" также передается "С" то должен быть создан простой базовый обьект (object).
"""