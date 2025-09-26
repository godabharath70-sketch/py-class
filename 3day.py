# Student_id = 21
# Student_name = "Bharath"
# Student_age = 20

# quiz_score = 80
# assigment_score = 75
# exam_score = 90

# Student_attendance = 60

# Total_count = quiz_score + assigment_score + exam_score 

# avg_score = Total_count/3


# student_passed = avg_score > 75

# Student_attendance += 1

# Student_eligibility = student_passed >= 90 and Student_attendance


# print("---------")
# print(f"Name:{Student_name}")
# print(f"total score:{Total_count}")
# print(f"avg_score:{avg_score}")
# print(f"student_passed :{student_passed }")
# print(f"Student_attendance:{Student_attendance}")
# print(f"Student_eligibility:{Student_eligibility}")


# a = 22
# b = 11
# c = a+b
# q = bool(c)
# print(q)
# print(type(q))

# x = 200
# y = x
# z = float(y)
# print(z)
# print(type(z))


# A = "110"
# B = int(A)
# print(B)
# print(type(B))

# A = 2
# print(A)
# print(type(A))

# A = 3.3
# B = str(A)
# print(B)
# print(type(B))

# A = True
# B = int(A)
# print(B)
# print(type(B))

# age  = 20
# if age <= 22:
#     print("You can vote")
# else:
#     print("You cannot vote")

# Data = int(input("Enter the data:"))
# print(Data)
# print(type(Data))

# Marks = float(input("Enter the GPA:"))
# print(Marks)
# print(type(Marks))

# Age = int(input("Enter the age:"))
# result = "Done to vote" if Age >= 33 else "Not done to vote"
# print(result);

# Age = 22
# if Age <= 21:
#     print("Vote")
# else:
#     print("Not vote")    


# fruites = ["Apple","banana","orange","cherry","mangao"]
# for u in fruites:
#     print(u);

# my_dict = {"name":"Bharath","age":"34"}
# for y in my_dict.values():
#     print(y)

# for i in range(2,22):
#     print(i)

# for k in range(1,10,4):
#     print(k)

# for k in range(23,1,-1):
#     print(k)

# count = 0
# while count <= 88:
#     print(count)
#     count+=5


# amount = 2
# while amount <=  22:
#     print(amount)
#     amount+=2
    
# print("HOOO")
# for l in range(2,33,6):
#     print(l)

# for u in range(1,99):
#     if u == 50:
#         break
#     print(u)

# for k in range(1,5):
#     for o in range(1,5):
#         print(f"{k} X {o} = {k * o}")

# for l in range(100,120):
#     for t in range(100,120):
#         print(f"{l} = {t} == {l + t}")
        


# u_list = [1,2,3,4,5,6]
# print(u_list)

# l_list = [1,2,3,4,5,6,7,8,9,10]
# l_list.append(11)
# print(l_list)

# l_list = [1,2,3,4,5]
# l_list.extend([6,7,8,9])
# print(l_list)

# l_list = [1,2,3,4,6,7,8]
# l_list.insert(4,5)
# print(l_list)

# l_list = [9,69,49,2,1,3,4,2,2,5,6]
# l_list.sort()
# print(l_list)

# l_list = [1,29,44,66,55,14,46]
# l_list.reverse()
# print(l_list)

# l_list = [3,2,1,4,5]
# l_list.remove(4)
# print(l_list)

# l_list  = [2,3,4,7,66,4]
# l_list.clear()
# print(l_list)

# l_list = [1,2,22,3,4,5,6]
# l_list.pop()
# print(l_list)


# l_list = [22,33,445,6,7,8,1,2,2,2,4,5,4,3,4,4,4]
# o_list = l_list.count(4)
# print(o_list)

# my_tuple = (1,2,3,3,3,3,4,5,6)
# U_tuple = my_tuple.count(3)
# print(U_tuple)

# my_tuple = (1,2,3,4,5)
# I_tuple = my_tuple.index(5)
# print(I_tuple)

# my_dict = {"Name":"Bharath","Age":"20","More":"confidente","JOB":"IT,IT,IT,IT,IT"}
# my_data = my_dict.items()
# for j in my_data:
#     print(j[0])
 
# my_dict = {"A":"Apple","B":"Ball"}
# my_data = my_dict.fromkeys(["A","B"],"DUDE")
# print(my_data)


# n_sete = {122,2,3,4,5}
# print(id(n_sete))

# My_dqct = {"NAme":"Bharath","Age":12,"Age":12}
# My_dct = My_dqct.setdefault("Age",22)
# print(My_dct)

# my_data = {"N":"Nanao","Plotnum":11}
# my_up = my_data.get("Plotnum",23)
# print(my_up)

# my_set = {1,2,2,2,3,4,5,3}
# my_set2 = {6,7,8,9,10}
# print(my_set2.intersection_update(my_set))
# print(my_set - my_set2)
# print(my_set2 - my_set)


# my_set1 = {1,2,3,4,5,3,3}
# my_set2 = {6,6,7,8,9}
# print(my_set1.difference(my_set2))
# print(my_set1)
# print(my_set2)

# my_set1 = {1,2,3,4,5,3,3}
# my_set2 = {6,6,7,8,9}
# print(my_set1.union(my_set2))


my_scores = [23,34,22]
total= sum(my_scores)
no_scores = len(my_scores)
avg = total/no_scores
max_value = max(my_scores)
print(total,avg,max_value)


