// import appropriate classes, 1 for readin inputs and the other for displaying outputs.
import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Tabulate {
	public static void main(String[] args) {
		// creating variables
		int atBats = 0; int hits = 0; String name; short count = 0;
		// every 3 tokens, restart order until eof
		while (!StdIn.isEmpty()) {
			// first token of 3 is always a string
			if (count == 0) {
				name = StdIn.readString();
				count ++;
				// print name formatted correctly
				StdOut.printf("%-14s%s", name, " ");
			}
			else {
				// second number is always an int
				if (count == 1) {
					atBats = StdIn.readInt();
					count ++;
					StdOut.printf("%-3d%s", atBats, " ");
				}
				else {
					// third is also an int
					if (count == 2) {
						hits = StdIn.readInt();
						// print an extra number, is a float that is the hit rate of each batter
						StdOut.printf("%-3d %-4.3f\n", hits, (double) hits / atBats);
						// restart order
						count = 0;
					}
				}
			}
		}
	}  
}