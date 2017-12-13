/******************************************************************************
 *  Name:     Richard Flores
 *
 *  Hours to complete assignment (optional): N/A
 *
 ******************************************************************************/

Programming Assignment 4: Eight Puzzle


/******************************************************************************
 *  Explain briefly how you implemented the Board data type.
 *****************************************************************************/

I had two constructors, one that took in a 2D array and another than took in a
1D array. They were basically the same except that the one that took a 2D array
turned it into a 1D array.

In these constructors, I cached the manhattan distance, position of 
the zero_tile in the 1D demiension (while also caching the 2D components), string
representation, if the board was the goal, and if the board was solvable.

To get the neighbors I created a bag of Boards and created all possible Boards
to add to it using the row and column components of the position of the empty tile.


/******************************************************************************
 *  Explain briefly how you represented a search node
 *  (board + number of moves + previous search node).
 *****************************************************************************/

 I created an encapsulated class in the Solver class named "SearchNode." It had
 a value for the moves, reference for the previous SearchNode, and a reference of
 its current Board.
 
 The intial SearchNode had it's board be the initial board and had its reference
 to the previous SearchNode be null. It also had it's moves set to 0. Then 
 when obtaining the appropriate neighbors of it's board, we put them in a new
 SearchNode constructor along with the number of moves + 1 and the current 
 SearchNode as their reference to their previous SearchNode.

/******************************************************************************
 *  Explain briefly how you detected unsolvable puzzles.
 *
 *  What is the order of growth of the running time of your isSolvable()
 *  method as function of the board size n? Recall that with order-of-growth
 *  notation, you should discard leading coefficients and lower-order terms,
 *  e.g., n log n or n^3.

 *****************************************************************************/

Description:

I just cycled through the 1D array representation of the board with a double-
loop. The outer loop started at the second tile and the second always started
at the first tile and went through all the tiles before the current tile of the
outer loop. As the inner loop went along, 

Order of growth of running time:



/******************************************************************************
 *  For each of the following instances, give the minimum number of moves to
 *  solve the instance (as reported by your program). Also, give the amount
 *  of time your program takes with both the Hamming and Manhattan priority
 *  functions. If your program can't solve the instance in a reasonable
 *  amount of time (say, 5 minutes) or memory, indicate that instead. Note
 *  that your program may be able to solve puzzle[xx].txt even if it can't
 *  solve puzzle[yy].txt even if xx > yy.
 *****************************************************************************/


                 min number          seconds
     instance     of moves     Hamming     Manhattan
   ------------  ----------   ----------   ----------
   puzzle28.txt   NA			NA			NA
   puzzle30.txt   NA			NA			NA
   puzzle32.txt   NA			NA			NA
   puzzle34.txt   NA			NA			NA
   puzzle36.txt   NA (11?)		NA			NA
   puzzle38.txt   NA (11?)		NA			NA
   puzzle40.txt   NA (12?)		NA			NA
   puzzle42.txt   NA (11?)		NA			NA



/******************************************************************************
 *  If you wanted to solve random 4-by-4 or 5-by-5 puzzles, which
 *  would you prefer: a faster computer (say, 2x as fast), more memory
 *  (say 2x as much), a better priority queue (say, 2x as fast),
 *  or a better priority function (say, one on the order of improvement
 *  from Hamming to Manhattan)? Why?
 *****************************************************************************/

 I would prefer twice as much speed. I say this because whenever my program 
 crashes I most likely got this message: "java.lang.OutOfMemoryError: GC 
 overhead limit exceeded"
 
 At first glance it seemed like more memory would be my answer but when looking
 more into it I found out the reason that error gets thrown is because the 
 Garbage collector is taking up more than 98% of the CPU time. Maybe I'm still 
 mistaken but the problem there is that the the CPU can't process the all the 
 garbage collecting whenever we discard a SearchNode from the MinPQ while still
 needing CPU to do the rest of the work.

/******************************************************************************
 *  Known bugs / limitations.
 *****************************************************************************/

Only works up to puzzle3x3-13.

/******************************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings, lectures, and precepts, but do
 *  include any help from people and attribute them by name.
 *****************************************************************************/

 Asking you, my professor, questions. Which I hope I did more of this assignment,
 its just lately there hasn't been a good time because of school and other 
 problems.
 
 I also looked online to find out what my "java.lang.OutOfMemoryError: GC 
 overhead limit exceeded" problem was about.

/******************************************************************************
 *  Describe any serious problems you encountered.                    
 *****************************************************************************/

 The problem is that my whole program seems to suck. I can only solve simple
 puzzles up to puzzle3x3-13.txt. I didn't even need to copy-and-paste that 
 because I'm so used to using that (and the next puzzles) to test my iterations
 that always seem to cap off there or even lower. I think it all steps from the
 Garbage Collector the most because most of my errors came from there. But I 
 also got other errors revolving around just having to many neighboring boards
 in the MinQ even though I never added any that equal the previous board. I even
 once did a version whereevery time I added Boards to the MinPQ I even iterated
 through the MinPQ to make sure I didn't add and that were already in there (as
 you can tell I was getting desperate). It worked but was so extremely slow; it 
 was taking hours to process puzzle3x3-14. It never got an error but also never
 finished (I killed it after waiting a ton of hours).

/******************************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 *****************************************************************************/

 I am so sorrry about how dang late this is Professor. I had it finished on time
 without bugs but it was able to run even less puzzles than it can now. I felt like
 I was going a little crazy trying to make it better. I've tried so many things
 that caused me to completely start over once while other times I had to rework
 a ton of methods and also work out all the bugs that came along with that.
 
 The program still isn't anywhere near where I want it to be but I am turning it in
 now because 1. I don't want to expend any more late days and 2. I just have no idea
 where to go from here... I hope it's just one small thing I keep missing everytime I
 iterate over the program but I don't think so. I'm looking forward to seeing
 how I could improve this.
 
 Update: I couldn't help myself from trying again because I really hate the idea of
 turning in something so bad... though I will have to. But I found a problem in my
 manhattan distance function and after fixing it the solver can solve puzzles past
 puzzle3x3-14 really quickly... But even then it wasn't even to solve any of then 
 puzzles in the readme with either manhattan-priority or hamming-priority.
 