Here is the Universal Sliding Window Template 🔥 — this single pattern solves 90% of Amazon / LinkedIn sliding window problems.

Once you master this, problems like:

Longest Substring Without Repeating Characters

Longest Substring With At Most K Distinct

Minimum Window Substring

Character Replacement

Fruit Into Baskets

Permutation in String

all become easy.

Universal Sliding Window Template 🚀
class Solution:
    def slidingWindowTemplate(self, s, k):

        l = 0
        hm = {}

        result = 0   # or float('inf') for minimum problems

        for r in range(len(s)):

            # 1. Expand window
            hm[s[r]] = hm.get(s[r], 0) + 1

            # 2. Shrink window (invalid condition)
            while not self.isValid(hm, k):
                
                hm[s[l]] -= 1
                
                if hm[s[l]] == 0:
                    del hm[s[l]]
                    
                l += 1

            # 3. Update result
            result = max(result, r-l+1)

        return result
How to Customize 🎯
1️⃣ Longest Substring Without Repeating Characters
Condition
Window must have no duplicates

while hm[s[r]] > 1:
Code
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        l = 0
        hm = {}
        max_len = 0

        for r in range(len(s)):

            hm[s[r]] = hm.get(s[r],0) + 1

            while hm[s[r]] > 1:
                hm[s[l]] -= 1
                
                if hm[s[l]] == 0:
                    del hm[s[l]]
                    
                l += 1

            max_len = max(max_len, r-l+1)

        return max_len
2️⃣ At Most K Distinct Characters ⭐
Condition
while len(hm) > k:
3️⃣ Minimum Window Substring ⭐⭐⭐
Result Initialization
result = float('inf')
Update Result
result = min(result, r-l+1)
Valid Condition
Window must contain all characters.

4️⃣ Character Replacement (Amazon Favorite)
Condition:

window_size - maxFreq <= k
Invalid condition:

(r-l+1) - maxFreq > k
Golden Rule 🔥
Every sliding window problem has 3 steps

1️⃣ Expand
hm[s[r]] += 1
2️⃣ Shrink
while window_invalid:
    remove s[l]
    l += 1
3️⃣ Update answer
max_len = max(max_len, r-l+1)
Interview Cheat Sheet ⭐⭐⭐
Problem Type	Condition
No Repeats	hm[s[r]] > 1
K Distinct	len(hm) > k
Replacement	(r-l+1) - maxFreq > k
Sum ≥ Target	windowSum >= target
Permutation	window size == len(s1)
