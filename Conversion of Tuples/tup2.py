#Python Program to convert tuple matrix into tuple list
matrix = []
num_rows = int(input("Enter the number of rows: "))
num_cols = int(input("Enter the number of columns: "))
for i in range(num_rows):
   row = []
   for j in range(num_cols):
        element = int(input(f"Enter element at row {i + 1}, column {j + 1}: "))
        row.append(element)
matrix.append(tuple(row))
print("Input Matrix:",matrix)
for row in matrix:
    print(row )

tup_list=[]
for i in range(matrix):
    ele1=input("Enter your first element:")
    ele2=input("Enter your second element:")
    current_tuple=(ele1,ele2)
    tup_list.append(current_tuple)
print("Your input tuple is :", tup_list)    