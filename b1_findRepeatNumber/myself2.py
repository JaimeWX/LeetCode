def repeatNumbers(array):
    for i in range(len(array)):
        while(array[i] != i):
            if array[i] == array[array[i]]:
                return array[i]
            else:
                temp = array[i]
                array[i] = array[array[i]]
                array[temp] = temp
                print(array1)
array1 = [2,3,1,0,2,5,3]
repeatNumbers(array1)

