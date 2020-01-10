# Lottery simulator
 A Simple python simulator to replicate the lottery

This simulator replicates the act of playing the lottery. Where the user chooses 6 given numbers (1-60) and then specifies how many weeks they wish to play for. The computer then generates 6 random numbers. Which are then compared to the users chosen numbers. Dependent on the number of matches that week, the amount won is then printed. The Program also includes a running total, profit and optional ticket cost. 

Version 1.1
-----
Modified the random number generator to ensure the numbers generated are independent of each other
i.e. 20,4,5,46,34,1  ✓
     20,20,3,35,25,2 X
