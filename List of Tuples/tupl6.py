#Python – Extract digits from Tuple list
tlist=int(input("Enter your Number of Tuples:"))
tup_list=[]
for i in range(tlist):
    ele1=int(input("Enter your 1st element:"))
    ele2=int(input("enter your 2nd element:"))
    current_element=(ele1,ele2)
    tup_list.append(current_element)
print("Input tuplelist is :",tup_list)
k=int(input("Enter your digit you want to extract from your tuple list"))
extract_digits=[]
for tup in tup_list:
    for num in tup:
        if num==k:
            extract_digits.append(tuple(num))
print("Extracted digits are:",extract_digits)