import random
import timeit
import matplotlib.pyplot as plt


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

    for i in range(length // 2 - 1, -1, -1):
        buildHeap(inArray, length, i)

    for j in range(length - 1, 0, -1):
        inArray[j], inArray[0] = inArray[0], inArray[j]
        buildHeap(inArray, j, 0)


def printArray(inArray):
    print("\nArray in current state")
    for i in range(len(inArray)):
        print("%d" % inArray[i], end=" ")


def performanceTest():
    sortedIncreasingTimes = []
    sortedDecreasingTimes = []
    unsortedTimes = []

    length = 5000

    for n in range(length // 5):
        sortedI = []
        sortedD = []
        unsorted = []

        for i in range(length):
            sortedI.append(i)
            sortedD.append(length - i)
            unsorted.append(random.randint(0, length))

        sortedIncreasingTimes.append(min(timeit.repeat(lambda: sortHeap(sortedI), repeat=3, number=5)))
        sortedDecreasingTimes.append(min(timeit.repeat(lambda: sortHeap(sortedD), repeat=3, number=5)))
        unsortedTimes.append(min(timeit.repeat(lambda: sortHeap(unsorted), repeat=3, number=5)))

    plt.plot(range(1, 5001, 5), sortedIncreasingTimes, label='Sorted Increasing Times')
    plt.plot(range(1, 5001, 5), sortedDecreasingTimes, label='Sorted Decreasing Times')
    plt.plot(range(1, 5001, 5), unsortedTimes, label='Unsorted Times (control sample)')
    plt.xlabel('Length of Array being Sorted (x 5)')
    plt.ylabel('Time (s)')
    plt.title('Performance Comparison: Sorted Array Performance in a Heap Sort')
    plt.legend()
    plt.show()


arr = [25, 44, 55, 99, 30, 37, 15, 10, 2, 4]

printArray(arr)
sortHeap(arr)
printArray(arr)

performanceTest()
