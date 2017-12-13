// testing out problem 14 from ch 1.1; works!
import edu.princeton.cs.algs4.StdOut;

public class Log2 {
	public static int lg(int in) {
		if (in == 1) {return 0;} // base case
		else {return lg( in/2 ) + 1;} // once lg reaches 1, it conts all the recursive loops, not counting final, to get log 2 int smaller than OG in; made easier thanks to int division
	}
	public static void main(String[] args) {
		int out = lg( Integer.parseInt(args[0]) );
		StdOut.print(out);
	}
}