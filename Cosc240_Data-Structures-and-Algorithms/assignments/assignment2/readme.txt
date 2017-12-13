/******************************************************************************
 *  Name:    Richard Flores
 *
 *  Hours to complete assignment (optional): N/A
 *
 ******************************************************************************/

Programming Assignment 2: Deques and Randomized Queues


/******************************************************************************
 *  Explain briefly how you implemented the deque and randomized queue.
 *  Which data structure did you choose (array, linked list, etc.) for each,
 *  and why?
 *****************************************************************************/

 For the Deque class I used a doubly linked-list because I had to be able to 
 add and remove items from both ends. And array wouldn't be able to handle that
 efficiently because the array would first have to resize, but also have to 
 shift over all items if someone wanted to add an item to the front.
 
 For the RandomizedQueue class I used an array because that was more efficient 
 for random dequeues, samples, and iterators. Sure the algorithm would have to 
 resize but if I went with a linked list I'd have to move from and end in 
 towards whatever index is chosen at random, and that can take linear time too
 often. Since I used an array I just needed to choose a random index and then
 return the item at that index. If I were doing a dequeue, I'd return the item 
 while moving the item at the end into the the current random index then shrink
 the array down by one since we moved the last item. ALso when I wanted to 
 iterate I'd just have to duplictate the array (only to where there ar items)
 and shuffle it.

/******************************************************************************
 *  How much memory (in bytes) do your data types use to store n items
 *  in the worst case? Use the 64-bit memory cost model from Section
 *  1.4 of the textbook and use tilde notation to simplify your answer.
 *  Briefly justify your answers and show your work.
 *
 *  Do not include the memory for the items themselves (as this
 *  memory is allocated by the client and depends on the item type)
 *  or for any iterators, but do include the memory for the references
 *  to the items (in the underlying array or linked list).
 *****************************************************************************/

Randomized Queue:  32 + 8n bytes   ~ 8n bytes 

Deque:             104 + 48n bytes ~  48n  bytes

RandomizedQueue:
- int queue_size = 4 bytes
- Item[] rand_q = 24(overhead) + 8n(reference for each Item) bytes
- total includes 4 more bytes for padding
Deque:
- int list_size = 4 bytes
- Node front and Node end = 2 * (16(overhead)  + (4 * 8)(extra overhead for 
	self reference, then reference to ahead, behind, and item)  ) = 96 bytes
- n item/nodes in Deque = n * (16 + (4 * 8)) = 48n bytes
- total includes 4 more bytes for padding

/******************************************************************************
 *  Known bugs / limitations.
 *****************************************************************************/

 N/A

/******************************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings and lectures, but do
 *  include any help from people and attribute them by name.
 *****************************************************************************/

 - Professor Lutgen: helped me with figuring out which data-structure to use for
	RandomizedQueue by letting me bounce off ideas with him
	
 - The other kid in class besides Julian (sorry I am blanking on his name):
	didn't help me directly but I did get some insight when I was helping him
	figure out why he kept getting a null sometimes when he dequeued his 
	RandomizedQueue; while explaining what I thought was his problem I realized
	the solution was a more efficiant was to queue and dequeue my RandomizedQueue

/******************************************************************************
 *  Describe any serious problems you encountered.                    
 *****************************************************************************/

 My serious problems came from implementing RandomizedQueue. It took a long 
 time to figure out just which data type would be best for it. I also had some
 trouble implementing how the queuing, dequeuing, and sampling would work 
 without shifting over all the items. I went through many different ideas. One
 included using my Deque class to keep track of all the positions where there
 were nulls in the array before the end index. Then whenever an Item was queued,
 it would be used to either fill a random one of those null indexes in Deque
 (from index stored at either the end or front of Deque) or just added to end
 if the null postions Deque was empty. But then when Dequing and sampling I had
 to make private methods that sifted through the array (to left or right 
 depending on random index) if the random index was pointing to a null and 
 other operations. Nontheless it was the idea I spent the most time on before I
 realized that maybe it wasn't efficient enough at times..

/******************************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether    
 *  you enjoyed doing it.                                             
 *****************************************************************************/

 Implementing the Deque class really affirmed my understanding of linked-lists,
 possibly better than when I was first taught about linked-lists.
 
 The overall assignment also solidified my understanding of iterators in Java,
 it also shed some light on object inheritance that was enlightening.
 
 In the FAQ yu said that some implementations of RandomizedQueue wouldn't needed
 to use StdRandom.shuffle() in the iterator. I am curious as to how that would 
 be implemented efficiently, I couldn't think of a way when trying to challenge
 myself.
 
 Oh and when writing the client I got it correct but couldn't understand why
 StdIn.getStrings() ignored the argument that was provided before the redirect
 of the file into the standard input and only got the strings from the file.
 
 Finally I am a bit doubtfull that I calculated the memory for the RandomizedQueue
 class because I wasn't sure how to account for the extra null space in the 
 array and how to figure out what the size of the array (including nulls) would
 be if it doubled every time it was full starting at a an overall size of 10.
 
 I will come in at office hours about the final three comments or just ask you
 after out next class period.
