# Complete the function to return the first two items in the given list
def getFirstTwo(mylist):
    return mylist[0], mylist[1]

# expected output: [8, 3]
print(getFirstTwo([8, 3, 5, 2, 10]))

# expected output: [15, 2]
print(getFirstTwo([15, 2, 10, 12]))


#######################################################################################################################
# Complete the function to return the last two items in the given list
def getLastTwo(mylist):
    return mylist[-2], mylist[-1]

# expected output: [2, 10]
print(getLastTwo([8, 3, 5, 2, 10]))

# expected output: [9, 12]
print(getLastTwo([15, 2, 9, 12]))


#######################################################################################################################
# Complete the function to add num1 to the end of the given list
def addToEnd(mylist, num1):
    mylist.append(num1)
    return mylist

# expected output: [4, 5, 6, 7]
print(addToEnd([4, 5, 6], 7))

# expected output: [9, 8, 7, 6]
print(addToEnd([9, 8, 7], 6))


#######################################################################################################################
# Complete the function to add num1 to the front of the given list
def addToFront(mylist, num1):
    mylist.insert(0,num1)
    return mylist

# expected output: [3, 4, 5, 6]
print(addToFront([4, 5, 6], 3))

# expected output: [10, 9, 8, 7]
print(addToFront([9, 8, 7], 10))


#######################################################################################################################
# Complete the function to return a new list containing
# the first two and last two items in the given list
def getFirstTwoAndLastTwo(mylist):
    result = [mylist[0], mylist[1], mylist[-2], mylist[-1]]
    return result

# expected output: [8, 3, 19, 1]
print(getFirstTwoAndLastTwo([8, 3, 7, 15, 2, 10, 19, 1]))

# expected output: [7, 15, 3, 5]
print(getFirstTwoAndLastTwo([7, 15, 2, 10, 19, 1, 3, 5]))


#######################################################################################################################
# Complete the function to remove the first item in the given list
def removeFirst(mylist):
    mylist.pop(0)
    return mylist

# expected output: [7, 8, 9]
print(removeFirst([6, 7, 8, 9]))

# expected output: [2, 3, 4]
print(removeFirst([1, 2, 3, 4]))


#######################################################################################################################
# Complete the function to remove the third item in the given list
def removeThird(mylist):
    mylist.pop(2)
    return mylist

# expected output: [6, 7, 9]
print(removeThird([6, 7, 8, 9]))

# expected output: [1, 2, 4]
print(removeThird([1, 2, 3, 4]))


#######################################################################################################################
# Complete the function to order the values in the list
# if ascending is true then order lowest to highest
# if ascending is false then order highest to lowest
def sortList(mylist, ascending):
    if ascending:
        return sorted(mylist)
    else:
        return sorted(mylist, reverse=True)

# expected output: [4, 12, 19, 33]
print(sortList([19, 4, 33, 12], True))

# expected output: [33, 19, 12, 4]
print(sortList([19, 4, 33, 12], False))


#######################################################################################################################
# Complete the function to return a dictionary using
# list1 as the keys and list2 as the values
def createDict(list1, list2):
    new_dict = {list1[i] : list2[i] for i in range(len(list1))}
    return new_dict


# expected output: {'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}
print(createDict(['tomato', 'banana', 'lime'], ['red', 'yellow', 'green']))

# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(createDict(['Brazil', 'Ireland', 'Indonesia'], ['Brasilia', 'Dublin', 'Jakarta']))


#######################################################################################################################
# Complete the function to return a dictionary value
# if it exists or return Not Found if it doesn't exist
def findDictItem(mydict, key):
    if key in mydict:
        return mydict[key]
    else:
        return 'Not Found'

# expected output: yellow
print(findDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}, 'banana'))

# expected output: Not Found
print(findDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}, 'Cameroon'))


#######################################################################################################################
# Complete the function to remove a dictionary item if it exists
def removeDictItem(mydict, key):
    if key in mydict:
        del mydict[key]
    return mydict

# expected output: {'tomato': 'red', 'lime': 'green'}
print(removeDictItem({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'}, 'banana'))

# expected output: {'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}
print(removeDictItem({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'}, 'Cameroon'))


#######################################################################################################################
# Complete the function to print every key and value
def printDict(mydict):
    for key, value in mydict.items():
        print(f'{key}={value}')

# expected output:
#        tomato=red
#        banana=yellow
#        lime=green
printDict({'tomato': 'red', 'banana': 'yellow', 'lime': 'green'})

# expected output:
#        Brazil=Brasilia
#        Ireland=Dublin
#        Indonesia=Jakarta
printDict({'Brazil': 'Brasilia', 'Ireland': 'Dublin', 'Indonesia': 'Jakarta'})