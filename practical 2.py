numbers = [1,2,3,4,5,6,7]
lists = []
for number in numbers:
    number = number**2
    lists.append(number)
print(lists)
list1 = ["Hello", "take"]
list2 = ["Dear", "Sir"]
output = []
for i in list1:
    for j in list2:
        word = (i + ' ' + j)
        output.append(word)
print(output)
        