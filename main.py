
def buildHeap(inArray, n, i):
    upper = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and inArray[upper] < inArray[left]:
        upper = left

    if right < n and inArray[upper] < inArray[right]:
        upper = right

    if upper != i:
        inArray[i], inArray[upper] = inArray[upper], inArray[i]

        buildHeap(inArray, n, upper)

def sortHeap(inArray):
    length = len(inArray)

    for i in range(length//2 - 1, -1, -1):
        buildHeap(inArray, length, i)

    for j in range(length-1, 0, -1):
        inArray[j], inArray[0] = inArray[0], inArray[j]
        buildHeap(inArray, j, 0)


def printArray(inArray):
    print("\nArray in current state")
    for i in range(len(inArray)):
        print("%d" % inArray[i], end=" ")



arr = [25, 44, 55, 99, 30, 37, 15, 10, 2, 4]

printArray(arr)
sortHeap(arr)
printArray(arr)

