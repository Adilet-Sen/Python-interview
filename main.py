# 1 - 4, 6
decel = 0
decelpoint = 0.5
strings = "awdawd"
tupl = (1,2,3,4)
lists = [1,2,3,4]
dictans = []
def some_func(list: list = []):
    list.append(1)
    return list

print(some_func([]), id([]))
print(some_func() , id(some_func()))
print(some_func(), id(some_func()))
print(some_func(), id(some_func()))
# 5
def some_phonc(l1,l2,**l3):
    print("l1: ", l1)
    print("l2: ",l2)
    print("l3: ", l3)
some_phonc(1,2, text="text")
# 7
def sum_arg(a, b): return a + b
# аналог 
sum_arg = lambda a, b: a + b

# 8
import copy

# original object
original = [[1, 2], [3, 4]]

# shallow copy
shallow_copy = copy.copy(original)

# deep copy
deep_copy = copy.deepcopy(original)

# modify the original object
original[0][0] = 9

print("Original:", original, id(original))
print("Shallow copy:", shallow_copy, id(shallow_copy))
print("Deep copy:", deep_copy, id(deep_copy))

#Original: [[9, 2], [3, 4]]
#Shallow copy: [[9, 2], [3, 4]]
#Deep copy: [[1, 2], [3, 4]]

class MyClass:
    count = 0
    value = 0
    def __init__(self, value):
        self.value = value
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count + cls.value

obj1 = MyClass(10)
obj2 = MyClass(20)
print(MyClass.get_count()) 