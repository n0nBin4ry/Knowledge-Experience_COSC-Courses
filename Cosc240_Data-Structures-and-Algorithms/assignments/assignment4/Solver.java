import edu.princeton.cs.algs4.Bag;
import edu.princeton.cs.algs4.MinPQ;
import java.util.Comparator;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.Stack;
import edu.princeton.cs.algs4.In;
import edu.princeton.cs.algs4.StdOut;

public final class Solver {
	
	private final int min_moves;
	private Board[] solution_path;
	private final Stack<Board> trail = new Stack<Board>();
	
	// find a solution to the initial board (using the A* algorithm)
    public Solver(Board initial) {
		if (initial == null)
			throw new java.lang.IllegalArgumentException("Error: Solver must be given an intialized board.");
		if (!initial.isSolvable())
			throw new java.lang.IllegalArgumentException("Error: Solver must be given a solvable board.");
		
		// setting up initial search node at intial given board
		SearchNode root = new SearchNode(initial, null, 0);
		// create min priority queue and insert initial search node
		MinPQ<SearchNode> choices = new MinPQ<SearchNode>();
		choices.insert(root);
		
		// create a reference for whatever gets taken out of the minPQ each loop
		SearchNode check;
		while (true) {
			// take out Search node with min priority
			check = choices.delMin();
			//StdOut.println(check.moves);
			// if board of search node is the goal board, break
			if (check.curr.isGoal())
				break;
			// adds search nodes of all neighbors of check's Board, already 
			// excluding previous board already in constructor of SearchNode
			
			// IDEA: Just go ahead and search through minPQ to avoid getting
			//		 repeated boards... worth a try because everything is so
			//		 dang slow
			
			for (Board x : check.curr_neighbors) {
				/*boolean matches = false;
				for (SearchNode y : choices)
					if (x.equals(y.curr)) {
						matches = true;
						break; 
					}
				if (!matches)*/
					choices.insert(new SearchNode(x, check, check.moves + 1));
			}
		}
		
		// assign the minimum number of moves now that we found the goal board
		min_moves = check.moves;
		
		for (SearchNode n = check; n != null; n = n.prev)
			trail.push(n.curr);
	}
	
	// encapsulated class to keep track of the number of moves, non-repeated
	// neighbors, priority, and the previous Board
	private class SearchNode implements Comparable<SearchNode> {
		// current Board
		private final Board curr;
		// pevious SeachNode
		public final SearchNode prev;
		// amount of moves to get to initial board
		public final int moves;
		// manhattan priority of current board
		public final int priority;
		// Iterable of neighboring Boards, not including previous boards
		public Bag<Board> curr_neighbors = new Bag<Board>();
		
		public SearchNode(Board current, SearchNode previous, int moves) {
			curr = current;
			prev = previous;
			this.moves = moves;
			this.priority = moves + curr.manhattan();
			//this.priority = moves + curr.hamming();
			
			// search through the current Boards neighbors and add them to
			// iterable of neighboring boards, unless the board is the same as
			// the previous board
			Iterable<Board> poss_neighbors = curr.neighbors();
			if (prev == null)
				for (Board x : poss_neighbors)
					curr_neighbors.add(x);
			else
				for (Board x : poss_neighbors)
					if (!x.equals(prev))
						curr_neighbors.add(x);
		}
		
		// compare nodes by their current board's priority
		public int compareTo(Solver.SearchNode other) {
			int o_p = other.priority;
			if (priority < o_p)
				return -1;
			if (priority > o_p)
				return 1;
			return 0;
		}
		
	}
	
	// returns min number of moves to solve initial board
	public int moves() {
		return min_moves;
	}
	
	// returns iterable sequence of boards in a shortest solution
    public Iterable<Board> solution() {
		/*Queue<Board> out = new Queue<Board>();
		for (int i = 0; i <= min_moves; i++)
			out.enqueue(solution_path[i]);
		return out;*/
		return trail;
	}
	
	
	// test client 
    public static void main(String[] args) {
		In input = new In(args[0]);
		int t_len = input.readInt();
		int[][] tiles = new int[t_len][t_len];
		for (int j = 0; j < t_len; j++)
			for (int i = 0; i < t_len; i++)
				tiles[j][i] = input.readInt();
		Board init_board = new Board(tiles);
		Solver sherlock = new Solver(init_board);
		StdOut.println("Minimum Number of moves = " + sherlock.moves());
		Iterable<Board> answers = sherlock.solution();
		for (Board x : answers)
			StdOut.println(x);
	}
}