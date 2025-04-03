# 1. Use the range function in for loop to print the sequence of 0 to 5
# 2. Print the value from 2 to 6 using range()
# 3. Increment the sequence with 3
# 4. Print all number from 0 to 5 and print a message when loop has ended.
# 5. Print Each Adjective of each fruit

#1
'''
for i in range(6):
    print(i)
'''
#2
'''
for j  in range(2,7):
    print(j)
'''
#3
'''
for k in range(2,30,3):
    print(k)
'''
#4 
'''
for l in range(6):
    print(l)
else:
    print("Execution Finish")
'''
#5 Nested Loops
adj = ["red","big","tasty"]
fruit =["apple","banana","cherry"]
for i in adj:
    for j in fruit:
        print(i , j)
