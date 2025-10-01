# without retrun function
def data(a,b):
    d = a+b
    print(d)
data(2,3)

# with retrun function
def data_base (a,b):
    d = a+b
    return d
data_base(6,6)
print(data_base(6,6))

def add(a,b):
    return (a+b)

def sub(c,d,e):
    return add(c,d)-e
print(sub(4,8,2))

def adding(a,b):
    return (a+b)
def subing(e,d,f):
    return adding(e,d)-f
print(subing(4,5,1))

# Local scope 

def fun1():
    A = 4
    B = 5
    print(A)
    print(B)
fun1()

def fun2(a,b):
    print(a)
    print(b)
fun2(3,3)

#Global scope

C = 45
def fun3(A,B):
    print(A)
    print(B)
    print(C)
fun3(4,6)
print(C)


c = 50
def fun4(a,b):
    print(a)
    print(b)
    print(c)
fun4(3,4)
print(c)






