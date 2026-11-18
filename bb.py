# import pandas as pd
# a = pd.DataFrame({"NAME": ["vishal",'Ritik','Sankar','Abhi'],
#                   "AGE": [19,20,18,20],
#                   "ADDRESS" : ['mathiya','bankatti','patna','gaya']})
# print(a)




# import pandas as pd
# a = pd.DataFrame([
#     ['vishal',18],
#     ['ritik',20],
#     ['sankar',18],
#     ['abhi',20]
#     ],
#     columns=["name",'age'])

# print(a)



import pandas as pd
n = pd.DataFrame({
    "Name": ["vishal", "ritik", "sankar"],
    "Age": [19, 20, 18],
    "course": ["bca", "mca", "b-tech"]
})

# print(n)

# ___________ Properties ___________

# print(n.shape)
# print(n.columns)
# print(n.index)
# print(n.dtypes)
# print(n.values)
# print(n.size)
# print(n.ndim)
# print(n.empty)

# ___________ Methods ___________

# print(n.head(2))
# print(n.tail(2))
# print(n.info())
# print(n.describe())
# print(n.isnull())

# print(n.sum(numeric_only=True))
# print(n.mean(numeric_only=True))
# print(n.min())
# print(n.max())


print(n.loc[0])
print(n.iloc[0])
