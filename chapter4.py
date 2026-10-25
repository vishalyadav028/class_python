# dict={
#     "name":"vishal",
#     "cgpa":9.6,
#     "marks":96
# }
# print(dict)


# info={
#     "key":"values",
#     "name":"vishal",
#     "learning":"coding",
#     "age":20,
#     "adult":True,
#     "marks":94.4,
#     "subject":["phy","che","bio"],
#     "topics":"tuple"
# }
# print(info)
# print(info["name"])
# print(info["topics"])
# print(info["subject"])


# info={
#     "name":"vishal",
#     "subject":["c","c++","java"],
#     "topics":["operator","condition"],
#     12.99:94.4
# }
# info["name"]=23
# info["surname"]="kumar"
# print(info)


# num_dict={}
# num_dict["name"]="apnacollege"
# print(num_dict)
# print(type(num_dict))


# student ={
#     "name":"vishal",
#     "score":{
#         "c":98,
#         "phy":97
#     }
# }


# student ={
#     "name":"vishal",
#     "subject":{
#         "phy":97,
#         "chem":86,
#         "math":94
#     }
# }
# print(student["subject"]["chem"])
# print(len(student))
# print(list(student.keys()))



# student ={
#     "name":"vishal",
#     "subject":{
#         "phy":97,
#         "chem":86,
#         "math":94
#     }
# }
# print(student.values)
# # keys()
# print(list(student.values()))

# # values()
# print(list(student.values()))

# # items()
# print(list(student.values()))

# # get()
# print(student["name"])
# print(student.get("name"))

# # update()
# student.update({"city":"delhi"})
# print(student)

# # update()
# new_dict={"city":"delhi","age":10}
# student.update(new_dict)
# print(student)


# SETS
# print("__________________________________")
# collection={1,2,3,4,"hello","world"}
# print(collection)
# print(type(collection))
# print(len(collection))
# print("____________________________________")

# # set.add()
# collection=set()
# collection.add(1)
# collection.add(2)
# collection.add(3)
# collection.add(4)
# print(collection)
# print("_____________________________")

# # set.remove
# collection.remove(2)
# print(collection)
# print("_______________________________")

#set.clear()
# collection.clear()
# print(len(collection))
# print("_____________________________")

# set.pop
# print(collection.pop())
# print(collection.pop())
# print(collection.pop())
# print("_______________________")

# set.union(set)
# set1={1,2,3,3}
# set2={2,3,4}
# print(set1.union(set2))
# print(set1)
# print(set2)

# set.intersection
# set1={1,2,3,4}
# set2={2,3,4}
# print(set1.intersection(set2))

# doct={
#     "cat":"smal animal",
#     "table":["a piece of future","list is of fact"]
# }
# print(dict)


# sub={
#     "python","java","c++"
# }
# print(sub)
# print(len(sub))

# marks={}
# y =int(input("Enter phy: "))
# marks.update({"phy":y})

# y =int(input("Enter math: "))
# marks.update({"math":y})

# y =int(input("Enter chem: "))
# marks.update({"chem":y})
# print(marks)
# print(type(marks))

# vall={9,9.25,8,8.0}
# print(vall)
# vall ={9,"9.0"}
# vall ={"9",9.0}
# print(vall)