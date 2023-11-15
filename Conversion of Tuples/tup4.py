#Conversion Of lists of lists to tuples of tuples
list1=[]
num= int(input("Enter the number of lists:"))
for i in range(num):
    sublist=[]
    ele=int(input(f"Enter the number of elements in your list {i+1}"))
    for j in range (ele):
        ele= input(f"Enter an element for your list{i+1}")
        sublist.append(ele)
    list1.append(sublist) 
result=tuple(tuple(sub)for sub in list )    
print("Your Result is :",result)