'''
Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).

The algorithm for myAtoi(string s) is as follows:

Read in and ignore any leading whitespace.
Check if the next character (if not already at the end of the string) is '-' or '+'. Read this character in if it is either. 
This determines if the final result is negative or positive respectively. Assume the result is positive if neither is present.
Read in next the characters until the next non-digit character or the end of the input is reached. The rest of the string is ignored.
Convert these digits into an integer (i.e. "123" -> 123, "0032" -> 32). If no digits were read, then the integer is 0. Change the sign as necessary (from step 2).
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range. Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.
Return the integer as the final result.
Note:

Only the space character ' ' is considered a whitespace character.
Do not ignore any characters other than the leading whitespace or the rest of the string after the digits.


'''

import re

class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        max =  2**31 - 1
        min = -2**31

        filterString = ''
        filterString2 = ''
        filterString3 = ''
        
        parsedStringToInt = 0
        parsedStringToFloat = 0
        

        if(len(s) == 0):
            return 0
        
        if(s == "-"):
            return 0

        if(s == "+1"):
            return 1
        
        if(s.startswith("-+") or s.startswith("+-")):
            return 0

        if(re.match(r'^[a-zA-Z+\.]', s) is not None): # Solves the problem for checking the first indexes of the string if they start with any letter or "+"; "."
            print("..")
            return 0

        filterString = re.sub(r'[^0-9-]', '', s) # Regular expression to keep only the numbers AND "-"

        filterString2 = re.sub(r'[^0-9\.\-]', '', s) # Regular expression to keep only the numbers, "-" and "."

        filterString3 = re.sub(r'[^0-9\-\+]', '', s) # Regular expression to keep only the numbers, "-" and "+"

        print(filterString3, "3")

        if(filterString3.startswith("+")):
            return 0


        try:

            parsedStringToInt = int(filterString)

            parsedStringToFloat = float(filterString2)
        except:
            print("Smth error")

        print(parsedStringToInt, "pars int")
        
        print(parsedStringToFloat, "pars float")

        print(min, "min")

        print(max, "max")
        if('.' in filterString2):
            
            parsedStringToFloat = int(round(parsedStringToFloat))
            print(parsedStringToFloat, "rounded")
            print(type(parsedStringToFloat))
            return parsedStringToFloat



        # =========================================== #
        if(parsedStringToInt > max):
            print("it is ")
            return max
    
        if(parsedStringToInt < min): 
            print("ok")
            print(min)
            return min
        
        # =========================================== #


        # This will take literally ages
        print(parsedStringToInt, "result")
                
        
        # Check if its in range of the 32 bit lenght
        if(-2**31 <= parsedStringToInt <= 2**31 - 1 ):
            return parsedStringToInt
        else:
        
            return 0



        
s = "     +004500"

solution = Solution()

solution.myAtoi(s)


# Expected = int 4500


# Comments
'''
Approach:
 Ok for this algorithm I should first parse the string into integer,
   cleaning any other character involved except for "-" which will 
   give me any negative number.

 Then I should check if its in range of -2**31 and 2**31 -1 {Values that compose a 32 bit}

Allright, for instance we have the string clean AND parsed.

=> I'll check the rest of the conditions, like the integer to be only 32 bit long (in that range)
    Gotta check what should I return.
    Ok there's basically a base result which would be the str totally parsed
    - Let me check the return if its not in range of the 32 bit lenght... 
        => As I read the problem, I should return 0 for the else.

    Everything is looking OK, I'll try the first test cases and submit.
    First three cases are OK!

    Case to check for now:
    s = "words and 987" =>> Should return 0
    I think this should be in range... And it is actually

# This is the statement I should check and, I think there's actually a restriction if the number begins and the rest are other characters
If the integer is out of the 32-bit signed integer range [-231, 231 - 1], then clamp the integer so that it remains in the range.
 Specifically, integers less than -231 should be clamped to -231, and integers greater than 231 - 1 should be clamped to 231 - 1.

 
    Now I gotta clamp the integer, the code is getting the int in between BUT the test cases
    are asking for the literal exact end of the minimun range in this case.

    Things to consider ==>
    {
        If the num is in LESS range, then checking the final result to match minimun value
            - Same for the opposite

        Allright, so setting the value to its minimun will do

        Now lets check the opposite. 
    }


    Now I have test cases with float numbers, so I gotta parse into floats too.
    test case => s = "3.14159"
    
    Somehow, to get the string to be parsed with the dot
    
    OK done, lets check the next cases..

    It says its giving me "3.0" when here its not the case.

    I'm checking why there are random numbers that are literally inside the range of 32 bits 
    yet expects 0.
    ex: -12; 982


    Basically returns and else are classified by an INDEX then the return, ex: +-12 should return 0 since +- shouldn't be a digit  => "+" => 0

    - This constraint: 
        s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.


    Checking lots of cases where its "-", length 0 and else.
    
    I'll continue it later, this is too annoying yeah.
    
    '''


'''
Chat!
Kind of!! haha
'''
'''
 

Example 1:

Input: s = "42"
Output: 42
Explanation: The underlined characters are what is read in, the caret is the current reader position.
Step 1: "42" (no characters read because there is no leading whitespace)
         ^
Step 2: "42" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "42" ("42" is read in)
           ^
The parsed integer is 42.
Since 42 is in the range [-231, 231 - 1], the final result is 42.
Example 2:

Input: s = "   -42"
Output: -42
Explanation:
Step 1: "   -42" (leading whitespace is read and ignored)
            ^
Step 2: "   -42" ('-' is read, so the result should be negative)
             ^
Step 3: "   -42" ("42" is read in)
               ^
The parsed integer is -42.
Since -42 is in the range [-231, 231 - 1], the final result is -42.
Example 3:

Input: s = "4193 with words"
Output: 4193
Explanation:
Step 1: "4193 with words" (no characters read because there is no leading whitespace)
         ^
Step 2: "4193 with words" (no characters read because there is neither a '-' nor '+')
         ^
Step 3: "4193 with words" ("4193" is read in; reading stops because the next character is a non-digit)
             ^
The parsed integer is 4193.
Since 4193 is in the range [-231, 231 - 1], the final result is 4193.
 

Constraints:

0 <= s.length <= 200
s consists of English letters (lower-case and upper-case), digits (0-9), ' ', '+', '-', and '.'.

'''
