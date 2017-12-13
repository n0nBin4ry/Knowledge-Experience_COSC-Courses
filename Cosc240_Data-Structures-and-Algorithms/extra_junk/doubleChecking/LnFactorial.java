// testing my answer to problem 20 in ch 1.1; works!
import edu.princeton.cs.algs4.StdOut;

public class LnFactorial {
	public static double lnFact(int in) {
		if (in == 1) {return 0;} // log of 1 is zero; base-case
		else {return Math.log(in) + lnFact(in - 1);}
	} // basically used property of logs to change a log of factorial into the sum of the logs of all integers from 1 to N (or in)
	public static void main(String[] args) {
		double out = lnFact( Integer.parseInt(args[0]) );
		StdOut.print(out);
	}
}