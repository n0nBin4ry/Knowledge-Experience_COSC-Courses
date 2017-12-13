/******************************************************************************
 *  Name:     Richard Flores
 *
 *  Hours to complete assignment (optional): N/A
 *
 ******************************************************************************/

Programming Assignment 3: Autocomplete


/******************************************************************************
 *  Describe how your firstIndexOf() method in BinarySearchDeluxe.java
 *  finds the first index of a key that equals the search key.
 *****************************************************************************/

 I basically run binary search on the array of Terms using the byPrefix 
 comparator and a key Term that is the prefix. If the search doesn't find 
 anything with the given prefix then it returns -1. But if it does find a Term 
 with the prefix then the method checks the Term to to left of index that the 
 Term is at. the method keeps comparing to the left until there is a Term that 
 isn't equal to the key according to the byPrefix comparator. Then it returns 
 the index of the last index that did match the key.

/******************************************************************************
 *  Identify which sorting algorithm (if any) that your program uses in the
 *  Autocomplete constructor and instance methods. Choose from the following
 *  options:
 *
 *    none, selection sort, insertion sort, mergesort, quicksort, heapsort
 *
 *  If you are using an optimized implementation, such as Arrays.sort(),
 *  select the principal algorithm.
 *****************************************************************************/

Autocomplete() : none

allMatches() : Dual-Pivot Quicksort

numberOfMatches() : Dual-Pivot Quicksort

/******************************************************************************
 *  What is the order of growth of the number of compares (in the worst case)
 *  that each of the operations in the Autocomplete data type make, as a
 *  function of the number of terms n and the number of matching terms m?
 *
 *  Recall that with order-of-growth notation, you should discard
 *  leading coefficients and lower-order terms, e.g., m^2 + m log n.
 *****************************************************************************/

Autocomplete(): 	O(n)

allMatches():		O(n log n)

numberOfMatches(): 	O(m log m + n log n)




/******************************************************************************
 *  Known bugs / limitations.
 *****************************************************************************/

 N/A
 
/******************************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings and lectures, but do
 *  include any help from people and attribute them by name.
 *
 *  Also include any resources (including the web) that you may
 *  may have used in creating your design.
 *****************************************************************************/

 N/A

/******************************************************************************
 *  Describe any serious problems you encountered.                    
 *****************************************************************************/


 N/A


/******************************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 *****************************************************************************/

 Was fun! Really enjoyed figuring out something many applications use in some 
 way. Made me want to get into some GUI stuff to see how I could make maybe a
 search (with autocomplete and such) GUI in the future. Maybe once there's more
 time.
