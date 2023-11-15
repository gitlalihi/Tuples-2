#Conversion of Tuples of tuples(nested tuples) into a dictionary
num_tuples=int((input("Enter the number of tuples:")))
tuples_lists=[]
for i in range (num_tuples):
    element=input(f"Enter the elemnts {i+1}of the tupleseperated by a comma:")
    input_tuple=tuple(map(int,element.split(',')))
    tuples_lists.append(input_tuple)
tuples_of_tuple=tuple(tuples_lists)
print("Tuples of tuples:",tuples_of_tuple)
res=[{'key': x[0],'value': x[1]} for x in tuples_of_tuple]
print("The converted didctionary is ", res)    