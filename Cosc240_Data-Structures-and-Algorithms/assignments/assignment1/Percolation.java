// Richard Flores 9/20/17 ; The purpose of this class is to be used in program 
// testing probability of percolation

import edu.princeton.cs.algs4.WeightedQuickUnionUF;
import edu.princeton.cs.algs4.StdOut;

public class Percolation {
	// variable to save the input from constructor; to keep track of grid dimensions
	private int N;
	// union find object used to keep track of connected nodes
	WeightedQuickUnionUF nodes;
	// union find object used to keep track of which states are filled
	WeightedQuickUnionUF fills;
	// bottom root under grid
	private int bottom = 0;
	// top root above grid
	private int top = 0;
	// create grid
	private boolean[][] grid;
	// number to keep track of open sites in grid
	private int open_sites = 0;
	
	// constructor, int input is the dimension for grid; the grid is 
	// initialized with all false by default; flase means closed, true means open;
	// also initialized the WeightedQuickUnionUF object for keeping track of nodes
	public Percolation(int n) {
		N = n;	
		grid = new boolean[N][N];
		// number of nodes used for WeightedQuickUnionUF constructor, plus 2 for the top and
		// bottom nodes
		int num_of_nodes = (N * N) + 2;
		// plus 1 because of the 0-indexing in WeightedQuickUnionUF
		bottom = (N * N) + 1;
		nodes = new WeightedQuickUnionUF(num_of_nodes);
		fills = new WeightedQuickUnionUF(num_of_nodes - 1);
		// unions the top to the top row, and bottom to bottom row
		int bottom_offset = ( (N - 1) * N ) + 1;
		for (int j = 0; j < N; j ++) {
			nodes.union(top, j + 1);
			fills.union(top, j + 1);
			nodes.union(bottom, bottom_offset + j);
		}
		if (n == 1)
			open_sites++;
	}
	// opens site of grid at row i (y) and and column j (x)
	public void open(int i, int j) {
		if (i >= N || i < 0)
			throw new java.lang.IndexOutOfBoundsException("row index " + i + " must be between 0 and " + (N - 1));
		if (j >= N || j < 0)
			throw new java.lang.IndexOutOfBoundsException("column index " + j + " must be between 0 and " + (N - 1));
		if (!isOpen(i, j)) {
			//StdOut.print("" + i + " ");
			//StdOut.println("" + j);
			grid[j][i] = true;
			open_sites ++;
			int node_position = to1D(i, j);
			// if site above is open, then union to current site; bounds checked
			if (i - 1 >= 0 && isOpen(i - 1, j)) {
				nodes.union(node_position, node_position - N);
				fills.union(node_position, node_position - N);
			}
			// if site under is open, then union to current site; bounds checked
			if (i + 1 < N && isOpen(i + 1, j)) {
				nodes.union(node_position, node_position + N);
				fills.union(node_position, node_position + N);
			}
			// if site at left is open, then union to current site; bounds checked
			if ((j - 1) >= 0 && isOpen(i, j - 1)) {
				nodes.union(node_position, node_position - 1);
				fills.union(node_position, node_position - 1);
			}
			// if site at right is open, then union to current site; bounds checked
			if ((j + 1) < N && isOpen(i, j + 1)) {
				nodes.union(node_position, node_position + 1);
				fills.union(node_position, node_position + 1);
			}
		}
	}
	// returns boolean at position i, j; works because true means open
	public boolean isOpen(int i, int j) {
		if (i >= N || i < 0)
			throw new java.lang.IndexOutOfBoundsException("row index " + i + " must be between 0 and " + (N - 1));
		if (j >= N || j < 0)
			throw new java.lang.IndexOutOfBoundsException("column index " + j + " must be between 0 and " + (N - 1));
		return grid[j][i];
	}
	// returns true if the section is open and if the the postion is connected 
	// to the top root
	public boolean isFull(int i, int j) {
		if (i >= N || i < 0)
			throw new java.lang.IndexOutOfBoundsException("row index " + i + " must be between 0 and " + (N - 1));
		if (j >= N || j < 0)
			throw new java.lang.IndexOutOfBoundsException("column index " + j + " must be between 0 and " + (N - 1));
		// to know which position of WeightedQuickUnionUF instance to check
		int node_position = to1D(i, j);
		if (isOpen(i, j) && fills.connected(top, node_position)) {
			return true;
		}
		return false;
	}
	// converts row index i (y) and column index j (x) into a 2d representation for the UF array
	private int to1D(int i, int j) {
		return (i * N) + (j + 1);
	}
	// returns number of open sites on grid
	public int numberOfOpenSites() {
		return open_sites;
	}
	// returns true if the bottom node's root is equal to the top root
	public boolean percolates() {
		return nodes.connected(top, bottom);
	}
	// to test methods; input an integer n for n-by-n grid
	public static void main(String args[]) {
		int n = Integer.parseInt(args[0]);
		// construct n-by-n grid for perculation
		Percolation test = new Percolation(n);
		StdOut.println("This system percolates: " + test.percolates());
		// print true/false version of grid; true = open, false = closed
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (j == n - 1)
					StdOut.println(test.isOpen(i, j));
				else
					StdOut.print("" + test.isOpen(i, j) + " ");
			}
		}
		// open a bunch of sites
		/*for (int i = 0; i < n; i++)
			test.open(i, 0);*/
		for (int k = 0; k < n; k++) {
			test.open(k, k);
			if (k != 0)
				test.open(k - 1, k);
		}
		// open some extra sites that may repeat; to test the counter of open sites
		test.open(0, 0); test.open(0, n - 1);
		StdOut.println("After changes are applied: ");
		// reprint new true/false version of grid
		for (int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (j == n - 1)
					StdOut.println(test.isOpen(i, j));
				else
					StdOut.print("" + test.isOpen(i, j) + " ");
			}
		}
		StdOut.println("Number of open sites: " + test.numberOfOpenSites());
		StdOut.println("This system percolates: " + test.percolates());
		//test.isOpen(n,-1); // use to test bounds
		
	}
}