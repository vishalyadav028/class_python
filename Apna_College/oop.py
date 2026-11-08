# class student:
#     name ="vishal"

# s1 = student()
# print(s1.name)  

# s2 = student()
# print(s2.name)








# class car:
#     color ="blue"
#     brand ="marcedes"

# car1 =car()
# print(car1.color)

# car2 =car()
# print(car2.brand)









# class student:
#     # dafault constructor
#     def __init__(self):
#         pass
#     # parameterize constructor
#     def __init__(self, fullname, marks):
#         self.fullname = fullname
#         self.marks = marks
#         print("adding new student in database....")

# s1 = student("vishal",98)
# print(s1.fullname,s1.marks)  

# s2 = student("prince",99)
# print(s2.fullname)
# print(s2.marks)










# ____________class & instance attribute_______________
# class student:
#     # dafault constructor
#     def __init__(self):
#         pass
    
#     # parameterize constructor
#     def __init__(self, fullname, marks):
#         self.fullname = fullname
#         self.marks = marks
#         print("adding new student in database....")

# s1 = student("vishal",98)
# print(s1.fullname,s1.marks)  

# s2 = student("prince",99)
# print(s2.fullname)
# print(s2.marks)




# class student:
#     colege_name ="ABC College"
  
#     def __init__(self, fullname, marks):
#         self.fullname = fullname
#         self.marks = marks
#         print("adding new student in database....")

# s1 = student("vishal",98)
# print(s1.fullname,s1.marks)  

# s2 = student("prince",99)
# print(s2.fullname)
# print(s2.marks)
# # print(s2.colege_name)
# print(student.colege_name)










# class student:
#     colege_name ="ABC College"
#     name ="anonymous"
  
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#         print("adding new student in database....")

# s1 = student("vishal",98)
# print(s1.name)








# --------------method-----------------
# class student:
#     college_name ="ABC College"

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def welcome(self):
#         print("welcome student", self.name)

#     def marks(self):
#         return self.marks   

# s1 = student("vishal", 97)
# print(s1.name)
# s1.welcome()
# print(s1.marks())







# Q1. Create a Student class that takes name and marks of 3
# subjects as arguments in the constructor. Then create a
# method to print the average.
# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#             print("hi", self.name, "your avg score is:",sum/3)

# s1 = student("tony stark", [98, 97, 99])            
# s1.get_avg()

# s1.name = "ironman"
# s1.get_avg()






# -------------------static method-----------------
# class student:

#     @staticmethod
#     def hello():
#         print("hello")

# s1 = student()
# s1.hello()        






# -----------abstruction-----------------
# class car:
#     def __init__(self):
#         self.acc = False
#         self.brk = False
#         self.clutch = False

#     def start(self):
#         self.clutch = True
#         self.acc = True
#         print("car start..")

# car1 = car()
# car1.start()        






# -----------abstruction-----------------
# Q2. Create an Account class with 2 attributes: balance and
# account number. Create methods for debit, credit and printing
# the balance     

class Account:
    def __init__(self, bal, acc):
        self.balance = bal
        self.account_no = acc

        # debit method
        def debit(self, amount):
            self.balance -= amount
            print("Rs.", amount, "was debited")
            print("total balace =",self.get_balance())


         # debit method
        def credit(self, amount):
            self.balance += amount
            print("Rs.", amount, "was creadited") 
            print("total balace =",self.get_balance())


        def get_balance(self):
            return self.balance



acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(1000)