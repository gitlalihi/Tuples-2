#Python – Cross Pairing in Tuple List
tlist1=int(input("Enter your Number of Tuples:"))
tup_list1=[]
for  x in range(tlist1):
    ele1=int(input("Enter your 1st element:"))
    ele2=int(input("enter your 2nd element:"))
    current_element1=(ele1,ele2)
    tup_list1.append(current_element1)
print("Input tuplelist is :",tup_list1)

tlist2=int(input("Enter your Number of Tuples:"))
tup_list2=[]
for y in range(tlist2):
    ele3=int(input("Enter your 1st element:"))
    ele4=int(input("enter your 2nd element:"))
    current_element2=(ele3,ele4)
    tup_list2.append(current_element2)
print("Input tuplelist is :",tup_list2)

crosspair_list=[(i[1],j[2]) for i in tup_list1 for j in tup_list2 if i[0] == j[0]]
print("Cross-pairing  of your elemnt is :",crosspair_list)