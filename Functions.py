def password(a,b):
    print(a+b)
    print(a-6)
password(3,5)

def loginform(username,password):
        username = input("Enter the Name:")
        username = input("Enter the password:")
        if username == "Nharath" and password == "12345":
             print("Login susscfully")
        else:print("Invalid the lohin creaditinals")
loginform("Nharath","12345")


def form(name,age):
      print(f"My name is {name} and my age is thsi {age}")
form("Bharath",20)

# default functions

def data_base(name = "raju",age = "20", place = "hyd" ,loceted = "india"):
      print(f"my name is the {name},and my age is the {age},{loceted},and the {place}")
data_base(age = 23,name = "bharath")

# with keyword arguments
def fun_name(Name,age):
      print(f"My nae is {Name} and in in old years old {age}")
fun_name(age = 223,Name = "hai")
fun_name(Name="Bharath",age = 322)    


# * argumants functions

def fun_based(*ones):
    num = 0
    for i in ones:
                num = num + i 
    print(f"the sum is:{num}")
fun_based()




          
