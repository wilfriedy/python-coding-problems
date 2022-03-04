#   Binary Search Exercise
#  Write a function called binarySearch which accepts a sorted array and a value and returns the index at which the value exists. Otherwise, return -1.

#  This algorithm should be more efficient than linearSearch - you can read how to implement it here - https://www.khanacademy.org/computing/computer-science/algorithms/binary-search/a/binary-search and here - https://www.topcoder.com/community/data-science/data-science-tutorials/binary-search/

#  Examples:

#  binarySearch([1,2,3,4,5],2) // 1
#  binarySearch([1,2,3,4,5],3) // 2
#  binarySearch([1,2,3,4,5],5) // 4
#  binarySearch([1,2,3,4,5],6) // -1
#  binarySearch([
#    5, 6, 10, 13, 14, 18, 30, 34, 35, 37,
#    40, 44, 64, 79, 84, 86, 95, 96, 98, 99
#  ], 10) // 2
#  binarySearch([
#    5, 6, 10, 13, 14, 18, 30, 34, 35, 37,
#    40, 44, 64, 79, 84, 86, 95, 96, 98, 99
#  ], 95) // 16
#  binarySearch([
#    5, 6, 10, 13, 14, 18, 30, 34, 35, 37,
#    40, 44, 64, 79, 84, 86, 95, 96, 98, 99
#  ], 100) // -1
import math


def binarySearch(arr, val) :
    if(len(arr) <= 0):
        return False
    starts = 0
    ends = len(arr) - 1
    middle = math.floor((starts + ends) /2)
    # index_count = 0
    while arr[middle] != val and starts <= ends:
        print(ends , 'end')
        print(starts , 'stat')
        print(middle , 'middle')
        print(arr[middle] , val , 'one')
        if arr[middle] > val:
            ends = middle - 1
        else:
            starts = middle + 1
        middle = math.floor((starts + ends) /2)
    
    if arr[middle] == val:
        print('found' , arr[middle])
        return middle


print(binarySearch([1,2,3,5,4],5))
