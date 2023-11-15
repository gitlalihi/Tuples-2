#Python – Flatten tuple of List to tuple
mytuple=()
num_list=int(input("Enter your number of list:"))
for i in range(num_list):
    userinput=input(f"Enter your element{i+1},seperated by coma:").split()
    mytuple=mytuple+(userinput,)
print("Your tuple of list is :",mytuple) 
res=[]
for i in mytuple:
    res.extend(i)
res=tuple(res)
    

