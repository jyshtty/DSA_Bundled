# coding=utf-8
"""
Change Date Format
Given a date string in the format Day Month Year, where:

Day is in the set {"1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", ..., "29th", "30th", "31st"}.
Month is in the set {"Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"}.
Year is in the inclusive range [1900, 3000].

Convert the date string to the format YYYY-MM-DD, where:

YYYY denotes the 4 digit year.
MM denotes the 2 digit month.
DD denotes the 2 digit day.
For example:

1st Mar 1984 → 1984-03-01
2nd Feb 2013 → 2013-02-02 4th Apr 1900 → 1900-04-04



Input Format

The only argument given is a String, a date in the above-mentioned format.
Output Format

Return a String, i.e date in YYYY-MM-DD format.
Constraints

The values of Day, Month, and Year are restricted to the value ranges specified above.
The given dates are guaranteed to be valid, so no error handling is necessary.
Sample Test 1

Input:
    A = "16th Mar 2068"
Output:
    2068-03-16
Sample Test 2

Input:
    A = "6th Jun 1933"
Output:
    1933-06-06
"""

class Solution:
    # @param A : string
    # @return a strings
    def solve(self, A):
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        month_dict = {}
        for i in range(len(month)):
            if i+1 < 10:
                month_dict[month[i]] = '0'+ str(i+1)
            else:
                month_dict[month[i]] = str(i+1)
        ls = A.split(' ')
        import re

        date = re.search(r"\d+", ls[0]).group(0)
        if len(date) == 1:
            date = '0' + date

        return "{}-{}-{}".format(ls[2], month_dict[ls[1]], date)



if __name__ == "__main__":
    A = "16th Mar 2068"
    obj = Solution()
    print(obj.solve(A))

