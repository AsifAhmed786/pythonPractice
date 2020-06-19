def func1(x,y):
    return x*y

print(func1(5,6))

def func2(x,y=5):
    return x*y

print(func2(5))

def func3(x,y,*d):
    return x,y,d

print(type(func3(4,5,6,7,8)))
abc = func3(4,5,6,7,8)
for a in abc:
    print(a)
print(abc[0])

abc1 = True
while(abc1):
    print("hello")
    abc1 = False
