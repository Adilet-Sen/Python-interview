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