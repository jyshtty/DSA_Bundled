import os

# Dictionary of file paths to their comment strings
comments_dict = {
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/01_Sort_an_array_of_0_1_2/Sort_an_array_of_0_1_2.py": """# leetcode 75: Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# https://leetcode.com/problems/sort-colors/
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Approach: Counting sort
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/01_Sort_an_array_of_0_1_2/dutch_national_flag_algo.py": """# leetcode 75: Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# https://leetcode.com/problems/sort-colors/
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Approach: Dutch National Flag algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/01_Sort_an_array_of_0_1_2/without_space.py": """# leetcode 75: Sort Colors
# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
# https://leetcode.com/problems/sort-colors/
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
# Approach: Counting sort
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/02_Repeat_and_Missing_Number/solution_01.py": """# Repeat and Missing Number
# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# Example:
# Input: [3,1,2,5,3]
# Output: [3,4]
# Approach: Using math - sum and sum of squares
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/02_Repeat_and_Missing_Number/solution_02.py": """# Repeat and Missing Number
# You are given a read only array of n integers from 1 to n.
# Each integer appears exactly once except A which appears twice and B which is missing.
# Return A and B.
# https://www.interviewbit.com/problems/repeat-and-missing-number-array/
# Example:
# Input: [3,1,2,5,3]
# Output: [3,4]
# Approach: Using XOR
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/03_kadanes_algorithm/kadanes_algorithm.py": """# leetcode 53: Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# https://leetcode.com/problems/maximum-subarray/
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Approach: Kadane's algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/03_Merge_two_sorted_array/solution_01.py": """# leetcode 88: Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums2 into nums1 as one sorted array.
# https://leetcode.com/problems/merge-sorted-array/
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Approach: Three pointers from end
# Time Complexity: O(m+n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/03_Merge_two_sorted_array/solution_02.py": """# leetcode 88: Merge Sorted Array
# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums2 into nums1 as one sorted array.
# https://leetcode.com/problems/merge-sorted-array/
# Example 1:
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Approach: Using extra space
# Time Complexity: O(m+n)
# Space Complexity: O(m+n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/04_longest_substring_non_repeating/04_longest_substring_non_repeating.py": """# leetcode 3: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Approach: Sliding window with hash set
# Time Complexity: O(n)
# Space Complexity: O(min(n, 26))
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/04_longest_substring_non_repeating/optimized_approach.py": """# leetcode 3: Longest Substring Without Repeating Characters
# Given a string s, find the length of the longest substring without repeating characters.
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Example 1:
# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Approach: Sliding window optimized
# Time Complexity: O(n)
# Space Complexity: O(min(n, 26))
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/05_merge_intervals/05_merge_intervals.py": """# leetcode 56: Merge Intervals
# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.
# https://leetcode.com/problems/merge-intervals/
# Example 1:
# Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Approach: Sort and merge
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/06_next_permutation/next_permution.py": """# leetcode 31: Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# https://leetcode.com/problems/next-permutation/
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Approach: Find the first decreasing element from right, swap with next greater, reverse the rest
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/06_next_permutation/Go_through_this.py": """# leetcode 31: Next Permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# https://leetcode.com/problems/next-permutation/
# Example 1:
# Input: nums = [1,2,3]
# Output: [1,3,2]
# Approach: Find the first decreasing element from right, swap with next greater, reverse the rest
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/07_Set_Matrix_Zero/solution.py": """# leetcode 73: Set Matrix Zeroes
# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# https://leetcode.com/problems/set-matrix-zeroes/
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Approach: Use first row and column as markers
# Time Complexity: O(m*n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/07_Set_Matrix_Zero/brute_force.py": """# leetcode 73: Set Matrix Zeroes
# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# https://leetcode.com/problems/set-matrix-zeroes/
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Approach: Brute force - mark rows and columns
# Time Complexity: O(m*n*(m+n))
# Space Complexity: O(m+n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/new_pascal.py": """# leetcode 118: Pascal's Triangle
# Given an integer numRows, return the first numRows of Pascal's triangle.
# https://leetcode.com/problems/pascals-triangle/
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
# Approach: Dynamic programming
# Time Complexity: O(n^2)
# Space Complexity: O(n^2)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/new_Set_matric_zeros.py": """# leetcode 73: Set Matrix Zeroes
# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# https://leetcode.com/problems/set-matrix-zeroes/
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Approach: Use first row and column as markers
# Time Complexity: O(m*n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/new_kmp_return_substring/brute_force.py": """# Implement strStr()
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# https://leetcode.com/problems/implement-strstr/
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Approach: Brute force
# Time Complexity: O((n-m+1)*m)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/new_kmp_return_substring/kmp_return_substring.py": """# Implement strStr()
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
# https://leetcode.com/problems/implement-strstr/
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
# Approach: KMP algorithm
# Time Complexity: O(n+m)
# Space Complexity: O(m)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day1_Arrays/set_matrix_zeros.py": """# leetcode 73: Set Matrix Zeroes
# Given an m x n integer matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
# https://leetcode.com/problems/set-matrix-zeroes/
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
# Approach: Use first row and column as markers
# Time Complexity: O(m*n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day2_Arrays/01_buy_and_sell_stocks/01_buy_and_sell_stocks.py": """# leetcode 121: Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Approach: Keep track of min price and max profit
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day2_Arrays/01_buy_and_sell_stocks/01_optimized.py": """# leetcode 121: Best Time to Buy and Sell Stock
# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Approach: Keep track of min price and max profit
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day2_Arrays/Rotate_Matrix/Transpose_and_reverse.py": """# leetcode 48: Rotate Image
# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.
# https://leetcode.com/problems/rotate-image/
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
# Approach: Transpose then reverse each row
# Time Complexity: O(n^2)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day2_Arrays/srarch_in_2DMatrix.py": """# leetcode 74: Search a 2D Matrix
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# https://leetcode.com/problems/search-a-2d-matrix/
# Example 1:
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# Approach: Binary search
# Time Complexity: O(log(m*n))
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day3_Arrays/4sum.py": """# leetcode 18: 4Sum
# Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
# https://leetcode.com/problems/4sum/
# Example 1:
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Approach: Two pointers
# Time Complexity: O(n^3)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day3_Arrays/sum_of_given_subarray.py": """# leetcode 53: Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# https://leetcode.com/problems/maximum-subarray/
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Approach: Kadane's algorithm
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day5_LinkedList/Add_Two_Numbers.py": """# leetcode 2: Add Two Numbers
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.
# https://leetcode.com/problems/add-two-numbers/
# Example 1:
# Input: l1 = [2,4,3], l2 = [5,6,4]
# Output: [7,0,8]
# Explanation: 342 + 465 = 807.
# Approach: Traverse both lists, add digits with carry
# Time Complexity: O(max(m,n))
# Space Complexity: O(max(m,n))
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day5_LinkedList/delete_node_in_ll.py": """# leetcode 237: Delete Node in a Linked List
# Write a function to delete a node in a singly-linked list. You will not be given access to the head of the list, instead you will be given access to the node to be deleted directly.
# It is guaranteed that the node to be deleted is not a tail node in the list.
# https://leetcode.com/problems/delete-node-in-a-linked-list/
# Example 1:
# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Approach: Copy next node's value and delete next node
# Time Complexity: O(1)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day5_LinkedList/Merge_2_Sorted_LL.py": """# leetcode 21: Merge Two Sorted Lists
# You are given the heads of two sorted linked lists list1 and list2.
# Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
# Return the head of the merged linked list.
# https://leetcode.com/problems/merge-two-sorted-lists/
# Example 1:
# Input: list1 = [1,2,4], list2 = [1,3,4]
# Output: [1,1,2,3,4,4]
# Approach: Iterative merge
# Time Complexity: O(m+n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day5_LinkedList/Middle_of_LinkedList.py": """# leetcode 876: Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
# If there are two middle nodes, return the second middle node.
# https://leetcode.com/problems/middle-of-the-linked-list/
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Approach: Fast and slow pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day5_LinkedList/Remove_nth_node_from_back.py": """# leetcode 19: Remove Nth Node From End of List
# Given the head of a linked list, remove the nth node from the end of the list and return its head.
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Example 1:
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
# Approach: Two pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day5_LinkedList/Reverse_a_LinkedList.py": """# leetcode 206: Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
# https://leetcode.com/problems/reverse-linked-list/
# Example 1:
# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]
# Approach: Iterative reversal
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day6_LinkedList/01_Reverse_Group_in_k_nodes.py": """# leetcode 25: Reverse Nodes in k-Group
# Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.
# If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.
# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Example 1:
# Input: head = [1,2,3,4,5], k = 2
# Output: [2,1,4,3,5]
# Approach: Reverse in groups
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day6_LinkedList/02_Swap_LisT_Nodes_in_Pairs.py": """# leetcode 24: Swap Nodes in Pairs
# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Example 1:
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Approach: Iterative swap
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day6_LinkedList/Intersection_of_2_LL.py": """# leetcode 160: Intersection of Two Linked Lists
# Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Example 1:
# Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
# Output: Intersected at '8'
# Approach: Two pointers
# Time Complexity: O(m+n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day6_LinkedList/LL_cycle_detection.py": """# leetcode 141: Linked List Cycle
# Given head, the head of a linked list, determine if the linked list has a cycle in it.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
# https://leetcode.com/problems/linked-list-cycle/
# Example 1:
# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Approach: Fast and slow pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day6_LinkedList/Palindrome_Linked_list.py": """# leetcode 234: Palindrome Linked List
# Given the head of a singly linked list, return true if it is a palindrome.
# https://leetcode.com/problems/palindrome-linked-list/
# Example 1:
# Input: head = [1,2,2,1]
# Output: true
# Approach: Find middle, reverse second half, compare
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day7_LL_andArray/CopyLLwith_Random_Pointer.py": """# leetcode 138: Copy List with Random Pointer
# A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.
# Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node.
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Example 1:
# Input: head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Output: [[7,null],[13,0],[11,4],[10,2],[1,0]]
# Approach: Hash map or interweave nodes
# Time Complexity: O(n)
# Space Complexity: O(n) for hash map, O(1) extra for interweave
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day7_LL_andArray/Rain_water_trapping/Prefix_max_array_approach.py": """# leetcode 42: Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# https://leetcode.com/problems/trapping-rain-water/
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Approach: Prefix max arrays
# Time Complexity: O(n)
# Space Complexity: O(n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day7_LL_andArray/Rain_water_trapping/Two_pointer_approach.py": """# leetcode 42: Trapping Rain Water
# Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.
# https://leetcode.com/problems/trapping-rain-water/
# Example 1:
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Approach: Two pointers
# Time Complexity: O(n)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day8_Greedy/N_meetings_in_one_room.py": """# N Meetings in One Room
# There is one meeting room in a firm. There are N meetings in the form of (start[i], end[i]) where start[i] is start time of meeting i and end[i] is finish time of meeting i.
# What is the maximum number of meetings that can be accommodated in the meeting room when only one meeting can be held in the meeting room at a particular time?
# https://practice.geeksforgeeks.org/problems/n-meetings-in-one-room-1587115620/1
# Example:
# Input: N = 6, start[] = {1,3,0,5,8,5}, end[] = {2,4,6,7,9,9}
# Output: 4
# Approach: Sort by end time, greedy select
# Time Complexity: O(n log n)
# Space Complexity: O(n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day9_Recurrsion/01_Generate_Permutation_of_Binary_String.py": """# Generate all binary strings of length n
# Given an integer n, generate all binary strings of length n.
# Example:
# Input: n = 2
# Output: ['00', '01', '10', '11']
# Approach: Recursion
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day9_Recurrsion/02_Generate_All_Permutation.py": """# leetcode 46: Permutations
# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.
# https://leetcode.com/problems/permutations/
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
# Approach: Backtracking
# Time Complexity: O(n!)
# Space Complexity: O(n!)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day9_Recurrsion/03_Generate_All_Permutation_with_Repitation.py": """# Permutations with repetition
# Given an array nums that may contain duplicates, return all possible unique permutations in any order.
# Example:
# Input: nums = [1,1,2]
# Output: [[1,1,2],[1,2,1],[2,1,1]]
# Approach: Backtracking with used array
# Time Complexity: O(n!)
# Space Complexity: O(n!)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day9_Recurrsion/04_Generate_Parenthesis.py": """# leetcode 22: Generate Parentheses
# Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
# https://leetcode.com/problems/generate-parentheses/
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Approach: Backtracking
# Time Complexity: O(4^n / sqrt(n))
# Space Complexity: O(4^n / sqrt(n))
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day9_Recurrsion/05_Generate_All_Subsets.py": """# leetcode 78: Subsets
# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# https://leetcode.com/problems/subsets/
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
# Approach: Backtracking
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day9_Recurrsion/06_Generate_All_Subsets_with_Dup.py": """# leetcode 90: Subsets II
# Given an integer array nums that may contain duplicates, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# https://leetcode.com/problems/subsets-ii/
# Example 1:
# Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
# Approach: Backtracking with sorting
# Time Complexity: O(2^n)
# Space Complexity: O(2^n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day9_Recurrsion/07_Combination_sum.py": """# leetcode 39: Combination Sum
# Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.
# The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# https://leetcode.com/problems/combination-sum/
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Approach: Backtracking
# Time Complexity: O(2^target) worst case
# Space Complexity: O(target)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day9_Recurrsion/08_Combination_sum2.py": """# leetcode 40: Combination Sum II
# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.
# Each number in candidates may only be used once in the combination.
# Note: The solution set must not contain duplicate combinations.
# https://leetcode.com/problems/combination-sum-ii/
# Example 1:
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: [[1,1,6],[1,2,5],[1,7],[2,6]]
# Approach: Backtracking with sorting
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Day9_Recurrsion/09_Palindrome_Partition.py": """# leetcode 131: Palindrome Partitioning
# Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.
# https://leetcode.com/problems/palindrome-partitioning/
# Example 1:
# Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
# Approach: Backtracking
# Time Complexity: O(2^n)
# Space Complexity: O(n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Days10_Backtracking/Letter_Phone_Number.py": """# leetcode 17: Letter Combinations of a Phone Number
# Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Example 1:
# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
# Approach: Backtracking
# Time Complexity: O(3^n * 4^m) where n is number of digits with 3 letters, m with 4
# Space Complexity: O(3^n * 4^m)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Days10_Backtracking/N_Queen.py": """# leetcode 51: N-Queens
# The n-queens puzzle is the problem of placing n queens on an n x n chessboard so that no two queens attack each other.
# Given an integer n, return all distinct solutions to the n-queens puzzle. You may return the answer in any order.
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' indicate a queen and an empty space, respectively.
# https://leetcode.com/problems/n-queens/
# Example 1:
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Approach: Backtracking
# Time Complexity: O(n!)
# Space Complexity: O(n^2)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Days10_Backtracking/Rat_in_Maze.py": """# Rat in a Maze
# Consider a rat placed at (0, 0) in a square matrix of order N * N. It has to reach the destination at (N - 1, N - 1). Find all possible paths that the rat can take to reach from source to destination.
# The directions in which the rat can move are 'U'(up), 'D'(down), 'L' (left), 'R' (right). Value 0 at a cell in the matrix represents that it is blocked and rat cannot move to it while value 1 at a cell in the matrix represents that rat can be travel through it.
# Note: In a path, no cell can be visited more than one time.
# Example:
# Input: N = 4, m[][] = {{1, 0, 0, 0}, {1, 1, 0, 1}, {1, 1, 0, 0}, {0, 1, 1, 1}}
# Output: DDRDRR DRDDRR
# Approach: Backtracking
# Time Complexity: O(4^(n^2))
# Space Complexity: O(n^2)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Days10_Backtracking/Sudoko_solver.py": """# leetcode 37: Sudoku Solver
# Write a program to solve a Sudoku puzzle by filling the empty cells.
# A sudoku solution must satisfy all of the following rules:
# Each of the digits 1-9 must occur exactly once in each row.
# Each of the digits 1-9 must occur exactly once in each column.
# Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# The '.' character indicates empty cells.
# https://leetcode.com/problems/sudoku-solver/
# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],["6","7","2","1","9","5","3","4","8"],["1","9","8","3","4","2","5","6","7"],["8","5","9","7","6","1","4","2","3"],["4","2","6","8","5","3","7","9","1"],["7","1","3","9","2","4","8","5","6"],["9","6","1","5","3","7","2","8","4"],["2","8","7","4","1","9","6","3","5"],["3","4","5","2","8","6","1","7","9"]]
# Approach: Backtracking
# Time Complexity: O(9^(81-k)) where k is number of filled cells
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Days10_Backtracking/Valid_Sudoko.py": """# leetcode 36: Valid Sudoku
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:
# Each row must contain the digits 1-9 without repetition.
# Each column must contain the digits 1-9 without repetition.
# Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
# Note: A Sudoku board (partially filled) could be valid but is not necessarily solvable.
# Only the filled cells need to be validated according to the mentioned rules.
# https://leetcode.com/problems/valid-sudoku/
# Example 1:
# Input: board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
# Output: true
# Approach: Check rows, columns, boxes
# Time Complexity: O(1)
# Space Complexity: O(1)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Days10_Backtracking/Word_Break.py": """# leetcode 139: Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.
# https://leetcode.com/problems/word-break/
# Example 1:
# Input: s = "leetcode", wordDict = ["leet","code"]
# Output: true
# Approach: DP or backtracking with memo
# Time Complexity: O(n^2)
# Space Complexity: O(n)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/Days10_Backtracking/Word_Search.py": """# leetcode 79: Word Search
# Given an m x n grid of characters board and a string word, return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.
# https://leetcode.com/problems/word-search/
# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
# Approach: Backtracking
# Time Complexity: O(m*n*4^L) where L is word length
# Space Complexity: O(L)
# Implementation:
""",
    "/workspaces/DSA_Bundled/Topicwise/scaler_and_striver/Striver_DSA_Sheet/test.py": """# Test file
# This is a test file.
# No problem description needed.
""",
}

for file_path, comment in comments_dict.items():
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            content = f.read()
        # Check if already has comments
        if content.startswith('# leetcode') or content.startswith('# Repeat') or content.startswith('# Implement') or content.startswith('# N Meetings') or content.startswith('# Generate') or content.startswith('# Rat') or content.startswith('# Test'):
            print(f"Skipping {file_path}, already has comments")
            continue
        new_content = comment + "\n\n" + content
        with open(file_path, 'w') as f:
            f.write(new_content)
        print(f"Added comments to {file_path}")
    else:
        print(f"File not found: {file_path}")