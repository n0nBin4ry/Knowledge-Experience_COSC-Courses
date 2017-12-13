// Richard Flores 10/06/17
// This is a client to test out the RandomizedQueue class. It takes an argument
// k to stand forhow many Items from the standard input will be printed at
// random. Each Item from standard input will be printed at most once.

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class Permutation {
	
	public static void main(String[] args) {
		// takes first argument which states how many Items from file we will
		// choose
		int k = Integer.parseInt(args[0]);
		// create empty RandomizedQueue a
		RandomizedQueue<String> a = new RandomizedQueue<String>();
		// queue every string from standard input into a
		while (!StdIn.isEmpty()) {
			a.enqueue(StdIn.readString());
		}
		// dequeue k random strings from a
		int a_size = a.size();
		for (int i = 0; i < k; i++) {
			StdOut.println(a.dequeue());
		}
	}
}