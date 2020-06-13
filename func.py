def func1(a,b):
    print(a,b)


func1(2,3)


def func2(name,lname):
    print(name,lname)

func2("asif","Ahmed")
func2(lname="Ahmed1us",name="Asif1us")

def f1():
    return 0;

abc = f1()
print(abc)



def func123(itemname,qty,*topping):
    print(itemname,qty,topping)


func123("Chicken Pizza",5,"olives","onions")


def func321(a,b):
    return a,b


ytk = func321(5,6)
print(type(ytk))