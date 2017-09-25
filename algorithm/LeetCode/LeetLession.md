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
        
        
    

     