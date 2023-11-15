#Python – Consecutive Kth column Difference in Tuple List
tlist1=int(input("Enter your Number of Tuples:"))
tup_list1=[]
for  x in range(tlist1):
    ele1=int(input("Enter your 1st element:"))
    ele2=int(input("enter your 2nd element:"))
    current_element1=(ele1,ele2)
    tup_list1.append(current_element1)
print("Input tuplelist is :",tup_list1)
k=1
result=[]
for i in range(len(tup_list1)-1):
        diff = abs(tup_list1[i+k][1] - tup_list1[i][1])
        result.append(diff)
print(" Your extracted list is :",result)        