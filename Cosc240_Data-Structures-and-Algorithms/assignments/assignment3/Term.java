// Richard Flores 10/07/17
// Class Term holds a string and  int weight, can be compared with other Term 
// instances in lexicographic order of string or by reverse using the weight
import edu.princeton.cs.algs4.StdOut;
import java.util.Comparator;
import java.util.Arrays;

public class Term implements Comparable<Term> {
	
	private long weight = 0; 
	private String query = "";
	private int query_length;
	private int r;
	
	// Initializes a term with the given query string and weight.
    public Term(String query, long weight) {
		if (query == null)
			throw new java.lang.IllegalArgumentException("Error: Query is null, must be initialized with a String.");
		if (weight < 0)
			throw new java.lang.IllegalArgumentException("Error: Weight (" + weight + ") cannot be negative.");
		this.weight = weight; this.query = query;
		query_length = query.length();
	}
	
	// Compares the two terms in descending order by weight.
    public static class byReverseWeightOrder implements Comparator<Term> {
		public int compare(Term a, Term b) {
			long a_weight = a.weight; long b_weight = b.weight;
			// if a is less than (or greater than) return opposite result,
			// but if equal, just return that theyre equal
			if (a_weight < b_weight)
				return 1;
			if (a_weight > b_weight)
				return -1;
			return 0;
		}
	}
	
	// Compares the two terms in lexicographic order but using only the first r
	// characters of each query.
	public static class byPrefixOrder implements Comparator<Term> {
		
		// length of prefix
		private int r;
		
		// constructor
		public byPrefixOrder(int r_) {
			if (r_ < 0)
				throw new java.lang.IllegalArgumentException("Error: Prefix-size (" + r + ") cannot be negative.");
			r = r_;
		}
		
		public int compare(Term a, Term b) {
			// get prefix of each String of size r
			String a_query_pre; String b_query_pre;
			if (a.query.length() >= r)
				a_query_pre = a.query.substring(0, r);
			else
				a_query_pre = a.query;
			if (b.query.length() >= r)
				b_query_pre = b.query.substring(0, r);
			else
				b_query_pre = b.query;
			// compare substrings
			return a_query_pre.compareTo(b_query_pre);
		}
	}
	
	// Compares the two terms in lexicographic order by query.
    public int compareTo(Term that) {
		return query.compareTo(that.query);
	}
	
	// Returns a string representation of this term in the following format:
    // the weight, followed by a tab, followed by the query.
    public String toString() {
		return (weight + "\t" + query);
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
	
	// unit testing
    public static void main(String[] args) {
		Term[] starters = setStarters();
		printTerms(starters);
		StdOut.println("I will now sort array lexicographically by prefix 5.");
		Arrays.sort(starters, new Term.byPrefixOrder(5));
		printTerms(starters);
		StdOut.println("Next I will sort the array by reverse weight order.");
		Arrays.sort(starters, new Term.byReverseWeightOrder());
		printTerms(starters);
		
		// exceptions
		try
			{new Term(null, 0);}
		catch (java.lang.IllegalArgumentException e)
			{StdOut.println("IllegalArgumentException: " + e.getMessage());}
		try
			{new Term("", -1);}
		catch (java.lang.IllegalArgumentException e)
			{StdOut.println("IllegalArgumentException: " + e.getMessage());}
		try
			{new byPrefixOrder(-1);}
		catch (java.lang.IllegalArgumentException e)
			{StdOut.println("IllegalArgumentException: " + e.getMessage());}
	}
	
}