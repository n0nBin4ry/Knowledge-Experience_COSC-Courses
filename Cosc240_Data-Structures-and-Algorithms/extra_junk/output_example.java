// this is a source file to compile a class, you compile it by using command: javac <filename>
// error: saying this package doesnt exist even though it is in CLASSPATH environment variable
import edu.princeton.cs.algs4.StdOut;
// in java, classes are used not only for objects but also as a collection of just functions/methods; can use functions/ethods without instantiation
public class output_example { // has to be same name as file, minus the .java extension
	// if you are using the class to store functions then the function must be a static function; currently don't know why
	public static boolean isPrime(int n) {
		if (n < 2) {
			return false;
		}
		for (int d = 2; d * d <= n; d ++) {
			if (n % d == 0) {
				return false;
			}
		}
		return true;
	}
	// can have a main function like in c++, but has to be static void AND argument must always include a string array (usually named args)
	public static void main(String[] args){ 
		for (int i = 0; i <= 500; i++){
			if (isPrime(i)){
				StdOut.println(i);
			}
		}
	}
}
