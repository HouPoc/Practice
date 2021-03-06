# LeetCode Lesson



* **[Judge Route Circle - 657](https://leetcode.com/problems/judge-route-circle/description/)**
    * Hint
        
        This problem is *entry* level. The key to solve this problem is to understand that 
        
        Moves to opposed  directions. If the robot is in its original position, 
        
        it should **have same amount of opposed moves** 
    
    * Analysis
        * O(n) time complexity. 
        * O(1) space complexity.
         
 
 
* **[Divided Two Integers - 29](https://leetcode.com/problems/divide-two-integers/description/)**
    * Hint
        
        This problem is *medium* level according to LeetCode,
        
        Before to solve this problem, you should know the definition of **Overflow** and range of **Int**.
         
        * **Overflow** -- The value of a numerical variable goes beyond the range of its variable type
        * **Int** -- 16 bits (-2147483648 to 2147483647)
        
        There are two cases in this problem: dividend and divisor have the same sign; divided and divisor have different signs.
        
        Division is a serial of subtractions.
        
        Simple subtraction is too slow to solve this effectively.
        
        greedy subtraction -- subtract the largest available dividend (dividend - divisor ^ n) and repeat. 
        
    * Analysis
        * O(nlog(n)) time complexity.
        * O(1) space complexity.

*   **[Distribute Candies - 575](https://leetcode.com/problems/distribute-candies/description/)**

    * Hint

        This problem is *easy* level.

        The sister only can get **the half amount** of candies so that the candies types she holds is less than that.

        If there is no enough candy types, she can only choose **existing types of candies**.

        Otherwise, her candies is not duplicated.

    * Analysis

        * O(n) time complexity
        * O(1) space complexity

    * Python built-in functions

        ```python
           #get unique candy list
           set()
           #count list element
           len()
        ```

*   **[Swap Salary - 627](https://leetcode.com/problems/swap-salary/description/)**

    * Hint

        This problem is *easy* level.

        This is a simple SQL query with UPDATE and CASE.

        Be careful about requirements.

    * MySQL Query
        ```sql
            UPDATE salary a
                SET a.sex = ( CASE WHEN a.sex = 'f'
                              THEN 'm'
                              ELSE 'f'
                              END)
        ```

* **[Not Boring Movie - 620](https://leetcode.com/problems/not-boring-movies/description/)**

    * Hint

        This problem is *easy* level

        Simple SQL query with SELECT, WHERE and ORDER... DESC.

    * MySQL Query

        ```sql
            SELECT id, movie, description, rating FROM cinema
                WHERE (id%2 <> 0 AND description != 'boring')
                ORDER BY rating DESC
        ```

* **[Trim a Binary Tree - 669](https://leetcode.com/problems/trim-a-binary-search-tree/description/)**

    * Hint

        This problem is *easy* level

        This problem tess the understanding of binary tree

        The binary tree is ordered, leaf less than the node is in left.

        Otherwise, it goes right.

    * Analysis

        * O(log(2)) time complexity
        * O(1) space complexity
* **[Set Matrix Zeros - 73](https://leetcode.com/problems/set-matrix-zeroes/description/)**

    * Hint

        This problem is *medium* level

        It tests the understanding of matrix operations

        Instead of storing the zeroes' locations, we can directly modified the matrix

    * Analysis
        * O(MN) time complexity
        * O(1)  space complexity
        
* **[Reshape the Matrix - 566](https://leetcode.com/problems/reshape-the-matrix/description/)**
    
    * Hint
        
        This problem is *easy* level
        
        It tests the understanding of matrix operations and usage of numpy
        
    * Analysis
    
        * O(Row*Col) time complexity
        * O(Row*Col) space complexity
        
* **[Find Peak Element - 162](https://leetcode.com/problems/find-peak-element/description/)**
    
    * Hint
    
       This problem is *medium* level
       
       It test the understanding of binary search and the situation analysis
       
       Start with the best case
       
       Move forward to a normal case
       
       Then, end with a worst case to test the algorithm
       
       Consider end situations
       
       Understand the problem and 
       
    * Analysis
    
        * O(log(n)) time complexity
        * O(1) space complexity

*   **[Evaluate Reverse Polish Notation - 150](https://leetcode.com/problems/evaluate-reverse-polish-notation/description/)**
        
    * Hint
    
        This problem is *medium* level
        
        It tests the understanding of [reverse Polish Notation](https://en.wikipedia.org/wiki/Reverse_Polish_notation)
        
        There are two ways to solve this problem
            
        * Recursive
        * Stack
        
        Similar Problems: *infix notation* and *prefix notation*
    
    * Analysis
    
        * O(n) time complexity
        * O(n) space complexity
        
    * New Python Function
    
        ```python
           lambda x: lambda y: int(float(x) / float(y))
           range(m, n) # return m to n-1

        ```
        
*   **[Second Highest Salary - 176](https://leetcode.com/problems/second-highest-salary/discuss/)**

    * Hint
        
        This problem is *easy* level
        
        It implements **desc limit offset** to order the table and select the second highest value
         
*   **[Maxium Average Subarray - 643](https://leetcode.com/problems/maximum-average-subarray-i/description/)**    
     
    * hint
        
        * This is a *easy* level problem 
        * Can be solved with **brute force approach** or **[Window Sliding Algorithm](http://www.geeksforgeeks.org/window-sliding-technique/)** 
    
    * Analysis
    
        * O(n) time complexity for window Sliding Algorithm
        * O(Nk) time complexity for the Brute force approach
        
    * Python Note
        * **Get a sublist from a list with nums[m:n] (nums[m] is inclusive, nums[n] does not return)**
        * python negative infinity number **float("-inf")** postive infinity number **float("inf")**
        
    
        





     