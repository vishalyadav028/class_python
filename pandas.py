# __________________________________Value access krna sikha___________________________
# import pandas as pd
# a = pd.Series([5,15,20])
# print(a.values)



# import pandas as pd
# a = pd.Series([5,15,20])
# print(a.values+5+2)
# print(len(a))



# import pandas as pd
# a = pd.Series([20,10,50],index=["a","b","c"])
# print(a.index[0])


# import pandas as pd
# a = pd.Series([20,10,50])
# print(a.index[0])

# import pandas as pd
# a = pd.Series([20,10,50])
# print(a[0])


# import pandas as pd
# joy = pd.Series(["vishal","prince","rakesh"])
# print(joy.iloc[0])

# __________________________________Value access krna sikha___________________________
#-----All indexes
import pandas as pd
num = pd.Series(['vishal','ritik','abhi'],
                index=['a','b','c'])
# print(num['a'])  
# print(num['b'])  
print(num.index[1])
print(num.dtype)
print(num.size)
print(num.sum)




# print(s.dtype)      # Data type
# print(s.size)       # Total elements
# print(s.sum())      # Total marks
# print(s.mean())     # Average marks
# print(s.max())      # Maximum marks
# print(s.min())      # Minimum marks
