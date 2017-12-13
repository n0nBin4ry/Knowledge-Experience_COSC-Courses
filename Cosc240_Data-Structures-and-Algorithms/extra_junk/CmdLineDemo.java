import edu.princeton.cs.algs4.StdOut;

class CmdLineDemo {
	// sum command-line args (assume doubles); on cmd line you type in the java file name followed by arguments you want to add
	public static void main(String[] args) {
		double sum = 0.0; 
		for (int i = 0; i < args.length; i++) { // takes in all arguments in command line, uses args array, arrays have a built in value of its length (super cool)
			sum += Double.parseDouble(args[i]);
		}
		StdOut.println(sum);
	}
}