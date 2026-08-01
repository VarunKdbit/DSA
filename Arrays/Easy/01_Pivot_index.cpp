/*

PIVOT INDEX (ARRAYS)


Topic        : Arrays, Prefix Sum
Difficulty   : Easy
Pattern      : Prefix Sum / Running Sum


PROBLEM OVERVIEW

Given an integer array, find the first index where the sum of all elements on
its left is equal to the sum of all elements on its right.

The current element itself should not be included in either the left or the
right sum.

Return the index if such a position exists; otherwise, return -1.


EXAMPLE


Input:
[1, 7, 3, 6, 5, 6]

Output:
3

Explanation:

Left Side  = 1 + 7 + 3 = 11
Right Side = 5 + 6 = 11

Since both sums are equal, index 3 is the pivot index.

IDEA :
Calculating the left and right sums separately for every index would require
multiple passes over the array.

Instead:

1. Compute the total sum once.
2. Maintain a running left sum.
3. Derive the right sum using:

       rightSum = totalSum - leftSum - nums[i]

4. If leftSum equals rightSum, return the current index.



TIME COMPLEXITY : O(n)
SPACE COMPLEXITY : O(1)

*/

class Solution {
public:
    int pivotIndex(vector<int>& nums) {

        int totalSum = 0;

        for (int num : nums)
            totalSum += num;

        int leftSum = 0;

        for (int i = 0; i < nums.size(); i++) {

            int rightSum = totalSum - leftSum - nums[i];

            if (leftSum == rightSum)
                return i;

            leftSum += nums[i];
        }

        return -1;
    }
};

