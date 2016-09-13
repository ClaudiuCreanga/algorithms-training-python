#sorting algorithm, O(n^2)

inputList = [64,25,12, 22, 11]
for index, item in enumerate(inputList):
    min = index # 0
    for index2, item2 in enumerate(inputList):
        if item2 < inputList[min] and index2 > index:
            min = index2
    if(min != index):
        inputList[index], inputList[min] = inputList[min], inputList[index]
print(inputList)
