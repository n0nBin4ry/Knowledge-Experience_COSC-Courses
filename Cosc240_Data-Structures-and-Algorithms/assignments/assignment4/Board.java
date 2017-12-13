import edu.princeton.cs.algs4.Bag;
import edu.princeton.cs.algs4.StdOut;

public final class Board {
	
	// 1-d version of board, +1 to help with math
	private final int[] board;
	// length n of n-by-n tiles
	private final int t_len;
	// length of 1-d board representation of tiles
	private final int b_len;
	// position of empty tile in 1-d board, 1-indexed
	private int zero_pos;
	// row (j) and col (i) components of zero_pos, both 0-indexed
	private int zero_j;
	private int zero_i;
	// is the n size of n-by-n tiles even?
	private final boolean t_even;
	// number of inversions per board
	private final int inv;
	// is solvable?
	private final boolean solvable;
	// hamming distance
	//private final int hamming_dist;
	// manhattan distance
	private final int manhat_dist;
	// is goal board?
	private final boolean goal;
	// string representation of board
	private String string_rep;
	
	// create a board from an n-by-n array of tiles,
	public Board(int[][] tiles) {
		// assignm values to instance variables.
		t_len = tiles[0].length;
		b_len = t_len * t_len;
		
		// create and fill the 1-d representation of given tiles
		// and create string representation at same time!
		string_rep = "" + t_len + "\n";
		board = new int[b_len + 1];
		for (int j = 0; j < t_len; j++) {
			for (int i = 0; i < t_len; i++) {
				if (tiles[j][i] == 0) {
					// set zero pos and its components
					zero_pos = to1D(j, i);
					board[zero_pos] = 0;
					zero_i = i;
					zero_j = j;
				}
				else
					board[to1D(j, i)] = tiles[j][i];
				string_rep += " " + tiles[j][i];
			}
			string_rep += "\n";
		}
		
		// initialize all other private final values
		// is the n-length even or odd?
		if (t_len % 2 == 0)
			t_even = true;
		else
			t_even = false;
		
		// run all caching functions
		
		goal = isGoalCache();
		// count inversions
		inv = inversionCount();
		solvable = isSolvableCache();
		//hamming_dist = hammingCache();
		manhat_dist = manhattanCache();
	}
	
	public Board(int[] tiles/*, int t_len*/) {
		// assign values to instance variables
		b_len = tiles.length - 1;
		t_len = (int) Math.sqrt(b_len);
		//this.t_len = t_len;
		board = tiles;
		
		// search for zero tile and set components
		// and create string representation at same time!
		string_rep = "" + t_len + "\n";
		for (int n = 1; n <= b_len; n++) {
			if (board[n] == 0) {
				zero_pos = n;
				zero_i = (zero_pos - 1) % t_len;
				zero_j = (zero_pos - 1) / t_len;
			}
			string_rep += " " + board[n];
			if (n % t_len == 0)
				string_rep += "\n";
		}
		
		// initialize all other private final values
		// is the n-length even or odd?
		if (t_len % 2 == 0)
			t_even = true;
		else
			t_even = false;
		
		// run all caching functions
		
		goal = isGoalCache();
		// count inversions
		inv = inversionCount();
		solvable = isSolvableCache();
		//hamming_dist = hammingCache();
		manhat_dist = manhattanCache();
	}
	
	// functions for caching
	
	// number of tiles out of place
	private int hammingCache() {
		int out = 0;
		// cycle through board and see if tiles are in right pos
		// here we go from 1 to b_len - 1 because the last spot should be empty
		for (int n = 1; n < b_len; n++) {
			if (board[n] != n)
				out++;
		}
		return out;
	}
	
	// sum of Manhattan distances between tiles and goal
    private int manhattanCache() {
		int out = 0;
		for (int n = 1; n <= b_len; n++)
			if (board[n] != 0 && board[n] != n)
				out += manhattanHelper(board[n], n);
		return out;
	}
	
	// is this board the goal board?
	private boolean isGoalCache() {
		for (int n = 1; n < b_len; n++)
			if (board[n] != n)
				return false;
		return true;
	}
	
	// is this board solvable?
    private boolean isSolvableCache() {
		if (goal)
			return true;
		if (t_even)
			return isSolv_evenSize();
		return isSolv_oddSize();
	}
	
	
	
	// returns index of grid indices in a 1D integer representation
	// the grid indeces are 0-indexed, but the returned index is 1-indexed
	private int to1D(int j, int i) {
		return (j * t_len) + i + 1;
	}
	
	// string representation of this board
	// where tiles[row][col] = tile at (row, col)
    public String toString() {
		return string_rep;
	}
	
	// tile at (row, col) or 0 if blank
    public int tileAt(int row, int col) {
		return board[to1D(row, col)];
	}
	
	// board size n
    public int size() {
		return t_len;
	}
	
	// number of tiles out of place
    public int hamming() {
		return hammingCache();
		//return hamming_dist;
	}
	
	// sum of Manhattan distances between tiles and goal
    public int manhattan() {
		return manhat_dist;
		//return manhattanCache();
	}
	
	// finds manhatten distance between given tile and the correct position of
	// tile
	private int manhattanHelper(int given, int correct) {
		int given_i = given % t_len;
		int given_j = given / t_len;
		int correct_i = correct % t_len;
		int correct_j = correct / t_len;
		return Math.abs(given_i - correct_i) + Math.abs(correct_j - given_j);
	}
	
