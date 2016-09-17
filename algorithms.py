inputList = [64, 25, 12, 22, 11, 2, 15, 15, 20]


#Bubble sort - sorting algorithm O(n^2), starts with the first 2 keys, compares them, swaps them if necessary
# and then procedes to compare key 1 and key 2, and then key 2 an key 3 etc
def bubbleSort():
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
    for i in range(1, len(inputList)): # start at 1 because we don't do anything to first key
        for j in range(i, 0, -1): # loop through all past value
            if inputList[j] < inputList[j - 1]: # if current value is smaller than any of the past values
                inputList[j], inputList[j - 1] = inputList[j - 1], inputList[j] # swap the values
    return inputList
print(insertionSort())

def insertionSort2():
    for i in range(1, len(inputList)):
        j = i # create a copy of i and then we will decrease it to zero while we check every item smaller than i
        while j > 0 and inputList[j] < inputList[j - 1]:
            inputList[j], inputList[j - 1] = inputList[j - 1], inputList[j]  # swap the values
            j -= 1
    return inputList
print(insertionSort2())


#Selection sort - sorting algorithm, O(n^2). starts at key 0 and finds the global minimum
# it puts it in the first position, then proceeds to next key and finds the global minimum
# of the rest of the list and then inserts it in key n etc.

def selectionSort():
    for index, item in enumerate(inputList):
        min = index
        for index2, item2 in enumerate(inputList):
            if item2 < inputList[min] and index2 > index:
                min = index2
        if(min != index):
            inputList[index], inputList[min] = inputList[min], inputList[index]
    return inputList
print(selectionSort())


