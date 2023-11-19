#include <iostream>

#include <vector>

#include <algorithm>
/*
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.


*/

/* === Approach ===
Ok, I should just check for the number that DOESN'T repeats,
then output that one.

1) Lets get the vectors
2) then add into another vector the numbers that are repeated
3) Then for that new vector, lets check each number and
4) get them out from the OG
vector.

That would give us the non repeated number.

For now I want to just iterate i over the given vector, check the repeated number with the
last occurrency, the add the occurrency that was repeated to the newVector.

Gotta get the new and last value of i

I think its pretty self explanatory by now.

Then for this will try to give a O(1) solution.

Ok so the leetcode compiler was complaining about a return smth and a ;

Test cases are ok, let's check the rest

Seems like there are cases for less than one integers, lets fix that.

Lets check now.

Ok this case works. Thing is, it's O(n) (linear time), in time complexity.
Results by now:
Runtime: 882 ms, beats 5.08% of users
Memory:  17.17 mb, beats 80.21% of users


*/

class Solution
{
public:
    std::vector<int> newVector = {}; // Disposable vector (array)

    int singleNumber(std::vector<int> &nums)
    {

        // for (int i = 1; i <= 5; ++i)
        // {
        //     std::cout << i << " ";
        // }
        // std::cout << std::endl;

        for (int i = 0; i <= nums.size(); ++i)
        {
            auto findRepeatedNumber = std::count(nums.begin(), nums.end(), nums[i]); // this will count each time i is inside Nums 

            std::cout << "value of i" << i << std::endl;

            std::cout << "value of nums[i]" << nums[i] << std::endl;

            if ( findRepeatedNumber > 1 )
            { 
                std::cout << "Number IS repeated" << i << std::endl;
                std::cout << "is inside" << std::endl;
            }
            else if (findRepeatedNumber == 1)
            {
                std::cout << "Not repeated and only once" << " " << nums[i] << std::endl;
                newVector.push_back(nums[i]);

                std::cout << "Checking for correct newVector index at 0 = " << " " <<  newVector[0] << std::endl;

                return newVector[0];
            } 

        }
        return newVector[0]; // This is for the complainer i mean the compiler of leetcode
        std::cout << "msg are displaying" << std::endl;
    }
};

int main()
{
    // Create an object of the class
    Solution myObject;
    std::vector<int> numbers = {-1, -1, -2};

    // Call a member function of the object
    myObject.singleNumber(numbers);

    return 0;
}

/*
Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1


Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.


*/
