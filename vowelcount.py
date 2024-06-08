x =input("enter the string")
y=x.lower()
print(y)
count=0
l=['a','e','i','o','u']
for i in y:
    if i in l:
        count=count+1
print(count)
