#   - averagePair
#  Write a function called averagePair. Given a sorted array of integers and a target average, determine if there is a pair of values in the array where the average of the pair equals the target average. There may be more than one pair that matches the average target.

#  Bonus Constraints:

#  Time: O(N)

#  Space: O(1)

#  Sample Input:

#  averagePair([1,2,3],2.5)  true
#  averagePair([1,3,3,5,6,7,10,12,19],8)  true
#  averagePair([-1,0,3,4,5,6], 4.1)  false
#  averagePair([],4)  false



def averagePair(arr , targ) :
    arrLength = len(arr) #get the last element of the array
    start = 0 #first element of the array
    # this function returns the average value of two consecutive elements 
    def average(val1 , val2):
       return (val1 + val2) / 2
    if (len(arr) < 1 ) : #if there is no element in the array then return false and stop the operation
        return False
    for i in range(1, arrLength): #loop through the a range as much as there is elements in the array and check the average 
        
        # print(average(arr[start] , arr[i]) )
        if(average(arr[start] , arr[i]) == targ ):
            return True
        else:
            start += 1
    return False

# print(averagePair([12,4,5,6], 4.5))

# print(averagePair([1,2,3],2.5) ) #true
print(averagePair([1,3,3,5,6,7,10,12,19],8))  #false
# print(averagePair([-1,0,3,4,5,6], 4.1))  #false
# print(averagePair([],4))  #false