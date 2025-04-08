def countingSort(array):
    M = max(array)

    countingArray = [0] * (M + 1)

    for num in array:
        countingArray[num] += 1

    for i in range(1, M + 1):
        countingArray[i] += countingArray[i - 1]

    outputArray = [0] * len(array)

    for i in range(len(array) - 1, -1, -1):
        outputArray[countingArray[array[i]] - 1] = array[i]
        print("before: ", outputArray[countingArray[array[i]] - 1], array[i])
        countingArray[array[i]] -= 1
        print("After: ", outputArray[countingArray[array[i]] - 1], array[i])

    return outputArray


input_array = [6,0,2,0,1,3,4,6,1,3,2]
print(countingSort(input_array))