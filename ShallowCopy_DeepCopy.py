import copy
oldList = [[1,2,3],[4,5,6],[7,8,9]]
print(oldList)
print('Id of old list = ', id(oldList))
newList = oldList
print(newList)
print('Id of new list = ', id(oldList))

print('after copy')
newList[2][2] = 'AA'
print(oldList)
print('Id of old list = ', id(oldList))
print(newList)
print('Id of new list = ', id(oldList))

print('shallow copy')
newList = copy.copy(oldList)
print(oldList)
print('Id of old list = ', id(oldList))
print(newList)
print('Id of new list = ', id(oldList))

print('Append after shallow copy')
oldList.append([7,7,7])
print(oldList)
print('Id of old list = ', id(oldList))
print(newList)
print('Id of new list = ', id(oldList))

print('modify after shallow copy')
oldList[1][1]=999
print(oldList)
print('Id of old list = ', id(oldList))
print(newList)
print('Id of new list = ', id(oldList))

print('Deep copy')
oldList = [[1,2,3],[4,5,6],[7,8,9]]
newList = copy.deepcopy(oldList)
print(oldList)
print('Id of old list = ', id(oldList))
print(newList)
print('Id of new list = ', id(oldList))

print('Append after deep copy')
oldList.append([7,7,7])
print(oldList)
print('Id of old list = ', id(oldList))
print(newList)
print('Id of new list = ', id(oldList))

print('modify after deep copy')
oldList[1][1]=999
print(oldList)
print('Id of old list = ', id(oldList))
print(newList)
print('Id of new list = ', id(oldList))
