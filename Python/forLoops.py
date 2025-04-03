#Print each fruit in a fruit list
fruit = ["apple","banana","cheery"]
for i in fruit:
    print(i)
#Loop Through Letter in "Banana"
_fruit=fruit[1] # Pick up a fruit name form list and save in variable as string
print("Selected Fruit from list is :",_fruit) #Print for confirmation
for a in _fruit: #Loop for the save variable
    print(a) # Print the data
#Break Statement 
#Break the for loop in case j is "banana"
for j in fruit:
    print(j)
    if(j=="banana"):
        break
    print(j)
print("Continue Statement")
#Continue Statement
for k in fruit:
    if (k=="banana"):
        continue # This will bypass the above condition
    print(k)
