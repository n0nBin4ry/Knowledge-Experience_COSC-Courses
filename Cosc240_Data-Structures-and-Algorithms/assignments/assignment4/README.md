# Assignment 4

Score: 84.00 / 100.00

## Files That Matter
- Board.java
- Solver.java

## Professor Notes

Good readme.txt. Correctly identifies unsolvable puzzles. Solves easy puzzles relatively quickly. However, as you observed in your readme.txt, your solver is very slow for puzzles above a certain complexity. I would have to spend more time investigating to find the precise problem, but it is clear that you are somehow adding too many Boards to your queue in the main loop of the A* algorithm. For example, with puzzle08.txt, printing the size of your queue after each iteration gives:
1
4
6
8
9
10
11
13
15
18
19
21
24
25
27
29
30
31
33
35
36
38
39
41
44
46
Done
For comparison, I did the same with my solution for the same puzzle:
1
4
5
5
5
6
6
7
9
10
Done