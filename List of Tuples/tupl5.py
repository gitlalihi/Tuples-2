#Python | Remove duplicate lists in tuples (Preserving Order)
tlist=int(input("Enter your Number of Tuples:"))
tup_list=[]
for i in range(tlist):
    ele1=int(input("Enter your 1st element:"))
    ele2=int(input("enter your 2nd element:"))
    current_element=(ele1,ele2)
    tup_list.append(current_element)
print("Input tuplelist is :",tup_list)
temp=set()
result=[ele for ele in tup_list if not (ele in temp or temp.add(ele))]
print("Your tuple stfer removing duplicates is :",result)