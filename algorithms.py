#Insertion sort - sorting algorithm O(n^2), starts at key 2 and sorts 1 key at a time O(n) and then swaps keys if necessary O(n)
def insertionSort():
    inputList = [64,25,12,22,11]
    for i in range(1, len(inputList)): # start at 1 because we don't do anything to first key
        if inputList[i] < inputList[i - 1]: # if present value is smaller than the previous value
            for j in range(i, 0, -1): # loop through all past value
                if inputList[j] < inputList[j - 1]: # if current value is smaller than any of the past values
                    inputList[j], inputList[j - 1] = inputList[j - 1], inputList[j] # swap the values
    return inputList
print(insertionSort())


#Selection sort - sorting algorithm, O(n^2). starts at key 0 and finds the global minimum
# it puts it in the first position, then proceeds to next key and finds the global minimum
# of the rest of the list and then inserts it in key n etc.

def selectionSort():
    inputList = [64,25,12,22,11]
    for index, item in enumerate(inputList):
        min = index
        for index2, item2 in enumerate(inputList):
            if item2 < inputList[min] and index2 > index:
                min = index2
        if(min != index):
            inputList[index], inputList[min] = inputList[min], inputList[index]
    return inputList
print(selectionSort())


