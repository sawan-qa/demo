#Python String case-1
#case-1
#String can be denoted by Single quote or Double Quote
print("Hello World")# Double Quotes
print('Hello Sawan')# Single Quotes

#case-2 Quotes inside quotes
print('sawan lives in "Noida."')

#Assigning String to a variable
name = "Sawan Kumar" 
print("My Name is :", name)
# Multiline string
print("""My Name is Sawan Kumar.
I live in Noida, Uttar Pradesh.
I Worked as Software Tester.""")
#String as an Array
Name = "Sawan Kumar"
print(Name[1]) # a[0] means first character.

#Looping through a string
for x in "Sawan":
    print(x)
#String lenght by len()
name = "Sawan Kumar"
print(len(name))
name_lenghth=int(len(name))
if (name_lenghth<=10):
    print("Name is Valid")
else:
    print(name,"Name is invalid")
#Check String
name = "This is Sawan Kumar and lives in Noida"
if("Sawan" in name): # use in keyword to check whether the word present in that string
    print("You are an authorize Person.")
else:
    print("You are an Unauthorize Person.")
#Check if Not
if ("Noida"not in name):
    print("Noida not found in Name")
else:
    print("Noida found in your name")