	// is this board the goal board?
    public boolean isGoal() {
		return goal;
	}
	
	// does this board equal y?
    public boolean equals(Object y) {;
		// same instance?
		if (this == y)
			return true;
		// same object class?
		if (y.getClass() != this.getClass())
			return false;
		// same tile positions?
		Board yy = (Board) y;
		if (string_rep.compareTo(yy.string_rep) == 0)
			return true;
		return false;
	}
	
	// all neighboring boards
    public Iterable<Board> neighbors() {
		// iterable to return
		// NOTE: maybe do Bag for slightly more efficient memory usage, though
		//		 double check if it is better on memory
		Bag out = new Bag<Board>();
		// add all possible neighbors to board
		// right?
		if (zero_i + 1 < t_len)
			out.add(shiftZeroTile(0));
		// up?
		if (zero_j - 1 >= 0)
			out.add(shiftZeroTile(1));
		// left?
		if (zero_i - 1 >= 0)
			out.add(shiftZeroTile(2));
		// down?
		if (zero_j + 1 < t_len)
			out.add(shiftZeroTile(3));
		return out;
	}
	
	// returns a copy of current board where the zero_tile is switched with the
	// tile adjacent to it in the given direction
	// key for direction: 0 = right, 1 = up, 2 = left, 3 = down
	private Board shiftZeroTile(int dir) {
		Board out;
		// copy board array
		int[] board_copy = new int[b_len + 1];
		for (int n = 1; n <= b_len; n++)
			board_copy[n] = board[n];
		//swap w/right
		if (dir == 0) {
			int adj = to1D(zero_j, zero_i + 1);
			swap(board_copy, zero_pos, adj);
			out = new Board(board_copy/*, t_len*/);
			return out;
		}
		// swap w/top
		if (dir == 1) {
			int adj = to1D(zero_j - 1, zero_i);
			swap(board_copy, zero_pos, adj);
			out = new Board(board_copy/*, t_len*/);
			return out;
		}
		// swap with left
		if (dir == 2) {
			int adj = to1D(zero_j, zero_i - 1);
			swap(board_copy, zero_pos, adj);
			out = new Board(board_copy/*, t_len*/);
			return out;
		}
		// swap w/bottom
		int adj = to1D(zero_j + 1, zero_i);
		swap(board_copy, zero_pos, adj);
		out = new Board(board_copy/*, t_len*/);
		return out;
	}
	
	// swap two elements in given array at the given indeces
	private void swap(int[] a, int t1, int t2) {
		int a_t1 = a[t1];
		a[t1] = a[t2];
		a[t2] = a_t1;
	}

	// is this board solvable?
    public boolean isSolvable() {
		return solvable;
	}
	
	// to be used with isSolvable() when t_size is even
	private boolean isSolv_evenSize() {
		if ((inv + zero_j) % 2 != 0)
			return true;
		return false;
	}
	
	// to be used with isSolvable() when t_size is odd
	private boolean isSolv_oddSize() {
		if (inv % 2 == 0)
			return true;
		return false;
	}
	
	private int inversionCount() {
		// counter of inversions to be returned
		int out = 0;
		// for each tile, check all tiles before and see if any shouldn't be
		// before current tile
		for (int n = 2; n <= b_len; n++)
			if (n != zero_pos)
				for (int k = 1; k < n; k++)
					if (board[k] > board[n])
						out++;
		return out;
	}

	// unit testing (required)
    public static void main(String[] args) {
		// tiles
		int[][] tiles1 = {{1, 3, 7}, {0, 2, 5}, {6, 8, 4}}; // solvable
		int[] tiles2 = {0, 1, 2, 3, 4, 5, 6, 8, 7, 0}; // unsolvable
		// boards, testing constructors
		Board board1 = new Board(tiles1);
		Board board1_dup = new Board(tiles1);
		Board board2 = new Board(tiles2);
		// testing toString()
		StdOut.println("String representation of Board1 and Board2 respectively:");
		StdOut.println(board1);
		StdOut.println(board2 + "\n");
		// testing equals()
		StdOut.println("Board1 is equal to a duplicate of itself:");
		StdOut.println(board1.equals(board1_dup) + "\n");
		StdOut.println("Is equal to Board2:");
		StdOut.println(board1.equals(board2) + "\n");
		// testing isGoal()
		int[] tiles3 = {0, 1, 2, 3, 4, 5, 6, 7, 8, 0};
		Board goal = new Board(tiles3);
		StdOut.println(goal);
		StdOut.println("The above Board is the goal-board:");
		StdOut.println(goal.isGoal() + "\n");
		// testing hamming()
		StdOut.println("The hamming distance of Board1 should be 6. hamming() returns : " + board1.hamming() + "\n");
		// testing isSolvable()
		StdOut.println("Board1 should be solvable, and Board2 shouldn't be.");
		StdOut.println("Board1 is solvable: " + board1.isSolvable());
		StdOut.println("Board2 is solvable: " + board2.isSolvable());
		// testing neighbors()
		StdOut.println("These are all the possible neighbors to Board1:");
		Iterable<Board> neighbors1 = board1.neighbors();
		for (Board x : neighbors1) {
			StdOut.println(x);
		}
	}
}