#Python- Custom Sorting in list of Tuples
tlist=int(input("Enter your Number of Tuples:"))
tup_list=[]
for i in range(tlist):
    ele1=input("Enter your first element:")
    ele2=input("Enter your second element:")
    current_tuple=(ele1,ele2)
    tup_list.append(current_tuple)
print("Your input tuple is :", tup_list)

for x in range (len(tup_list)):
    for y in range(x+1,len(tup_list)):
        if tup_list[y][0]<tup_list[y+1][1] or((tup_list[y][0]==tup_list[y+1][1] ) and (tup_list[y][1]>tup_list[y+1][1])):
            tup_list[y],tup_list[y+1]=tup_list[y+1],tup_list[y]
print("Your Custom sorting in list of tuple is :",tup_list)
