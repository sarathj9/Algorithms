Minimized Cookie Distribution
------------------------------
------------------------------
####Problem: 
Minimize cookie distribution to students based on their marks with following constraints
- [x] Position of the students is fixed.
- [x] Every student should get at least one cookie.
- [x] A student can only see the marks obtained to his neighbours. Meaning, he can be compared with only his neighbouring
      students 
- [x] cookies are directly proportional to their marks. 
 
    
####Solution:
Degenerated cases:
--- All have got same cookies: all should get only one cookie
--- Students have got scores in increasing order or decreasing order: No. of cookies distributed can never be minimized 
less than the  maximum possible cookies `n!`

Student scores : [5, 9, 19, 20, 29, 45, 85, 100]
Cookies        : [1, 2, 3, 4, 5, 6, 7, 8]

So the key idea I have taken is identify all possible increasing sequence of scores and assign cookies in incremental 
order starting from 1, for every such sequence. And then Identify the boundaries, where the increasing sequence has 
broken and assign 1 cookie each. Now we have to check, only at these boundaries whether there are any violations. 

####Examples:
Student scores : [1, 2, 3, 4, 5, 6]
Cookies        : [1, 2, 3, 4, 5, 6]

Student scores : [4, 1, 2, 3, 1, 4, 9, 11]
Cookies        : [2, 1, 2, 3, 1, 2, 3, 4]

Student scores : [15, 20, 5, 21, 50, 20, 11, 6, 10, 19, 11, 8, 9, 12]
Cookies        : [1, 2, 1, 2, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3]

Student scores : [1, 2, 1, 2, 4, 3, 2, 1, 2, 3, 2, 1, 2, 3]
Cookies        : [1, 2, 3, 4, 3, 2, 1]

Student scores : [5, 10, 15, 11, 9, 8, 13, 25, 40, 50, 35, 12, 7]
Cookies        : [1, 2, 4, 3, 2, 1, 2, 3, 4, 5, 3, 2, 1]

