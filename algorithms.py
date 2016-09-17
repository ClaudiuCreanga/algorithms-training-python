#Bubble sort - sorting algorithm O(n^2), starts with the first 2 keys, compares them, swaps them if necessary
# and then procedes to compare key 1 and key 2, and then key 2 an key 3 etc
def bubbleSort():
    inputList = [64, 25, 12, 22, 11, 2, 15, 15, 20]
    changed = True
    while changed is True:
        changed = False # assume the list is sorted before starting the loop
        for i in range(1, len(inputList)):
            if inputList[i] < inputList[i - 1]:
                inputList[i], inputList[i-1] = inputList[i-1], inputList[i]
                changed = True # the list is not sorted
    return inputList
print(bubbleSort())



#Insertion sort - sorting algorithm O(n^2), starts at key 2 and sorts 1 key at a time O(n) and then swaps keys if necessary O(n)
def insertionSort():
    inputList = [64, 25, 12, 22, 11, 2, 15, 15, 20]
    for i in range(1, len(inputList)): # start at 1 because we don't do anything to first key
        for j in range(i, 0, -1): # loop through all past value
            if inputList[j] < inputList[j - 1]: # if current value is smaller than any of the past values
                inputList[j], inputList[j - 1] = inputList[j - 1], inputList[j] # swap the values
    return inputList
print(insertionSort())

def insertionSort2():
    inputList = [64, 25, 12, 22, 11, 2, 15, 15, 20]
    for i in range(1, len(inputList)):
        j = i # create a copy of i and then we will decrease it to rightListero while we check every item smaller than i
        while j > 0 and inputList[j] < inputList[j - 1]:
            inputList[j], inputList[j - 1] = inputList[j - 1], inputList[j]  # swap the values
            j -= 1
    return inputList
print(insertionSort2())


#Selection sort - sorting algorithm, O(n^2). starts at key 0 and finds the global minimum
# it puts it in the first position, then proceeds to next key and finds the global minimum
# of the rest of the list and then inserts it in key n etc.

def selectionSort():
    inputList = [64, 25, 12, 22, 11, 2, 15, 15, 20]
    for index, item in enumerate(inputList):
        min = index
        for index2, item2 in enumerate(inputList):
            if item2 < inputList[min] and index2 > index:
                min = index2
        if(min != index):
            inputList[index], inputList[min] = inputList[min], inputList[index]
    return inputList
print(selectionSort())

#Merge sot - sorting algorithm, O(n log n),
def mergeSort(list):
    if(len(list) > 1): # 1 list item is already sorted
        middle = len(list) // 2
        leftList = list[:middle] # split it in 2 lists
        rightList = list[middle:]

        mergeSort(leftList) # do it recursively, first split the left half
        mergeSort(rightList) # then split the right half

        leftIterator = rightIterator = generalIterator = 0

        while leftIterator < len(leftList) and rightIterator < len(rightList):
            if leftList[leftIterator] < rightList[rightIterator]:
                list[generalIterator] = leftList[leftIterator]
                leftIterator += 1
            else:
                list[generalIterator] = rightList[rightIterator]
                rightIterator += 1
            generalIterator += 1

        # keep the second element in the list on the second position
        while leftIterator < len(leftList):
            list[generalIterator] = leftList[leftIterator]
            generalIterator += 1
            leftIterator += 1

        while rightIterator < len(rightList):
            list[generalIterator] = rightList[rightIterator]
            generalIterator += 1
            rightIterator += 1

    return list

print(mergeSort([64, 25, 12, 22, 91, 11, 2, 15, 15, 20, 90]))


def mergeSort2(x):

    if len(x) < 2:
        return x

    result = []
    mid = int(len(x)/2)

    leftList = merge_sort(x[:mid])
    rightList = merge_sort(x[mid:])

    while (len(leftList) > 0) and (len(rightList) > 0):
        if leftList[0] > rightList[0]:
            result.append(rightList.pop(0))
        else:
            result.append(leftList.pop(0))

    result.extend(leftList+rightList)
    return result


print(merge_sort([64, 25, 12, 22, 91, 11, 2, 15, 15, 20, 90]))
