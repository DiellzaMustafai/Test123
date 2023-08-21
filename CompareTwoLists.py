#Compare two lists using Python

#Compare two lists

list1 = [10, 20, 30, 40, 50]
list2 = [50, 75, 30, 20,  40, 59]


res = [x for x in list1 + list2 if x not in list1 or x not in list2]

print(res)
if not res:
    print("Both the lists are equal")
else:
    print("Both of the lists are not equal")