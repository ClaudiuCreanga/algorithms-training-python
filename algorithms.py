#Insertion sort - sorting algorithm O(n^2), starts at key 2 and sorts 1 key at a time O(n) and then swaps keys if necessary O(n)
def insertionSort():
    inputList = [64,25,12,22,11]
    for i in range(len(inputList)): #3
        if i == 0:
            continue
        if inputList[i] < inputList[i - 1]:
            for j in range(i, 0, -1):
                if inputList[j] < inputList[j - 1]:
                    inputList[j], inputList[j - 1] = inputList[j - 1], inputList[j]




    return inputList
print(insertionSort())


#Selection sort - sorting algorithm, O(n^2)

def selectionSort():
    inputList = [64,25,12,22,11]
    for index, item in enumerate(inputList):
        min = index # 0
        for index2, item2 in enumerate(inputList):
            if item2 < inputList[min] and index2 > index:
                min = index2
        if(min != index):
            inputList[index], inputList[min] = inputList[min], inputList[index]
    return inputList
print(selectionSort())
