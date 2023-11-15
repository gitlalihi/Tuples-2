#Python Program to Cover  tuple into list by adding the given string after every element
t=input("Enter your elements:").split(',')
userinput=tuple(t)
print("Your tuple is :",userinput)
k=input("Enter your string to be added")
result=[ele for i in userinput for ele in (i,k)]
print("Your coverted tuple to list ids :",result)