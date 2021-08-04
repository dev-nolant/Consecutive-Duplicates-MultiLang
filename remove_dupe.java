// Remove immediate duplicates in a provided string.

import java.util.*; // important import of the collection framework : ect/.

class Solution { // 'nuff said
    public String solve(String s) { // sets the argument included to the variable s in the string type.
        StringBuilder result = new StringBuilder(); // Creates the array result, which will be converted into a string representation when called upon.
        char lastChar = Character.UNASSIGNED; // Character contains a single field, which is typed char. The Unassigned tag clears the single field of Character.
        for (char currentChar : s.toCharArray()) { // this is a for loop, which declairs a new variable: 'currentChar' the value of the current character selected in the char array.
                                                   // The 's.toCharArray' turns the string s, which is declaired in the public statement above, into an array of chars(characters).
            if (!Objects.equals(currentChar, lastChar)) { // If the current Objects don't equal eachother, then the current character is appended to the result array.
                result.append(currentChar); // Add(Append) the current character selected into the result array, if the current requirements/filters are met
            }
            lastChar = currentChar; // 'nuff said, but I will note, this saves time and the possibility of having to plugin pointers.
        }
        return result.toString(); // 'nuff said, but I will note, this is not a System.out.print(), because we're not looking to print out the answer, but instead to turn the result
                                  // from an array into a string, and then return the value under the public String class
    }
}
// Note: 's.toCharArray' can be compaired to Python's 'list(string)' statement

// Your code took 7 milliseconds — faster than 95.29% in Java
