#Coversion to Float Values
t=input("Enter your elements:").split(',')
userinput=tuple(t)
print("Your tuple is :",userinput)
res=float('.'.join(str(ele) for ele in userinput))
print("Your coversion to float values are:",res)