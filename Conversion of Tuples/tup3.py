# Conversion of Tuples to Tuples Pairs
t=input("Enter your elements:").split(',')
userinput=tuple(t)
print("Your tuple is :",userinput)
tuple_pair=[(userinput[i],userinput[i+1])for i in range(len(userinput)-1) ]
print("Your Tuple pairs is :",tuple_pair)