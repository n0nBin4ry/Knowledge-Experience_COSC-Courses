// Richard Flores 10/10/17
// BinarySearchFancy is a collection of static methods that use binary sort and
// a comparator to find the left or right -most index that the key is in a 
// given array

import edu.princeton.cs.algs4.StdOut;
import java.util.Comparator;
import java.util.Arrays;

public class BinarySearchFancy {

    // Returns the index of the first key in a[] that equals the search key, or -1 if no such key.
    public static <Key> int firstIndexOf(Key[] a, Key key, Comparator<Key> comparator) {
		if (a == null || key == null || comparator == null)
			throw new java.lang.IllegalArgumentException("Error: None of your arguments can be null.");
		
		int a_length = a.length; int hi = a_length - 1; int lo = 0; int pivot = 0;
		// dir is set to negative 1 because we are looking for left-most index,
		// so if we need the direction to be negative to search to the left
		int dir = -1; 
		
		// while lo and hi borders don't pass each other
		while (lo <= hi) {
			// middle index between lo and hi
			pivot = lo + ((hi - lo) / 2);
			// if key is less than pivot point, shift left while dropping hi border
			if (comparator.compare(key, a[pivot]) < 0)
				hi = pivot - 1;
			// if key is greater than pivot point, shift right while increasing
			// lo border
			else if (comparator.compare(key, a[pivot]) > 0)
				lo = pivot + 1;
			// if t=its not greater or less than, then it's equal then break
			else
				break;
		}
		// if the loop broke because it cycled all the way through w/out key 
		// equalling anything, return -1
		if (comparator.compare(key, a[pivot]) != 0) 
			return -1;
		// now cycle to right to see if there are any duplicates of the pivot/key
		// more to the right than the current index
		while (pivot <= a_length - 2 && pivot >= 1 ) { // 1 index buffer on both ends
			if ( comparator.compare(a[pivot + dir] , a[pivot]) == 0 )
				pivot += dir;
			else
				break;
		}
		return pivot;
		//return siftThroughDupes(true, pivot, a, key, comparator);
	}

    // Returns the index of the last key in a[] that equals the search key, or -1 if no such key.
    public static <Key> int lastIndexOf(Key[] a, Key key, Comparator<Key> comparator) {
		if (a == null || key == null || comparator == null)
			throw new java.lang.IllegalArgumentException("Error: None of your arguments can be null.");
		int a_length = a.length; int hi = a_length - 1; int lo = 0; int pivot = 0; 
		// dir is set to positive 1 because we are looking for right-most index,
		// so if we need the direction to be positive to search to the right
		int dir = 1;
		
		// copy of the firstIndexOf() method
		while (lo <= hi) {
			pivot = lo + ((hi - lo) / 2);
			if (comparator.compare(key, a[pivot]) < 0)
				hi = pivot - 1;
			else if (comparator.compare(key, a[pivot]) > 0)
				lo = pivot + 1;
			else
				break;
		}
		if (comparator.compare(key, a[pivot]) != 0) 
			return -1;
		while (pivot <= a_length - 2 && pivot >= 1 ) {
			if ( comparator.compare(a[pivot + dir] , a[pivot]) == 0 )
				pivot += dir;
			else
				break;
		}
		return pivot;
	}
	
	// to help speed up unit test implementations
	private static void printTerms(Term[] terms) {
		int terms_l = terms.length;
		for (int i = 0; i < terms_l; i++)
			StdOut.println(terms[i]);
		StdOut.print("\n");
	}
	// to help keep testing clean
	private static Term[] setStarters() {
		Term[] starters = new Term[9];
		starters[0] = new Term("Bulbasaur",  1);
		starters[1] = new Term("Ivysaur",    2);
		starters[2] = new Term("Venasaur",   3);
		starters[3] = new Term("Charmander", 4);
		starters[4] = new Term("Charmeleon", 5);
		starters[5] = new Term("Charzard",   6);
		starters[6] = new Term("Squirtle",   7);
		starters[7] = new Term("Warturtle",  8); // putting 08 or 09 is "too big?"
		starters[8] = new Term("Blastoise",  9);
		return starters;
	}
	
    // unit testing (required)
    public static void main(String[] args) {
		Term[] starters = setStarters();
		Arrays.sort(starters, new Term.byPrefixOrder(4));
		StdOut.println("This is our starting array, already ordered in lexographical order of prefix length 4.");
		printTerms(starters);
		Term key = new Term("Char", 0);
		Term key3 = new Term("Pika", 0);
		int front = BinarySearchFancy.firstIndexOf(starters, key, new Term.byPrefixOrder(4));
		int end = BinarySearchFancy.lastIndexOf(starters, key, new Term.byPrefixOrder(4));
		StdOut.println("The sub-array of Terms starting with prefix 'char' starts at " + front + " and ends at " + end + ", inclusively.\n");
		front = BinarySearchFancy.firstIndexOf(starters, key3, new Term.byPrefixOrder(4));
		StdOut.println("The sub-array of Terms starting with prefix 'pika' starts at " + front + ". Meaning there is no such sub-array.\n");
		
		// exceptions
		try 
			{BinarySearchFancy.firstIndexOf(null, null, null);}
		catch (java.lang.IllegalArgumentException e)
			{StdOut.println("IllegalArgumentException: " + e.getMessage());}
			try 
			{BinarySearchFancy.lastIndexOf(null, null, null);}
		catch (java.lang.IllegalArgumentException e)
			{StdOut.println("IllegalArgumentException: " + e.getMessage());}
	}
}