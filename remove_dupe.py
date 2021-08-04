# Remove immediate duplicates in a provided string

class Solution: # 'nuff said
    def solve(self, s): # declaires a function under the name of 'solve', which accepts the argument for s. The class declaired above allows the used of 'self' in order to tidy up and speed up our code
        temp = "" # creates an empty string named 'temp'
        new = [] # creates an empty array named 'new'
        string_form = '' # creates an empty string named 'string_form'
        for i in list(s): # this is a for loop, which will repeat itself over and over, but everytime it repeats, it will assign the next char in a list to whatever variable you desire, which in my case is 'i' being declaired a new char from s.
                          # 'list(s)' turns the string [s] into a list/array
            if i == temp: # if the current char equals the previous char, then:
                temp = i # the 'previous char' mentioned before is assigned the current char
            else: # 'nuff said
                temp = i # the 'previous char' mentioned before is assigned the current char
                new.append(temp) # if previous char does not equal the current char, then it's appended/added to the array called 'new'
        return ''.join(new) # once the for loop finishes, the array 'new' is turned back into the string form using 'join' and returned 


# Your code took 5 milliseconds — faster than 95.92% in Python :: https://binarysearch.com/problems/Consecutive-Duplicates
