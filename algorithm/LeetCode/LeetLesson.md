# LeetCode Lesson



* **[Judge Route Circle - 657](https://leetcode.com/problems/judge-route-circle/description/)**
    * Hint
        
        This problem is *entry* level. The key to solve this problem is to understand that 
        
        Moves to opposed  directions. If the robot is in its original position, 
        
        it should **have same amount of opposed moves** 
    
    * Analysis
        * O(n) run time. Linearly count moves in four directions
        * O(1) Memory. No extra space created
         
 
 
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
        * O(nlog(n)) run time.
        * O(1) Memory.

*   **[Distribute Candies - 575](https://leetcode.com/problems/distribute-candies/description/)**

    * Hint

        This problem is *easy* level.

        The sister only can get the half amount of candies so that the candies types she holds is less than that.

        If there is no enough candy types, she can only choose existing types of candies.

        Otherwise, her candies is not duplicated.

    * Analysis

        * O(n) run time because we need to count the list
        * O(1) memory. No other list needed

    * Python built-in functions

        ```python
           #get unique candy list
           set()
           #count list element
           len()
        ```

*   **[Swap Salary - 627](https://leetcode.com/problems/swap-salary/description/)**

    * Hit

        This problem is *easy* level.

        This is a simple SQL query.

        Be careful about requirements.

    * MySQL Query
        ```sql
            UPDATE salary a
                SET a.sex = ( CASE WHEN a.sex = 'f'
                              THEN 'm'
                              ELSE 'f'
                              END)
        ```




     