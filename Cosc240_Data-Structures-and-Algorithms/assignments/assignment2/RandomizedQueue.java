// Richard Flores 10/04/17
// This class is a Queue that takes in items and either pops or samples their
// items at random. Also iterates at a random order.

import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdOut;
import java.util.Iterator;


public class RandomizedQueue<Item> implements Iterable<Item> {
	
	// book-keeping, and also keeps track of end index of array which tells us
	// where to add next Item
	private int queue_size = 0;
	// array for Items
	private Item[] rand_q;
	
	// construct an empty randomized queue
	public RandomizedQueue() {
		// empty array starts at 10 indexes, initialized at all null
		rand_q = (Item[]) new Object[10];
	}
	
	// is the randomized queue empty?
	public boolean isEmpty() {
		if (queue_size == 0)
			return true;
		else
			return false;
	}
	
	// return the number of items on the randomized queue
	public int size() {
		return queue_size;
	}
	
	// add the item
	public void enqueue(Item item) {
		if (item == null)
			throw new java.lang.IllegalArgumentException("Item is null, needs to be instantiated");
		// add Item to end of array
		rand_q[queue_size++] = item;
		// if array fills up, resize by doubling
		if (queue_size == rand_q.length) {
			Item[] new_q = (Item[]) new Object[2 * queue_size];
			for (int i = 0; i < queue_size; i++) {
				new_q[i] = rand_q[i];
			}
			// point to new array, old array gets garbage-collected
			rand_q = new_q;
		}
	}
	
	// remove and return a random item
	public Item dequeue() { 
		if (queue_size <= 0)
			throw new java.util.NoSuchElementException("Cannot remove an item from an empty Queue.");
		// pick a random array index from [0, queue_size) 
		int rand_selection = StdRandom.uniform(queue_size);
		// store the item at rand_selection index to return later
		Item out = rand_q[rand_selection];
		// move the Item at end to replace item at rand_selection, then 
		// decriment queue_size so that the final item in array becomes ignored
		// and eventually overwritten
		rand_q[rand_selection] = rand_q[--queue_size];
		return out;
	}
	
	// return a random item (but do not remove it)
	public Item sample() {
		if (queue_size <= 0)
			throw new java.util.NoSuchElementException("Cannot sample an item from an empty Queue.");
		// pick a random array index from [0, queue_size) 
		int rand_selection = StdRandom.uniform(queue_size);
		// return item at random_selection index
		return rand_q[rand_selection];
	}
	
	// return an independent iterator over items in random order
	public Iterator<Item> iterator() {
		return new RandomizedQueueIterator();
	}
	
	// Iterator of class/object
	private class RandomizedQueueIterator implements Iterator<Item> {
		// index of iterator's position
		private int curr = 0;
		// empty array that we will put Queue's items into to randomly iterate
		private Item[] shuffle_arr;
		
		// constructor, fills shuffle_array and shuffles it
		RandomizedQueueIterator() {
			shuffle_arr = (Item[]) new Object[queue_size];
			for (int i = 0; i < queue_size; i++) {
				shuffle_arr[i] = rand_q[i];
			}
			StdRandom.shuffle(shuffle_arr);
		}
		
		// returns true if there is another Item ahead of Item at curr
		public boolean hasNext() {
			if (curr != queue_size)
				return true;
			else
				return false;
		}
		
		// returns next item ahead of Item at curr, then moves curr along by one
		public Item next() {
			if (curr == queue_size)
				throw new java.util.NoSuchElementException("No more items to iterate over.");
			return shuffle_arr[curr++];
		}
		
		// there is no remove method
		public void remove() {
			throw new java.lang.UnsupportedOperationException("There is no remove method for iterator.");
		}
	}
	
	// unit testing (required)
	public static void main(String[] args) {
		RandomizedQueue<Integer> test = new RandomizedQueue<Integer>();
		StdOut.println("RandomizedQueue created.\nRandomizedQueue is empty: " + test.isEmpty() + "\nQueue size: " + test.size());
		for (int i = 0; i < 12; i++)
			test.enqueue(i);
		StdOut.println("RandomizedQueue enqueued numbers [0, 11].\nRandomizedQueue is empty: " + test.isEmpty() + "\nQueue size: " + test.size() + "\n");
		StdOut.println("Will now sample RandomizedQueue 4 times");
		for (int i = 0; i < 4; i++)
			StdOut.println(test.sample());
		StdOut.println("Size will be the same as previously.\nQueue size: " + test.size() + "\n");
		StdOut.println("Will now iterate through RandomizedQueue without removing numbers.");
		for (Integer x : test)
			StdOut.println(x);
		StdOut.println("Size will be the same as previously.\nQueue size: " + test.size() + "\n");
		StdOut.println("Will now pop off all numbers at random.");
		for (int i = 12; i > 0; i--)
			StdOut.println("" + test.dequeue());
		StdOut.println("RandomizedQueue is empty: " + test.isEmpty() + "\nQueue size: " + test.size() + "\n");
		
		// throwing all exceptions
		try
			{ test.enqueue(null); }
		catch (java.lang.IllegalArgumentException e)
			{ StdOut.println("IllegalArgumentException: " + e.getMessage()); }
		try
			{ test.dequeue(); }
		catch (java.util.NoSuchElementException e)
			{ StdOut.println("NoSuchElementException: " + e.getMessage()); }
		try
			{ test.sample(); }
		catch (java.util.NoSuchElementException e)
			{ StdOut.println("NoSuchElementException: " + e.getMessage()); }
			
		Iterator<Integer> test_iterator = test.iterator();
		try
			{ test_iterator.next(); }
		catch (java.util.NoSuchElementException e)
			{ StdOut.println("NoSuchElementException: " + e.getMessage()); }
		try
			{ test_iterator.remove(); }
		catch (java.lang.UnsupportedOperationException e)
			{ StdOut.println("UnsupportedOperationException: " + e.getMessage()); }
	}
}