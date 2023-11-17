


'''
You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.

Increment the large integer by one and return the resulting array of digits.

 



'''


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        newArray = []
        ninesArray = []
        set99true = False
        formattedDigits  = ''.join([str(num) for num in digits])
        print(formattedDigits, "Digits")


        for i in range(len(str(formattedDigits))):
            digitStr = str(formattedDigits) 

            newArray.append(digitStr[i])  

        for i in range(len(newArray)):        
            if(formattedDigits[i] == '9'):
                print(True)
                set99true = True
        
        if(set99true):
            answer = int(formattedDigits) + 1
            print(answer, "answer")
            str(answer)
            # Now we de-structure

            ninesArray = [int(num) for num in str(answer)]
            print(ninesArray, "n array") 
            return ninesArray


        '''
        if(formattedDigits[i] == 9): # Check each number if 9
                nineDigits  = ''.join([str(num) for num in digits])
        '''    
        #print(nineDigits, "n digits")


        if(len(digits) == 1): # First case if lenght of digits is 1
            newArray = []
            print("ok")
            if(digits[0] == 0):
                newArray.append(1)
                print(newArray)
                return newArray
            newDigits = digits[0] + 1
            print(newDigits)


            for i in range(len(str(newDigits)) +1):
                print(i, "i'm i")

                try:
                    digitStr = str(newDigits) 

                    newArray.append(digitStr[i])
                except:
                    print("some error")

            lastArray = [int(num) for num in newArray]
            print(lastArray, "new array with ints")
            return lastArray
        else:

            lastDigitPlusOne = digits[-1] + 1 # Add one to the last index
            print(lastDigitPlusOne, "lastDigitPlusOne")

            print(digits)
            digits[-1] = lastDigitPlusOne
            print(digits, "arr")
            return digits
        
        


digits = [0]

# Expected output = [2] eh

solution = Solution()

solution.plusOne(digits)

'''
Approach:
1) I should format the number, check the last index, add +1 to the last index
check if the sum of the new array gives the formatted number

# ===  TestCase for only lenght 1 digits == #
done => if its a single digit then I should just add +1 
done => then check each index to form the newArray

Time to check for test cases...
First test case: 

TypeError: ['1', '0'] is not valid value for the expected return type integer[]
    raise TypeError(str(ret) + " is not valid value for the expected return type integer[]");
Line 55 in _driver (Solution.py)
    _driver()
Line 61 in <module> (Solution.py)

Its saying that the array has STRING type elements, and needs int types,
let's fix that.

Cool, lets see now..

First 3 cases are ok. Now lets check for the rest...

We got the case for "0", and its giving some str int type error.


93 / 111 testcases passed
now:
digits = 99
expected [1, 0, 0]
This may fix and break some others lets see...
okok I was usin 99 instead of [9, 9]

What should I do for these cases which add 1 to 9's.

whole number => add +1 => destructure the list

That should get the case for that at least

Smth broken af, 
I gotta just add the whole arr without the last index
or make the whole digits then change only the last one

Allright, this one got fully accepted

Accepted
Editorial
Solution
Runtime
11
ms
Beats
91.91%
of users with Python
Memory
13.35
MB
Beats
11.19%
of users with Python


While I know there are mostly BETTER solutions in terms of like
O(n) and stuff and also ways of writing these algos with like 2 
functions, I like making these long kind of approaches dissecting each
case.

'''



'''

Example 1:

Input: digits = [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Incrementing by one gives 123 + 1 = 124.
Thus, the result should be [1,2,4].
Example 2:

Input: digits = [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
Incrementing by one gives 4321 + 1 = 4322.
Thus, the result should be [4,3,2,2].
Example 3:

Input: digits = [9]
Output: [1,0]
Explanation: The array represents the integer 9.
Incrementing by one gives 9 + 1 = 10.
Thus, the result should be [1,0].
 

Constraints:

1 <= digits.length <= 100
0 <= digits[i] <= 9
digits does not contain any leading 0's.


'''



        