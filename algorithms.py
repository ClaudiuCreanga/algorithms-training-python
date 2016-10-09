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

# Merge sot - sorting algorithm, O(n log n),
# Recursive algo, divide and conquer strategy
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

    leftList = mergeSort2(x[:mid])
    rightList = mergeSort2(x[mid:])

    while (len(leftList) > 0) and (len(rightList) > 0):
        if leftList[0] > rightList[0]:
            result.append(rightList.pop(0))
        else:
            result.append(leftList.pop(0))

    result.extend(leftList+rightList)
    return result


print(mergeSort2([64, 25, 12, 22, 91, 11, 2, 15, 15, 20, 90]))
A = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
def performOps(A):
    m = len(A)
    n = len(A[0])
    B = []
    for i in range(len(A)):
        B.append([0] * n)
        for j in range(len(A[i])):
            B[i][n - 1 - j] = A[i][j]
    return B
B = performOps(A)
for i in range(len(B)):
    for j in range(len(B[i])):
        pass
        #print(B[i][j],)


class Solution:
    # @param A : root node of tree
    # @param B : root node of tree
    # @return an integer
    def isSameTree(self, A, B):
        for i in range(len(A)):
            if A[i] != B[i]:
                return 0
        return 1
da  = Solution()
print(da.isSameTree("3 5 -1 -1","3 5 -1 -1"))



# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, A, B):
        if A is None and B is None:
            return 1

        if A is None or B is None:
            return 0

        return int(A.val == B.val and self.isSameTree(A.left, B.left) and
                self.isSameTree(A.right, B.right))

def fibonacci(n):
    if n == 1 or n == 0:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(4))

S='adobecodebaaaaaaaaanc'
T='abct'

def sInT(x):
    for index, item in enumerate(S):
        substring = S[index:index+x]
        if isInString(substring):
            return substring
    if x == len(S):
        return "No substring could be found"
    return sInT(x+1)
def isInString(substring):
    for i in T:
        if i not in substring:
            return
    return substring
goodstring = sInT(len(T))
print(goodstring)

# Quicksort O(n^2) , average case is O(n log n)
# recursive, divide and conquer algo
# start with a pivot. you want your pivot to be the closest to the median value so that you can split the list in half.
# a good way to ensure it is to chose the first, last and middle item and take the average value.
def quicksort(input_list = [64, 25, 12, 22, 11, 2, 15, 15, 20]):
    less = []
    equal = []
    greater = []

    if len(input_list) > 1:
        pivot = (input_list[0] + input_list[len(input_list) - 1]) / 2
        for x in input_list:
            x = abs(x)
            if x > pivot:
                greater.append(x)
            elif x == pivot:
                equal.append(x)
            elif x < pivot:
                less.append(x)
        return quicksort(less) + equal + quicksort(greater)
    else:
        return input_list
print(quicksort())

# https://leetcode.com/problems/regular-expression-matching/
def isMatch(myString,pattern):
    if len(myString):
        if not len(pattern):
            return False
        isDot = pattern[0] == "."
        isStar = False
        if (len(pattern) > 1):
            isStar = pattern[1] == "*"
        if isStar:
            if isDot:
                if len(pattern) == 2:
                    return True # .* matches everything
                else:
                    return isMatch(myString, pattern[2:])
            for index,item in enumerate(myString): # aaaaab a*b is True
                if pattern[0] is not item:
                    return isMatch(myString[index:], pattern[2:])
            if len(pattern) > 2:
                return isMatch(myString[2:], pattern[2:])
            else:
                return True
        elif myString[0] == pattern[0]:
            return isMatch(myString[1:],pattern[1:])
        elif isDot:
            return isMatch(myString[1:],pattern[1:])
        else:
            return False
    if len(pattern):
        return False
    return True
#print(isMatch("aa","a*c*a"))

#myList = ["1","2","3","3"]
#dict = dict([i, myList.count(i)] for i in myList)
#print([i, myList.count(i)])


def statistic():
    length = 10
    myList = "64630 11735 14216 99233 14470 4978 73429 38120 51135 67060"
    myList = sorted(map(int, myList.split(" ")))
    mean = sum(myList) / float(length)
    myList.sort()
    if length % 2:
        median = myList[length // 2]
    else:
        median = (myList[length / 2 - 1] + myList[length / 2 ]) / float(2)
    modeList = dict([i, myList.count(i)] for i in myList)
    sortedModeList = sorted(modeList.items(), key=lambda x: x[1], reverse=True)
    heighestMode = sortedModeList[0][1]
    multipleModes = []
    for x in sortedModeList:
        if x[1] == heighestMode:
            multipleModes.append(x[0])
        else:
            break

    mode = min(multipleModes)
    return str(mean) + "\n" + str(median) + "\n" + str(mode)


print(statistic())

