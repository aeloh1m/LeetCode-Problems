'''
Given two strings needle and haystack, return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

 

Example 1:

Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:

Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
 

Constraints:

1 <= haystack.length, needle.length <= 104
haystack and needle consist of only lowercase English characters.

'''

# Allright so.. We have two parameters then.. for a single word 
# aah right I wasn't having in count the other parameter lmao




# class Solution(object):
#     def strStr(self, haystack, needle):
#         """
#         :type haystack: str
#         :type needle: str
#         :rtype: int
#         """
#         needleFinder = []
#         indexes = []
#         needleChecker = ''

#         # enumerate()

#         # Set an initial index
#         # current_index = 2

#         # # Iterate over the array starting from the current index
#         # for index, value in enumerate(my_array[current_index:], start=current_index):
#         #     print(f"Index: {index}, Value: {value}")

#         '''So for instance in python you can get the index from a certain string inside another string'''

#         '''
#         key: 

#         The .index() method in Python is used to find the index of the first occurrence of a specified value in a list. Here's the general syntax:

#         '''
        

#         '''
#         This would be the simplest solution having in count big O notations
        
#         if(needle in haystack): # Check if str needle is inside haystack
#             return haystack.index(needle)
#         else:
#             return -1

#         '''


#         onlyChar = 0
        

#         if(len(needle) == 1 and len(haystack) == 1):
#             print("0")
#             return 0
        
#         if(len(needle) == 1):
#                     onlyChar = needle[0]
#                     print(onlyChar, "mememe")


#         if(onlyChar != 0):
#             for i in range(len(haystack)): # So basically we search in the lenght of haystack string
#                 try:
#                     if(onlyChar == haystack[i]):
#                             needleFinder.append(haystack[i])
#                             indexes.append(i) # This would make more sense.. 
#                 except:
#                     print("some error occurred with index") # Try catch here is bassicaly to not be having wild errors in console
#         else:                
#             for i in range(len(haystack)): 
#                 try:
#                     if(needle[i] == haystack[i]): # If any letter matches then we save it in the nFinder list
#                         needleFinder.append(haystack[i])
#                         indexes.append(i) # This would make more sense.. 
                
#                 except:
#                     print("some error occurred with index") # Try catch here is bassicaly to not be having wild errors in console
#         print(needleFinder, "needlefinder")


#         if(onlyChar != 0 and onlyChar == haystack[0]):
            
#             return print(indexes[-1])
#         else:
#             if(onlyChar != 0):
#                 return print(indexes[-1])

            
#             print(indexes, "actual indexes")

#             print(len(haystack), "len")
#             if len(haystack) == 1:
#                 print("0")
#                 return 0
            
#             # haystack = "abc"
#             # needle = "a" # Need to find

#             if(needle[0] == haystack[indexes[-1]]): # matching first letter with starting letter from haystack index
#                 print("ok")
#                 return print(indexes[-1])

#             needleChecker = ''.join(needleFinder) # What this does is basically join every index of the list we've given
            
#             print(needleChecker, "nc")
#             if(needleChecker != needle): # If the whole word doesn't match then -1
#                 print("-1")
#                 return -1 
#             else:
#                 print("0")
#                 return 0

'''
Ok, now I should think how to get the current indexes from the loop in order to catch the position of the 
matched word...

Ok I could use booleans maybe

For instance the logic in the problem says from "0 to 6".. <= This was, like wrong so ---

Now I gotta get the index from which the word from the param "needle" starts

I need to modify it for the second case, it wants me to check for the whole word, not just its index.

Then again I should check for other cases

Allright, this should work, I'll submit for all the tests to see if it passes all.
59/82 <=  passed

current:

 haystack =
"hello"
needle =
"ll"

output should be = 2

This asks me to actually give the index in return lol.

The main reason for the additional is bc it seems the current index where the "needle" begins is not
added to "indexes"

Ok time to check
----------

Should iterate like nodes. 
'''



'''
part 3:

We got this error for a testcase:

IndexError: string index out of range
    if(needle[0] == haystack[indexes[-1]]): # matching first letter with starting letter from haystack index
Line 28 in strStr (Solution.py)
    ret = Solution().strStr(param_1, param_2)
Line 73 in _driver (Solution.py)
    _driver()
Line 83 in <module> (Solution.py)

Basically we can't check for an index in 0 for -1, then for instance we add an if
statement to avoid that

'''

'''
Grab the needle word,

check if word in haystack

get index of starting point of first letter in needle
inside haystack.

'''
class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        needleFinder = []
        indexes = []
        needleChecker = ''

        # enumerate()

        # Set an initial index
        # current_index = 2

        # # Iterate over the array starting from the current index
        # for index, value in enumerate(my_array[current_index:], start=current_index):
        #     print(f"Index: {index}, Value: {value}")

        '''So for instance in python you can get the index from a certain string inside another string'''

        '''
        key: 

        The .index() method in Python is used to find the index of the first occurrence of a specified value in a list. Here's the general syntax:

        '''
        

        # This would be the simplest solution having in count big O notations
        
        if(needle in haystack): # Check if str needle is inside haystack
            return haystack.index(needle)
        else:
            return -1

        # So the first approach DID work but not for all test cases.

        









haystack = "hello"
needle = "ll" # Need to find

solution = Solution()
solution.strStr(haystack, needle)



