#Python program to find tuples which have all elements divisible by K from a list of tuples
tlist=int(input("Enter your Number of Tuples:"))
tup_list=[]
for i in range(tlist):
    ele1=int(input("Enter your 1st element:"))
    ele2=int(input("enter your 2nd element:"))
    current_element=(ele1,ele2)
    tup_list.append(current_element)
print("Input tuplelist is :",tup_list)
k= int(input("Enter your number to divide your elements from your list of tuple:"))
tup2_list=[]

for x in range(tlist):
    ele1 = tup_list[x][0] / k
    ele2 = tup_list[x][1] / k
    current_element = (ele1, ele2)
    tup2_list.append(current_element)

print("New tuple list after dividing by", k, "is:", tup2_list)