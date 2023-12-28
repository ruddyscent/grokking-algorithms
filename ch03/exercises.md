# Chapter 3 Recursion

### 3.1
In the `greet` function, a variable named `name` is defined with the value "Maggie," and then the `greet2` function is invoked. Within `greet2`, another variable named `name` is defined with the value "Maggie."

### 3.2
When a recursive function runs forever, it keeps making new function calls without reaching a base case to stop the recursion. As a result, the stack memory allocated for each function call accumulates, leading to a stack overflow.

A stack overflow occurs when the available stack space is exhausted due to an excessive number of function calls. In the case of an infinite recursive function, the stack continues to grow, and eventually, it exceeds the system's stack size limit.

When a stack overflow happens, the program typically crashes, and you may encounter a runtime error. This error indicates that the call stack has reached or exceeded its maximum capacity, and the system cannot allocate more space for new function calls. It's a common issue associated with infinite or deeply recursive functions.