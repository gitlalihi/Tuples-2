#Python -Flatten Tuple list to strings
mytuple=()
num_list=int(input("Enter your number of list:"))
for i in range (num_list):
    userinput=input(f"Enter your element{i+1},seperated by coma:").split()
    mytuple=mytuple+(userinput,)
print("Your tuple of list is :",mytuple) 


result=''.join(i for tup in mytuple for i in tup)
print("Tuple list conversion to string is :",result)
