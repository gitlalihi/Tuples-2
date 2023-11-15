#Python- Combinations of Sum with Tuples inlist of tuple
tlist=int(input("Enter your Number of Tuples:"))
tup_list=[]
for i in range(tlist):
    ele1=input("Enter your first element:")
    ele2=input("Enter your second element:")
    current_tuple=(ele1,ele2)
    tup_list.append(current_tuple)
print("Your input tuple is :", tup_list)
result=[]
for x in range (len(tup_list)):
    for y in range(x+1 ,len(tup_list)):
        result.append((tup_list[x][0] + tup_list[y][0],tup_list[x][1] + tup_list[y][1]))
print("Your summation combinations are:",result)        