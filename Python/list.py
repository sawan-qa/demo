'''
my_list =['c','cpp','java']
print(my_list)
my_list.append('Python')
print(my_list)
'''
_range = int(input("Enter the List Item Quantity:"))
_list = []
for i in range(_range):
    fruits = input("Enter the fruits name:")
    _list.append(fruits)
else:
    print("All Item has been added successfully")
print("Your added list items are ", _list)
