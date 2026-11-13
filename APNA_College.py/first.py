# type conversion

# a =float("2")
# b = 8.01
# print(a+b)
# print(type(a))





# -----------------empty string------------------
# strp =""
# print(type(strp))
# -----------------string------------------
# str1 = "apna"
# str2 = "college"
# final_str = str1 + str2
# print(final_str)


# str =" i love python "
# print(str.upper())
# print(str.lower())
# print(str.title())
# print(str.find("p"))
# print(str.count("o"))
# print(str.replace("python","java"))
# print(str.capitalize())
# print(str.strip())
# print(str.rstrip())
# print(str.lstrip())
# print(str.index("p"))
# print(str.endswith(" "))
# print(str.startswith("p"))




# -----------------empty list------------------
# list1 =[]
# print(type(list1))
# -----------------list------------------
# list1 =[10,30,20,50]

# accendacing
# print(list1.append(80))  
# list1.sort()

# Descending
# list1.sort(reverse=True)
# print(list1)

# index ke possition pe add krta hai
# list1.insert(1,50)
# print(list1)

# list se values ko remove krta hai
# list1.remove(2)
# print(list1)

# position delete krta hai
# list1.pop(2)
# print(list1)


# -----------------empty tuple-----------------
# tup =()
# print(type(tup))
# -----------------tuple-----------------







# -----------------empty dictionary-----------------
# num ={}
# print(type(num))
# -----------------dictionary-----------------
# info ={
#     "name":"apnacollege",
#     "subject":["python","c","java"],
#     "topics": ("dict","set"),
#     "age":35,
#     "is_adult": 94.4
# }

# print(info)
# print(info["subject"])
# print(info["age"])
# info["name"] ="vishal"
# print(info["name"])
# info["surname"] ="yadav"
# print(info["surname"])




# ------nested dictionary-------
# student ={
#     "name": "vishal kumar",
#     "subject":{
#         "phy":98,
#         "chem":97,
#         "maths":67
#     }
# }

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.update({"age":"12"}))
# print(student)
# print(student.get("name"))








# -----------------empty sets-----------------
# sets = set()
# print(type(sets))
# -----------------set-----------------
# cool ={1, 2, 3, 4, "hello", "world",4,5}
# print(len(cool))
# print(type(cool))

# print(cool.add(10))
# print(cool.remove(4))
# print(cool)
# print(cool.clear())
# print(cool)
# print(cool.pop(1))
# print(cool)



# -----------------loop-----------------
# heros =["ironman","thor","superman","batman"]

# i =0
# while i< len(heros):
#     print(heros[i])
#     i += 1




# nums =[1,4,9,16,25,45,36]
# x = 36

# i = 0
# while i < len(nums):
#     if(nums[i] == x):
#         print("found ad idx")
#         i += 1




# n= int(input("enter number:"))
# for i in range(1,11):
#     print(n*i)






# -----------------function-----------------
# def cal_sum(a,b):
#     return a+b
# sum = cal_sum(10,5)
# print(sum)

# def print_hello():
#     print("hello")

# print_hello()
# print_hello()
# print_hello()




# def cal(a, b, c):
#     sum = a+b+c
#     avg = sum/3
#     print(avg)
#     return avg

# cal(10,5,8)



# cities =["delhi","gurgaon","noida","pune"]
# heros = ["thor","ironman","captian america"]

# def print_len(list):
#     print(len(list))

# print_len(cities)
# print_len(heros)    







# -----------------Recursion-----------------
# def show(n):
#     if(n == 0):
#         return
#     print(n)
#     show(n - 1)

# show(5)