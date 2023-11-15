#Python program to find Tuples with positive elements in List of tuples
tlist=int(input("Enter your Number of Tuples:"))
tup_list=[]
for i in range(tlist):
    ele1=int(input("Enter your 1st element:"))
    ele2=int(input("enter your 2nd element:"))
    current_element=(ele1,ele2)
    tup_list.append(current_element)
print("Input tuplelist is :",tup_list)
extract_tuplist=[i for i in range(tlist)if all(ele >0 for ele in i)]
print("Your postive tuple are:" ,extract_tuplist)