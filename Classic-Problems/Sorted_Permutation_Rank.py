# Idea - 

# # If you want to find rank of cbdae

# # find all the words that occur before c + (with d fixed in first place find all the words starting with b in second place) + and so on

# # all the words that occur before d in first place is 2 * factorial (4)
# # 2 because there are 2 letters less than c - a and b

# # with a fixed in first place, there are 4 places left to fill with 4 different characters which is given by 4!. hence it is 2 * 4!


# step1 - Sort the given array. 
# step2 - compare every char in given array with sorted array. 
# step3 - if it is found in visted it means that char has been already used(because we put in vis only if it is used), Hence skip. Dont increment c. 
# Here c plays a important role. it keeps the count of number of character less than current given array character.

# step4 - if char in sorted array is greater than or equal, break the for loop. We don't need any to check any other.
# (As we know 2nd for loop string is already sorted)

# step5 - if step fails, it wont continue, if step 4 fails it wont break for loop. Then you increment c by 1

# step6- for every iteration of inner loop. calculate res += c * factorial(lna - e)

# step7 - increment e for every iteration of inner loop



from math import factorial
class Solution:
    # @param A : string
    # @return an integer
    def findRank(self, A):
        res = 0
        s = sorted(A)
        lna = len(A)
        e = 1
        vis = set()
        for i in A:
            c = 0
            for j in s:
                if j in vis:
                    continue
                if j >= i:
                    vis.add(j)
                    break
                c += 1
            res += c * factorial(lna - e)
            e += 1
        return (res + 1) % 1000003
