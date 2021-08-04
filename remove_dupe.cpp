// Remove immediate duplicates in a provided string

string solve(string s) { // Declairs a function solve, which accepts the variable 's' and turns it into a string form.
    auto last = std::unique(s.begin(), s.end()); // auto declaires the variable 'last' automatically depending on what type of data is written to it.
                                                // std::unique removes all duplicate chars in the string from the beginning(s.begin()) until the end(s.end())
    s.erase(last, s.end()); // erases the end of the string that is not able to be processed by the unique function above.
    return s; // 'nuff said
}

// Your code took 3 milliseconds — faster than 99.60% in C++
