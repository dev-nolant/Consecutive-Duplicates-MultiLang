// Remove immediate duplicates in a provided string

string solve(string s) { // Declairs a function solve, which accepts the variable 's' and turns it into a string form.
    s.erase(unique(s.begin(), s.end()), s.end()); // std::unique removes all duplicate chars in the string from the beginning(s.begin()) until the end(s.end())
    return s; // 'nuff said
}

// Your code took 3 milliseconds — faster than 99.60% in C++
