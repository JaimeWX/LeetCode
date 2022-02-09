def repeatNumbers(array):
    hashTable = {}
    repeatArray = []
    for i in array:
        if i not in hashTable:
            hashTable[i] = i
        else:
            repeatArray.append(i)
    return repeatArray
array1 = [2,3,1,0,2,5,3]
print(repeatNumbers(array1))