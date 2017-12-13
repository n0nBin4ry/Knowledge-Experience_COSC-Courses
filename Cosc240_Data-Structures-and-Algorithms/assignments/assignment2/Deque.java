// Richard Flores 9/29/17
// class that makes a Deque using linked list that can also be iterated from
// front to end node
import java.util.Iterator;
import edu.princeton.cs.algs4.StdOut;

// "implements Iterable<Item>" states that class inherits Iterable type;
// ie: you can iterate over it
public class Deque<Item> implements Iterable<Item>{
	// subclass of nodes for linked list; behind points to pointer behind and 
	// infront points to pointer ahead; Item item points to generic object
	private class Node {
		Node behind;
		Node ahead;
		Item item;
		
		// argument of constructor is the item stored in node
		public Node(Item in) {
			item = in;
		}
	}
	
	// contructor of empty Deque, front will point to front object/node, end 
	// will point to end object/node in deque
	// list size
	private Node front;
	private Node end;
	private int list_size;
	
	public Deque() {
		list_size = 0;
	}
	
	// checks if deque is empty
	public boolean isEmpty() {
		if (list_size == 0)
			return true;
		return false;
	}
	
	// returns number of Items in Deque
	public int size() {
		return list_size;
	}
	
	// add item to front of deque
	public void addFront(Item item) {
		if (item == null)
			throw new java.lang.IllegalArgumentException("Item is null, needs to be instantiated");
		// if deque is empty then point both front and end towards the new item
		if (isEmpty()) {
			front =  new Node(item);
			end = front;
		}
		else {
			// store reference to node currently in front
			Node old_front = front;
			// assign new node to the front
			front = new Node(item);
			// have new front node point to previous front item through behind
			front.behind = old_front;
			// have previous front node point to new front item through ahead
			old_front.ahead = front;
		}
		// bookeeping for size
		list_size ++;
	}
	
	// add item to end of deque
	public void addEnd(Item item) {
		if (item == null)
			throw new java.lang.IllegalArgumentException("Item is null, needs to be instantiated");
		// if deque is empty then point both front and end towards the new node of item
		if (isEmpty()) {
			front =  new Node(item);
			end = front;
		}
		else {
			// store reference to noe currently at end
			Node old_end = end;
			// assign new node to end
			end = new Node(item);
			// have new end node point to previous end node through ahead var
			end.ahead = old_end;
			// have previous end node point to new end node through behind var
			old_end.behind = end;
		}
		// bookeeping for size
		list_size ++;
	}
	
	// remove item from front of deque
	public Item removeFront() {
		if (isEmpty())
			throw new java.util.NoSuchElementException("Cannot remove an item from an empty Deque");
		// store item from front node
		Item returned_item = front.item;
		// if there is no pointer behind then it is the only one in deque
		if (front.behind == null) {
			// remove solo node from front and end; causing it to loiter
			front = null;
			end = null;
		}
		else {
			// point front pointer towards new front node using behind var
			front = front.behind;
			// assign null to the ahead var of new front because nothing will be
			// of front
			front.ahead = null;
		}
		// bookeeping for size
		list_size --;
		// return stored item
		return returned_item;
	}
	
	// remove item from end of deque
	public Item removeEnd() {
		if (isEmpty())
			throw new java.util.NoSuchElementException("Cannot remove an item from an empty Deque");
		// store item from end node
		Item returned_item = end.item;
		// if there is no pointer ahead then it is the only one in deque
		if (front.behind == null) {
			// remove solo node from front and end; causing it to loiter
			front = null;
			end = null;
		}
		else {
			// point end pointer towards new end node using ahead var
			end = end.ahead;
			// assign null to the behind var of new end node because nothing will 
			// be behind the end
			end.behind = null;
		}
		// bookeeping for size
		list_size --;
		// return stored item
		return returned_item;
	}
	
	// iterate through deque from front to end
	public Iterator<Item> iterator() {
		// creates and uses new iterator
		return new LinkedListIterator();
	}
	
	// "implements Iterator<Item>" means that this class inherits the Iterator class;
	// ie: this class can iterate over a Iterable classes
	private class LinkedListIterator implements Iterator<Item> {
		// points node in front
		Node curr = front;
		
		// returns true if current node is not null
		public boolean hasNext() {
			return curr != null;
		}
		
		// return item in node that curr points to, then iterates to next node
		public Item next() {
			if (curr == null) {
				throw new java.util.NoSuchElementException("No more items to iterate over.");
			}
			// store item of current node
			Item returned_item = curr.item;
			// move to next node using bhind var because we are in front
			curr = curr.behind;
			// return stored item
			return returned_item;
		}
		
		public void remove() {
			throw new java.lang.UnsupportedOperationException("There is no remove method for iterator.");
		}
	}
	
	// test methods
	public static void main(String args[]) {
		Deque<Integer> test = new Deque<Integer>();
		StdOut.println("Deque created.\nDeque is empty: " + test.isEmpty() + "\nDeque size: " + test.size());
		test.addFront(0);
		for (int i = 1; i < 10; i ++) {
			test.addEnd(i);
		}
		StdOut.println("Deque populated.\nDeque is empty: " + test.isEmpty() + "\nDeque size: " + test.size());
		StdOut.println("Will now iterate through Deque from front (0) to end (9):");
		for (Integer x : test) {
			StdOut.println("" + x);
		}
		StdOut.println("Will now remove all items from Deque using removeEnd() then for last item, I'll use removeFront()\n");
		for (int i = 10; i > 1; i--) {
			StdOut.println("" + test.removeEnd());
		}
		StdOut.println("" + test.removeFront());
		StdOut.println("Deque is empty: " + test.isEmpty() + "\nDeque size: " + test.size() + "\n");
		// throwing out all exceptions
		try 
			{ test.addEnd(null); }
		catch (java.lang.IllegalArgumentException e)
			{ StdOut.println("IllegalArgumentException: " + e.getMessage()); }
		try 
			{ test.addFront(null); }
		catch (java.lang.IllegalArgumentException e)
			{ StdOut.println("IllegalArgumentException: " + e.getMessage()); }
		try 
			{ test.removeEnd(); }
		catch (java.util.NoSuchElementException e)
			{ StdOut.println("NoSuchElementException: " + e.getMessage()); }
		try 
			{ test.removeFront(); }
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