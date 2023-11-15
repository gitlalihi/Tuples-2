#Python | Count tuples occurrence in list of tuples
tlist=int(input("Enter your Number of Tuples:"))
tup_list=[]
for i in range(tlist):
    ele1=int(input("Enter your 1st element:"))
    ele2=int(input("enter your 2nd element:"))
    current_element=(ele1,ele2)
    tup_list.append(current_element)
print("Input tuplelist is :",tup_list)
check_element=input("Enter your element")
newtup_list=[i for i in range(tlist)if i ==check_element]
print("Occurences of your elemnt is :",newtup_list)