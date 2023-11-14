'''
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

'''

# Code:
# First of all, catch the lenght of the given roman number, then for each of its index longitude, check for the values and then
# collect the right data and else
# First of all I WILL have to make sure there is a correct roman number in the string.

# For combinations of 2, I'll need to check for the combination between one R number and the one that follows behind.
# Or I could check in the destructured list what comes before each to filter the exceptions.

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dictionaryData = {'I':1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        exceptions = {'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90, 'CD': 400, 'CM': 900}
        destructuringOfNumber = [] # Create a list for storing each individual index of the string
        restOfNumbers = []
        listToConvert = []
        romansToInt = []
        checker = []
        wholeData = []
        formattedNumber = ''
        result = 0

        for i in range(len(s)):
            destructuringOfNumber.insert(i, s[i]) # Create a deestructured list

        restOfNumbers = destructuringOfNumber[:] # Copy og array list
        
        for i in range(len(destructuringOfNumber)): # We start formatting the exceptions.
            try:
                checker += [destructuringOfNumber[i], destructuringOfNumber[i+1]] # Check individually each pair of possible numbers.
                formattedNumber = ''.join(checker) # Format to merge into one.

                if(formattedNumber in exceptions): # check if in exceptions array.
                    listToConvert.append(formattedNumber)
                    restOfNumbers.remove(checker[0])
                    restOfNumbers.remove(checker[1])
                checker = [] # After each check, we restore values to none.
                formattedNumber = ''
            except:
                print("Some error with indexes")

        listToConvert += restOfNumbers # We add up the rest of the numbers after formatting

        # wholeData = {**dictionaryData, **exceptions} # Merge all data.
        wholeData = dictionaryData.copy()
        wholeData.update(exceptions)

        for i in range(len(listToConvert)):
            if(listToConvert[i] in wholeData): #Check the whole numbers for individual values.
                 
                romansToInt.append(wholeData[listToConvert[i]]) # We catch the equivalent then append.
        
                
        result = sum(romansToInt) # Then sum

        return result
        
        
s = "LVIII"
'''
Ok so I have a list with the exceptions, then I have a list with all the characters for the string, so I gotta mix up the ones that do not match
up to any exception with the exceptions, how do I do that ? I could be sustracting from the og datas the ..

I have to check for each checker, if that combination is not in the exceptions'''


solution = Solution()
solution.romanToInt(s)





'''

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.
Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.
Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
 

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].


'''