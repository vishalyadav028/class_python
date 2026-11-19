# file = open("mast.txt", "r")
# data = file.read()

# print("Data of the file is:",data)



# write a prigram to read a text from a given file certificate.txt and find 
# whether it contains the word live.
# file = open("certificate.txt", "r")
# data = file.read()
# data = data.lower()

# if "live" in data:
#     print("yes live word is present in the file")
# else:
#     print("no")    






# open a file called report.txt in write mode.
# file = open("report.txt", "w")
# file.write("kafi achha se python learn lr rahe hai. mast\n")
# file.write("kaha ho bhai")



# file = open("report.txt", "a")
# file.write("\nkaho peeter parkar ka haal ba")





# file = open("report3543543461212w33.txt", "x")
# file.write("\nkaho peeter parkar ka haal ba")





# with open("report.txt", "r") as f:
#     data = f.read()
#     print("file data",data)







# with open("readba.txt", "r") as f:
#     naya = f.readlines()
#     print(naya)

    # line1 = f.readline()
    # line2 = f.readline()
    # line3 = f.readline()
    # line4 = f.readline()
    # line5 = f.readline()
    # data = f.read()

    # print("line 1: ",line1)
    # print("line 2: ",line2)
    # print("line 3: ",line3)
    # print("line 4: ",line4)
    # print("line 5: ",line5)
    # print("file data: ",data)






# Read only the line of bio.txt
# with open("bio.txt", "r") as f:
#     line1 = f.readline()
#     print("line 1", line1)







# print how many lines are present in notes.txt
import os

with open("notes.txt", "r") as f:
    list1 = f.readlines()
    print("output of readlines function: ",list1)
    print("number of lines in file: ",len(list1))

os.rename("mast.txt", "vishal")    




