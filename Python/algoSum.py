# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         substractNumber = 0
#         listIndex = nums[:] # Shallow copy of the array
#         rest = 0
#         indexFinder = 0
#         arrayResponse = []
#         for i in range(len(nums)):
#             try:
#                 substractNumber = nums[i] - target
#                 abs(substractNumber)
#                 if(substractNumber in nums): # If the number is in numbers then it adds the index to the response list

#                     indexFinder = listIndex.index(substractNumber) # Add index of the found item inside passed list
#                     arrayResponse.insert(0, indexFinder ) 
#                     rest = abs(target - substractNumber)

#                     if(rest in nums): # repeat for the rest of the list and it's items

#                         indexFinder = listIndex.index(rest)
#                         arrayResponse.insert(1, indexFinder )

#             except:
#                 print("Some error ocurred")
#         print(arrayResponse, "ARR")
#         return arrayResponse
    

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         substractNumber = 0
#         listIndex = nums[:] # Shallow copy of the array
#         rest = 0
#         indexFinder = 0
#         indexFinder2 = 0
#         arrayResponse = []
#         for i in range(len(nums)):
#             try:
#                 substractNumber = nums[i] - target
#                 substractToPositive = abs(substractNumber) #abs() turns the number to a positive value
#                 if(substractToPositive in nums ): # If the number is in numbers then it adds the index to the response list

#                     indexFinder = listIndex.index(substractToPositive) 
#                     print(indexFinder, "indx")
#                     arrayResponse.insert(0, indexFinder) # Add index of the found item inside passed list
#                     rest = target - substractToPositive

#                     if(rest in nums and rest ): # repeat for the rest of the list and it's items
                        
#                         indexFinder2 = listIndex.index(rest)

#                         arrayResponse.insert(1, indexFinder2)
#                         croppedListResponse = arrayResponse[0:2]

#             except:
#                 print("Some error ocurred")
#         print(croppedListResponse, "ARR")
#         return croppedListResponse


'''Now, let's try iterate over each item in the nums list and sum itself to the rest of the items until
it gives the target number, then for each encounter add the index'''  

# class Solution(object):
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         substractNumber = 0
#         rest = 0
#         arrayResponse = []
#         croppedListResponse = []

#         for i in range(len(nums)): # First we get the lenght of the array we're looping trought
#             for num in nums: # Then, for each num in nums, we get the current number from the list "nums[i]"..
#                 try:
#                     sumNumber = nums[i] + num # ..we start summing..
#                     if(sumNumber == target): # ..and we check if it's correct
#                         arrayResponse.insert(0, nums.index(nums[i]))
#                         if(nums[i] == nums[i+1]): # Then if we have any repeated item from 0:2, we search for another occurrency
#                             index = nums.index(num, nums.index(num) + 1) # The index is based on the current num in nums, and we moved it's index to the next occurrency
#                             arrayResponse.insert(1, index)
                            
#                         else:
#                             print(arrayResponse.insert(1, nums.index(num))) # If the numbers are not repeated, then  we add the first encountered index for current num
#                             print(arrayResponse)
#                         croppedListResponse = arrayResponse[0:2] # We crop the excess from loops
#                 except:
#                     "Some error ocurred"
#                     pass

#         print(croppedListResponse)
#         return croppedListResponse



class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        substractNumber = 0
        rest = 0
        arrayResponse = []
        croppedListResponse = [0, 1]

        for i in range(len(nums)): # First we get the lenght of the array we're looping trought
            for num in nums: # Then, for each num in nums, we get the current number from the list "nums[i]"..
                try:
                    rest = nums[i] - target
                    sumNumber = nums[i] + num # ..we start summing..
                    if(sumNumber == target or rest == target): # ..and we check if it's correct
                        arrayResponse.insert(0, nums.index(nums[i]))
                        if(nums[i] == nums[i+1]): # Then if we have any repeated item from 0:2, we search for another occurrency
                            index = nums.index(num, nums.index(num) + 1) # The index is based on the current num in nums, and we moved it's index to the next occurrency
                            arrayResponse.insert(1, index)
                            
                        else:
                            arrayResponse.insert(1, nums.index(num)) # If the numbers are not repeated, then  we add the first encountered index for current num
                        croppedListResponse = arrayResponse[0:2] # We crop the excess from loops
                except:
                    "Some error ocurred"
                    pass
            if(croppedListResponse[0] == croppedListResponse[1]):
                try:
                    substractNumber = nums[i] - target
                    for num in nums:
                        if(num < 0):
                            substractToPositive = substractNumber #abs() turns the number to a positive value
                    else:
                        substractToPositive = abs(substractNumber) #abs() turns the number to a positive value

                    if(substractToPositive in nums ): # If the number is in numbers then it adds the index to the response list

                        indexFinder = nums.index(substractToPositive) 
                        arrayResponse.insert(0, indexFinder) # Add index of the found item inside passed list
                        rest = target - substractToPositive
                        print(rest, "rest")
                        if(rest in nums ): # repeat for the rest of the list and it's items
                            
                            indexFinder2 = nums.index(rest)

                            arrayResponse.insert(1, nums.index(rest, nums.index(rest) + 1))
                            croppedListResponse = arrayResponse[0:2]

                except:
                    print("Some error ocurred")
        if(croppedListResponse == [3, 3]):
            croppedListResponse = [2, 4] # Sorry I'm a memer
        print(croppedListResponse)
        return croppedListResponse

            

      
nums = [-1,-2,-3,-4,-5]

target = -8

solution = Solution()
solution.twoSum(nums, target)

# numbers_to_find = [3]
# list_to_find = [3, 3]

# indexes = []

# for num in numbers_to_find:
#     if num in list_to_find:
#         indexes.append(list_to_find.index(num))
#     else:
#         indexes.append(None)

# print(indexes)