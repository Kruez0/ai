NP-complete:

How I understand, 
youtube: https://www.youtube.com/watch?v=e2cF8a5aAhE&t=1576s&ab_channel=AbdulBari

Np-complete is a problem where it is non deterministic and polynomial. non-deterministic meaning that it will be reseaarched more by people in the future because now it is still undetermined on how to do the code. polynomial time meaning that the problem was exponential time (2^n) and to make it easier and faster to solve effectively, we want to change it from exponential to polynomial time. Some of the NP-complete problem examples are knapsack, tsp etc.

Fractional Knapsack Problem:

How I understand, youtube: https://www.youtube.com/watch?v=m1p-eWxrt6g&ab_channel=GeeksforGeeks

A problem where there will be many items each item have different weights and values. This problem would like to know the most optimized way to maximize the value but also ensuring that the weight does not exceed the max weight limit.

The difference of Fractional Knapsack Problem to Regular Knapsack Problem is that with fractional knapsack we can take for example only 2/3 of an item. so for example i had a 60 kg item with a value of 120 and the max weight i can put is 50kg. with fractional we can take 50g of that item so 5/6. This is fractional Knapsack problem.

To do  this fractional Knapsack problem. I use a greedy method. These are the things I tried doing:
1. First make 3 items with different items and different values
2. make the maximum weight limit
3. calculate the ratio (value/weight) for each item
4. sort the items based on ratio
5. take the highest ratio and add them until we can't add the next item as a whole
6. add the next item as much fraction as we can.