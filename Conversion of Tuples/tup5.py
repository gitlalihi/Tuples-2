#Conversion of Lists of lists to custom list of tuples
list1=[]
num= int(input("Enter the number of lists:"))
for i in range(num):
    sublist=[]
    ele=int(input(f"Enter the number of elements in your list {i+1}"))
    for j in range (ele):
        ele= input(f"Enter an element for your list{i+1}")
        sublist.append(ele)
    list1.append(sublist) 
add_list=["jk","is","jk"]
res=[]
for x in range(0,len(add_list)):
    for y in range (0,len(list1[x])):
        res.append(add_list[x],list1[x][y])
print(" Your lists of tuple is :",res)        