import edu.princeton.cs.algs4.StdOut;

class ArrayDemo {
	// reverse an array in place
	private void reverse(int[] a) {
		int n = a.length;
		for (int i = 0; i < n/2; i++){
			int t = a[i]; // saves data at point for swap
			a[i] = a[n - 1 - i]; // takes data at other index and assigns it to current index
			a[n - 1 - i] = t; // puts saved data from earlier into the other index
		}
	}
	private void show(int[] a) {
		// shows the inputted array
		for (int i = 1; i < a.length; i++){
		StdOut.print(a[i] + " ");
		}
		StdOut.println();
	}
}