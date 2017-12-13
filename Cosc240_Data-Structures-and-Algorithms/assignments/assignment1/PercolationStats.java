// Richard Flores 9/23/17 ; The purpose of this class is to be used in program 
// testing probability of percolation
import edu.princeton.cs.algs4.StdRandom;
import edu.princeton.cs.algs4.StdStats;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.Stopwatch;
//import Percolation;

public class PercolationStats {
	public Stopwatch fatherTime = new Stopwatch();
	private int T;
	public double[] perc_thresh_results;
	// constructor, performs t independent experimentd on n-by-n grid
	public PercolationStats(int n, int t) {
		//StdOut.println("" + n);
		if (t <= 0) 
			throw new java.lang.IllegalArgumentException("number of experiments " + t + " must be greater than 0");
		if (n <= 0)
			throw new java.lang.IllegalArgumentException("dimension size " + n + "must be greater than 0");
		T = t;
		perc_thresh_results = new double[T];
		for (int q = 0; q < t; q++) {
			Percolation perc_Grid = new Percolation(n);
			while (!perc_Grid.percolates()) {
				int i = StdRandom.uniform(n);
				//StdOut.print("" + i + " ");
				int j = StdRandom.uniform(n);
				//StdOut.println("" + j);
				perc_Grid.open(i, j);
			}
			// multiplied by 1. to make it a double
			perc_thresh_results[q] = (1. * perc_Grid.numberOfOpenSites()) / (n * n);
		}
	}
	// sample mean of percolation threshold
	public double mean() {
		return StdStats.mean(perc_thresh_results);
	}
	// sample standard deviation of percolation threshold
	public double stddev() {
		return StdStats.stddev(perc_thresh_results);
	}
	// low endpoint of 95% confidence interval
	public double confidenceLow() {
		return mean() - ( (1.96 * stddev()) / Math.sqrt(T) );
	}
	// high endpoint of 95% confidence interval
	public double confidenceHigh() {
		return mean() + ( (1.96 * stddev()) / Math.sqrt(T) );
	}
	// runs expirements with Percolation class; input integer n and integer T 
	// for n-by-n grid and T tests
	public static void main(String args[]) {
		PercolationStats test = new PercolationStats(Integer.parseInt(args[0]), Integer.parseInt(args[1]));
		double mean = test.mean(); double std_dev = test.stddev();
		double con_high = test.confidenceHigh(); double con_low = test.confidenceLow();
		double time = test.fatherTime.elapsedTime();
		StdOut.printf("mean()            =  %f\n", mean);
		StdOut.printf("stddev()          =  %f\n", std_dev);
		StdOut.printf("confidenceHigh()  =  %f\n", con_high);
		StdOut.printf("confidenceLow()   =  %f\n\n", con_low);
		StdOut.printf("Total time:          %f", time);
	}
}