#Python – Kth Column Product in Tuple List
tlist1=int(input("Enter your Number of Tuples:"))
tup_list1=[]
for  i in range(tlist1):
    ele1=int(input("Enter your 1st element:"))
    ele2=int(input("enter your 2nd element:"))
    current_element1=(ele1,ele2)
    tup_list1.append(current_element1)
print("Input tuplelist is :",tup_list1)
k=2
product=1
for tup in tup_list1:
    product=product*tup[k]
print("Your prduct from the kth colomn",product)    

