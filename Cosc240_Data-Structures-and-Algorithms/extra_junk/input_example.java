import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

public class input_example {
	// sums double values from text file read into StdIn
	public static void main(String[] args) {
		double sum = 0.0;
		while(!StdIn.isEmpty()) {
			sum += Stdin.readDouble();
		}
		StdOut.printf("sum is: %.2f\n", sum);
	}
}