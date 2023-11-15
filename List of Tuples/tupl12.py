#Python program to sort list of tuples aplhabetically
tlist=int(input("Enter your Number of Tuples:"))
tup_list=[]
for i in range(tlist):
    ele1=input("Enter your first element:")
    ele2=input("Enter your second element:")
    current_tuple=(ele1,ele2)
    tup_list.append(current_tuple)
print("Your input tuple is :", tup_list)

for x in range(len(tup_list)):
    for y in range(len(tup_list)-x-1):
        if tup_list[y][0]>tup_list[y +1] [0]:
            result= tup_list[y],tup_list[y +1]  =  tup_list[y +1],tup_list[y]

print(" Your sorted List of tuples is ",result)

