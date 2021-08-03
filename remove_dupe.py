# Remove immediate duplicates in a string

class Solution:
    def solve(self, s):
        temp = ""
        new = []
        string_form = ''
        for i in list(s):
            if i == temp:
                temp = i
            else:
                temp = i
                new.append(temp)
        return ''.join(new)


# Your code took 5 milliseconds — faster than 95.92% in Python :: https://binarysearch.com/problems/Consecutive-Duplicates