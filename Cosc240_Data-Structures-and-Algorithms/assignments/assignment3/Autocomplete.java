import java.util.Arrays;
import edu.princeton.cs.algs4.StdOut;

public final class Autocomplete {
	
	private final Term[] terms;
	
    // Initializes the data structure from the given array of terms.
    public Autocomplete(Term[] terms_) {
		if (terms_ == null)
			throw new java.lang.IllegalArgumentException("Error: The given array cannot be null.");
		int len  = terms_.length;
		for (int i = 0; i < len; i++)
			if (terms_[i] == null)
				throw new java.lang.IllegalArgumentException("Error: The elemtent at index " + i + " of given array is null.");
		terms = terms_;
	}

    // Returns all terms that start with the given prefix, in descending order 
	// of weight.
    public Term[] allMatches(String prefix) {
		if (prefix == null)
			throw new java.lang.IllegalArgumentException("Error: The given prefix string cannot be null.");
		// sort terms by given prefix
		int prefix_l = prefix.length();
		Arrays.sort(terms, new Term.byPrefixOrder(prefix_l));
		// vars to keep bounds of section with same prefix
		int front; int end;
		// create a key out of the prefix to use in BinarySearchFancy methods
		Term key = new Term(prefix, 0);
		front = BinarySearchFancy.firstIndexOf(terms, key, new Term.byPrefixOrder(prefix_l));
		end = BinarySearchFancy.lastIndexOf(terms, key, new Term.byPrefixOrder(prefix_l));
		// create new array that is just the interval of array terms from 
		// bounds [front, end]
		if (front == -1)
			return new Term[0];
		Term[] out = new Term[end - front + 1];
		for (int i = front; i <= end ; i++)
			out[i - front] = terms[i];
		// sort new array in reverse weight order then return
		Arrays.sort(out, new Term.byReverseWeightOrder());
		return out;
	}

    // Returns the number of terms that start with the given prefix.
    public int numberOfMatches(String prefix) {
		if (prefix == null)
			throw new java.lang.IllegalArgumentException("Error: The given prefix string cannot be null.");
		int prefix_l = prefix.length();
		Arrays.sort(terms, new Term.byPrefixOrder(prefix_l));
		int front; int end; 
		Term key = new Term(prefix, 0);
		front = BinarySearchFancy.firstIndexOf(terms, key, new Term.byPrefixOrder(prefix_l));
		end = BinarySearchFancy.lastIndexOf(terms, key, new Term.byPrefixOrder(prefix_l));
		// the implemention follows along with the implemention of allMatches
		// up until this point where instead we just return the difference of
		// the bounds, note that it is front + 1 because the end bound is inclusive
		if (front == -1)
			return 0;
		return (end + 1) - front ;
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
		Autocomplete test = new Autocomplete(starters);
		StdOut.println("This is the given array of Terms:");
		printTerms(starters);
		int n_matches = test.numberOfMatches("Char");
		Term[] matches = test.allMatches("Char");
		StdOut.println("There are " + n_matches + " Terms in given array that have the prefix 'Char'. Here they are in reverse order by weight:");
		printTerms(matches);
		
		// exceptions
		try
			{new Autocomplete(null);}
		catch (java.lang.IllegalArgumentException e)
			{StdOut.println("IllegalArgumentException: " + e.getMessage());}
		Term[] missingno = {new Term("Kangaskhan", 115), null};
		try
			{new Autocomplete(missingno);}
		catch (java.lang.IllegalArgumentException e)
			{StdOut.println("IllegalArgumentException: " + e.getMessage());}
		try
			{test.allMatches(null);}
		catch (java.lang.IllegalArgumentException e)
			{StdOut.println("IllegalArgumentException: " + e.getMessage());}
		try
			{test.numberOfMatches(null);}
		catch (java.lang.IllegalArgumentException e)
			{StdOut.println("IllegalArgumentException: " + e.getMessage());}
	}
}