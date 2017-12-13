import edu.princeton.cs.algs4.Queue;


public final class Board {
	
	// n-by-n board
	private int[][] board;
	// n of n-by-n board
	private final int b_len;
	// keep position of the space w/out a tile in len-2 array: [row, col]
	private final int[] zero_tile = new int[2];
	
	// ASK: since it says that we assume the array is 2 or greater, ahould we do exceptiond?
	//		also since on subject, should we come up with our own corner cases we find neccesary?
	
	// create a board from an n-by-n array of tiles,
    // where tiles[row][col] = tile at (row, col)
    public Board(int[][] tiles) {
		board = tiles;
		b_len = board[0].length;
		for (int j = 0; j < b_len; j++) 
			for (int i = 0; i < b_len; i++)
				if (board[j][i] == 0) {
				zero_tile[0] = j;
				zero_tile[1] = i;
					break;
				}
	}
	
	// string representation of this board
    public String toString() {
		String out = "" + b_len + "\n";
		for (int j = 0; j < b_len; j ++) {
			for(int i = 0; i < b_len; i ++ )
				out += " " + board[j][i];
			out += "\n";
		}
		return out;
	}
	
	// tile at (row, col) or 0 if blank
    public int tileAt(int row, int col) {
		return board[row][col];
	}
	
    // board size n
	public int size() {
		return b_len;
	}
	
	// number of tiles out of place
    public int hamming() {
		int out = 0;
		int count = 1;
		for (int j = 0; j < b_len; j++)
			for (int i = 0; i < b_len; i++) {
				if (count++ != board[j][i])
					out++;
			}
		return out;
	}
	
	// sum of Manhattan distances between board and goal-board
    public int manhattan() {
		int out = 0;
		int count = 1;
		for (int j = 0; j < b_len - 1; j++)
			for (int i = 0; i < b_len; i++) {
				if (count++ != board[j][i]) {
					out += manhattanHelper(board[j][i], count);
				}
			}
		for (int i = 0; i < b_len - 1; i++)
			if (count++ != board[b_len - 1][i])
				out += manhattanHelper(board[b_len - 1][i], count);
		return out;
	}
	
	// returns the Manhattan distance between given tile at board indeces and
	//  be correct tile
	private int manhattanHelper(int given, int correct) {
		int given_i = given % b_len;
		int given_j = ((given - b_len) / b_len);
		int correct_i = correct % b_len;
		int correct_j = ((correct - b_len) / b_len);
		return Math.abs(given_i - correct_i) + Math.abs(correct_j - given_j);
		}
	
	// is this board the goal board?
    public boolean isGoal() {
		int count = 1;
		for (int j = 0; j < b_len - 1; j++)
			for (int i = 0; i < b_len; i++)
				if (board[j][i] != count++)
					return false;
		for (int i = 0; i < b_len - 1; i++)
			if (board[b_len][i] != count++)
				return false;
		if (board[b_len][b_len] != 0)
			return false;
		return true;
	}
	
	// ASK: how can I get accces to the board in object y?
	//		or chould I 
	// does this board equal y?
    public boolean equals(Object y) {
		// same instance?
		if (this == y)
			return true;
		// same object class?
		if (y.getClass() != this.getClass())
			return false;
		// same size?
		Board yy = (Board) y;
		if (b_len != yy.b_len)
			return false;
		//same tile positions?
		for (int j = 0; j < b_len; j++)
			for (int i = 0; i < b_len; i++)
				if (board[j][i] != yy.board[j][i])
					return false;
		return true;
	}
	
	// all neighboring boards
    public Iterable<Board> neighbors() {
		return boardNeighborQueue();
	}
	
	private Queue<Board> boardNeighborQueue() {
		/*boolean j_edge = false;
		boolean i_edge = false;
		int neigh_cnt = 0;
		if (zero_tile[0] == 0 || zero_tile[0] == b_len - 1)
			j_edge = true;
		if (zero_tile[1] == 0 || zero_tile[1] == b_len - 1)
			i_edge = true;
		if (i_edge && j_edge)
			neigh_cnt = 2;
		else if (i_edge ^ j_edge)
			neigh_cnt = 3;
		else
			neigh_cnt = 4;*/
		Queue<Board> out = new Queue<Board>();
		int zero_j = zero_tile[0];
		int zero_i = zero_tile[1];
		boolean check = false;
		// right
		try {
			if (board[zero_j][zero_i + 1] == 0)
				check = true;
		}
		catch (java.lang.IndexOutOfBoundsException e) {
			check = false;
		}
		if (check)
			out.enqueue(shiftTile(0));
		// up
		try {
			if (board[zero_j - 1][zero_i] == 0)
				check = true;
		}
		catch (java.lang.IndexOutOfBoundsException e) {
			check = false;
		}
		if (check)
			out.enqueue(shiftTile(1));
		// left
		try {
			if (board[zero_j][zero_i - 1] == 0)
				check = true;
		}
		catch (java.lang.IndexOutOfBoundsException e) {
			check = false;
		}
		if (check)
			out.enqueue(shiftTile(2));
		// down
		try {
			if (board[zero_j + 1][zero_i] == 0)
				check = true;
		}
		catch (java.lang.IndexOutOfBoundsException e) {
			check = false;
		}
		if (check)
			out.enqueue(shiftTile(3));
		return out;
	}
	
	// returns a new Board where the tile adjacent to the empty tile in the given
	// direction is shifted over to fill the empty tile; meaning the tile's old 
	// position is also now the position of the empty tile on the new Board
	// direction key: 0: right, 1: up, 2: left, 3: down
	private Board shiftTile(int dir) {
		// new grid to be stored in the returned Board
		int[][] new_board = board;
		// returned Board
		Board out;
		if (dir == 0) {
			// new Board will have old adjacent tile in the old zero-position
			new_board[zero_tile[0]][zero_tile[1]] = new_board[zero_tile[0]][zero_tile[1] + 1];
			// new Board will have an empty tile in old adjacent tile-positon
			new_board[zero_tile[0]][zero_tile[1] + 1] = 0;
			// return new Board
			out = new Board(new_board);
			return out;
		}
		else if (dir == 1) {
			new_board[zero_tile[0]][zero_tile[1]] = new_board[zero_tile[0] - 1][zero_tile[1]];
			new_board[zero_tile[0] - 1][zero_tile[1]] = 0;
			out = new Board(new_board);
			return out;
		}
		else if (dir == 2) {
			new_board[zero_tile[0]][zero_tile[1]] = new_board[zero_tile[0]][zero_tile[1] - 1];
			new_board[zero_tile[0]][zero_tile[1] - 1] = 0;
			out = new Board(new_board);
			return out;
		}
		else if (dir == 3) {
			new_board[zero_tile[0]][zero_tile[1]] = new_board[zero_tile[0] + 1][zero_tile[1]];
			new_board[zero_tile[0] + 1][zero_tile[1]] = 0;
			out = new Board(new_board);
			return out;
		}
		return null;
	}
	
	
    // is this board solvable?
	public boolean isSolvable() {
		return false;
	}

	// unit testing (required)
    public static void main(String[] args) {
		
	}
}