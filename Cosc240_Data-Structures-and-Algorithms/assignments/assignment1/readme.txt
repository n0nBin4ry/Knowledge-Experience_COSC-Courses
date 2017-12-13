/******************************************************************************
 *  Name: Richard Flores
 *
 *  Operating system: Windows 10
 *  Compiler version: (do "javac -version" at a command prompt to find out)
 *  Text editor / IDE: Notepad++
 *
 *  Hours to complete assignment (optional): lost track..
 *
 ******************************************************************************/

Programming Assignment 1: Percolation


/******************************************************************************
 *  Describe how you implemented Percolation.java. How did you check
 *  whether the system percolates?
 *****************************************************************************/

 In the constructor method I made 2 private instances of a union-find object:
 one to keep track of perculation, and one to keep track of if a section is
 filled. I also made a 2D array to keep track of opened and closed sections for
 use by the 2 union-find instances. The methods basically used these 3 data
 structures to carry out their operations. Besides numberOfOpenSites() which
 just used a private instance variable that incremented every time a new site
 was opened. I also used an extra private methode to1D(int i, int j) to take 
 the row and column indexes and return a 1D representation for the union-find
 instances to use. 
 Anyways, the way I checked for perculation was by me checking the site in the 
 union-find object in charge of percolation and seeing if the site is connected
 to the top node.
 
/******************************************************************************
 *  Perform computational experiments to estimate the running time of
 *  PercolationStats.java for values values of n and T when implementing
 *  Percolation.java with QuickFindUF.java.
 *
 *  To do so, fill in the two tables below. Each table must have at least
 *  4 data points, ranging in time from around 0.1 seconds to around
 *  60 seconds. Do not include data points that takes less than 0.1 seconds.
 *****************************************************************************/

(T = 50)

 n          time (seconds)
------------------------------
45			0.118000
90			1.890000
180			32.262000
360			842.084000
720			7119.029000


(n = 20)

 T          time (seconds)
------------------------------
600			0.109000
1200		0.179000
2400		0.334000
4800		0.669000
9600		1.277000


/******************************************************************************
 *  Using the empirical data from the above two tables, give a formula 
 *  (using tilde notation) for the running time (in seconds) of
 *  PercolationStats.java as function of both n and T, such as
 *
 *       ~ 5.3*10^-8 * n^5.0 * T^1.5
 *
 *  Recall that with tilde notation, you include both the coefficient
 *  and exponents of the leading term (but not lower-order terms).
 *  Round each coefficient to two significant digits.
 *
 *****************************************************************************/

running time (in seconds) as a function of n and T:  ~ 5.53*10^-10 * n^4.1 * T^0.90


/******************************************************************************
 *  Repeat the previous two questions, but using WeightedQuickUnionUF
 *  (instead of QuickFindUF).
 *****************************************************************************/

(T = 50)

 n         time (seconds)
------------------------------
125			0.111000
250			0.343000
500			1.713000
1000		12.218000
2000		69.871000


(n = 20)

 T          time (seconds)
------------------------------
1500		0.103000
3000		0.161000
6000		0.268000
12000		0.455000
24000		0.784000


running time (in seconds) as a function of n and T:  ~ 1.62*10^-7 * n^2.4 * T^0.74


/**********************************************************************
 *  How much memory (in bytes) does a Percolation object (which uses
 *  WeightedQuickUnionUF.java) use to store an n-by-n grid? Use the
 *  64-bit memory cost model from Section 1.4 of the textbook and use
 *  tilde notation to simplify your answer. Briefly justify your
 *  answers.
 *
 *  Include the memory for all referenced objects (deep memory).
 **********************************************************************/

 memory: (n^2 + 80n + 192) bytes ~ n^2 bytes
 
 My percolation object has 4 integer instance variables, 1 n-by-n boolean grid,
 and 2 WeightedQuickUnionUF objects. The integer variables end up being 16 bytes
 altogether, the boolean grid is (n^2 + 32n + 24) bytes, and then two reference 
 variables (the size of machine words) for the WeightedQuickUnionUF objects add
 up to 16 bytes.
 And then each one of those objects WeightedQuickUnionUF objects have (24n + 60)
 bytes becuase they include 1 integer instance variables and 2 int arrays. We 
 have 2 of them so they add up to (48n + 120) bytes.
 If we add up everything we should get (n^2 + 80n + 192) bytes altogether. Which
 simplifies to n^2 bytes in tilde notation.

/******************************************************************************
 *  Known bugs / limitations.
 *****************************************************************************/

 N/A

/******************************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include course readings and lectures, and precepts, but do
 *  include any help from people and attribute them by name.
 *****************************************************************************/

 Help from my professor Dr. Lutgen with my backwash problem. Bounced wrong 
 ideas off of him until we came to the idea of another Union-Find object to
 keep track of isFull(). Thought I still feel there is a way without another
 union-find object but still get a stack overflow. One day.. But right now it
 works as correctly anyways.

/******************************************************************************
 *  Describe any serious problems you encountered.                    
 *****************************************************************************/

 The most serious problem was the backwash problem. Also my first implementtion
 had i be the column index and j be the row index because I was just used to it 
 being like that but I eventually figured out my error with the visualizer and 
 fixed it.

/******************************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 *****************************************************************************/

 I already knew I liked just building/making things through Computer Science, 
 but I also enjoyed researching the speed and processing with experiments. Felt
 pretty cool. The only thing was that I really got mixed up with the API saying
 that row index was i and column index was j. Especially since the row column 
 had to be the first argument in all the methods. But that was only a small 
 thing.