Say if I give to 3 digit -  5 7 8.
and 
ask you to make largest number out og it. 
you will say it would be 875

if you observe it is in decending order.
Hence no matter how you arrange it is always the decending order that is going to be largest.

So the intution is based on above observeration.

steps 1 - Iterate from back. Find the index of the element which is less then the prev element. here
ex - 13542. 
In above example, 3 is the elemnet which is less than prev element. 
index of 3 is 1

step 2 - interate again from back. find a number that is greater than 3. 
ex - 
here 4 is the element and its index is 3

step 3 - swap index 1 with 3. 
ex - 13542 -- 14532

step 4 - is reverse after index 1
ex - 14235

=================

corner case - if it is 54321 just reverse it.

==========================


class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums) - 1, -1, -1):
            if i == 0:
                return nums[::-1]

            if nums[i] > nums[i - 1]:
                index1 = i - 1
                break

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[index1]:
                nums[i], nums[index1] = nums[index1], nums[i]
                break

        to_rev = nums[index1 + 1:]
        ans = nums[:index1] + to_rev[::-1]
        return ans
