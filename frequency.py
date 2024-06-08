input_str =input("enter the string")
result={}
for i in input_str:
    if i in result:
        result[i]+=1
    else:
        result[i]=1
print(result)
