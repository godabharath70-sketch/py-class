def main_fun(w,r):
    print(w+r)
    print(w*r)
    print(w-r)
    print(w/r)
main_fun(3,4)
main_fun(9,8)
main_fun(10,2)
    

def name(Name,email,):
    print(f"My name is {Name} and my email is this {email}")
name("Bharath","@godabharath")
name("Joshan","@jooshan")


# without lambda function

def adding(a,b):
    return a+b
print(adding(6,6)) 

# with lambda function

A = lambda a,b : a+b
print(A(5,6)) 

print((lambda x,v:x+v)(9,9))

is_data = lambda num:num % 2==0
print(is_data(10))
print(is_data(15))

print((lambda a:a % 3 == 0 )(39))