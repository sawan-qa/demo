#Accessing Elment of a list 
_list=["Sawan","Atul","Garima","Kajal","Nishant"] #Single Dimensional List 
print(_list[1]) # Start with 0 Index
#Output will be "Atul"
print("Accessing Element in a Multi-Dimensional List")
_name=[["Sawan","Khushboo"],"Atul","Garima","Kajal","Nishant"] #Two Dimensional List
print(_name[0][1])
#Output will be khusboo
#Accessing Element via negative indexing i.e. used when last data not known
print(_name[-1])

my_list_3 =[["1","2","3"],[["a","b","c"],"5","6"]]
#Access the value of b in the above list
print(my_list_3[1][0][1])

#Add Element in list by append() method
_list.append("Khusboo")
print(_list)
# Add Element in list by insert() method
_list.insert(0,"Shubham Sharma")
print(_list)

#Add Element from one list to another list
_list.extend(_name)
print(_list)

#input a list using loop
_listRange = int(input("Kindly enter the list item count : "))
_age_list= []
for i in range(_listRange):
    _age = int(input("Enter Person Age: "))
    _age_list.append(_age)
print("Data has been successfully added.")
_show = int(input("For saved data view, Kindly type 1 else type 2 for exist : "))
if(_show == 1):
    print(_age_list)
elif(_show == 2):
    print("Thanks for Visiting")
elif(_show !=1 & _show !=2):
    pass
print(_show)