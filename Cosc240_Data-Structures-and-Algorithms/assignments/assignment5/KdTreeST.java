// Richard Flores

import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.Queue;
import edu.princeton.cs.algs4.StdOut;

public class KdTreeST<Value> {
	private Node root = null;
	int size = 0;
	// construct an empty symbol table of points 
	public KdTreeST() {
		
	}
	
	// Subclass for building tree
	private class Node<Value> {
		// point/key of node
		private Point2D point;
		// value of node
		private Value val;
		// rectangle axis of point
		private RectHV rect;
		// ref to right child; greater in whichever set orientation of node
		private Node l_b;
		// ref to left child; lesser in whichever set orientation of node
		private Node r_t;
		// set orientation of node; set to true at first since root starts off
		// horizontally oriented
		private boolean horizontal = true;
		
		public Node(Point2D point, Value val, Node prev) {
			this.val = val;
			this.point = point;
			// if this isn't the root node, then set orientation based on parent
			if (prev != null)
				horizontal = !prev.horizontal;
			
			// create rectangle of axis point
			
			// if node is the root by not having a previous node, its rect is
			// the whole universe
			if (prev == null)
				rect = new RectHV(0, 0, 1, 1);
			// if this node is of horizontal orientation; ie: x-value determines
			// where its children go
			else if (horizontal) {
				// if this node is above parent
				if (this == prev.r_t) {
					rect = new RectHV(prev.rect.xmin(), prev.rect.ymax(), prev.rect.xmax(), 1);
				}
				// if this node is below parent
				else {
					rect = new RectHV(prev.rect.xmin(), 0, prev.rect.xmax(), prev.rect.ymin());
				}
			}
			// if this node is of verticle orientation; ie: y-value determines
			// where its children go
			else {
				// if this node is to right of parent
				if (this == prev.r_t) {
					rect = new RectHV(prev.rect.xmax(), prev.rect.ymin(), 1, prev.rect.ymax());
				}
				// if this node is to left of parent
				else {
					rect = new RectHV(0, prev.rect.ymin(), prev.rect.xmin(), prev.rect.ymax());
				}
			}
		}
	}
	
	// is the symbol table empty? 
	public boolean isEmpty() {
		return root == null;
	}
	
	// number of points 
	public int size() {
		return size;
	}
	
	// associate the value val with point p
	public void put(Point2D p, Value val) {
		if (p == null || val == null)
			throw new java.lang.IllegalArgumentException("Error: Neither argument can be null.");
		// use helper function to build new tree with new node (or new value of old node)
		// then assign it to the root
		root = put(root, p, val);
	}
	
	// put helper function
	private Node put(Node n, Point2D p, Value v) {
		// if there is no node, make a new one with given key and value
		if (n == null) {
			size++; // size book-keeping
			return new Node(p, v, n);
		}
		if (n.point.equals(p)) {
			n.val = v;
			return n;
		}
		// if the node is one based on horizontal orientation compare x values
		// of points
		if (n.horizontal) {
			// if given point.x greater than current node-point.x, move to right child of
			// current node
			if ( n.point.x() < p.x() )
				n.r_t = put(n.r_t, p, v);
			// if given point.x is less than or equal to current node-point.x, move to left child of
			// current node
			else
				n.l_b = put(n.l_b, p, v);
		}
		// if the node is one based on vertical orientation compare y values of
		// points
		else {
			// if given point.y greater than current node-point.y, move to right child of
			// current node
			if ( n.point.y() < p.y() )
				n.r_t = put(n.r_t, p, v);
			// if given point.y is less than or equal to current node-point.y, move to left child of
			// current node
			else
				n.l_b = put(n.l_b, p, v);
		}
		
		return n;
	}
	
	// value associated with point p 
	public Value get(Point2D p) {
		if (p == null)
			throw new java.lang.IllegalArgumentException("Error: Argument can't be null.");
		return get(root, p);
	}
	
	// hepler function for public get()
	private Value get(Node n, Point2D p) {
		if (n == null)
			return null;
		// if the node is one based on horizontal orientation compare x values
		// of points
		if (n.horizontal) {
			// if given point greater than current node, move to right child of
			// current node
			if ( n.point.x() < p.x() )
				return get(n.r_t, p);
			// if given point is less than current node, move to left child of
			// current node
			else if ( p.x() < n.point.x() )
				return get(n.l_b, p);
			// if they are equal, then key found; return value of current node
			else
				return (Value) n.val;
		}
		// if the node is one based on vertical orientation compare y values of
		// points
		else {
			// if given point greater than current node, move to right child of
			// current node
			if ( n.point.y() < p.y() )
				return get(n.r_t, p);
			// if given point is less than current node, move to left child of
			// current node
			else if ( p.y() < n.point.y() )
				return get(n.l_b, p);
			// if they are equal, then key found; return value of current node
			else
				return (Value) n.val;
		}
	}
	
	// does the symbol table contain point p? 
	public boolean contains(Point2D p) {
		if (p == null)
			throw new java.lang.IllegalArgumentException("Error: Argument can't be null.");
		Value check = get(root, p);
		if (check == null)
			return false;
		return true;
	}
	
	// all points in the symbol table 
	public Iterable<Point2D> points() {
		// create iterable to store points
		Queue<Point2D> out = new Queue<Point2D>();
		// pass in root and iterable to helper function to add all points to iterable
		pointsHelper(root, out);
		return out;
	}
	
	// helper function for points()
	private void pointsHelper(Node n, Queue<Point2D> out) {
		// TODO: make it walk through tree in level-order
		// if there is no node, don't add any points
		if (n == null)
			return;
		// add points from all nodes to left of given node
		pointsHelper(n.l_b, out);
		// add point in given node
		out.enqueue(n.point);
		// add points from all nodes to right of given node
		pointsHelper(n.r_t, out);
	}
	
	// all points that are inside the rectangle (or on the boundary) 
	public Iterable<Point2D> range(RectHV rect) {
		if (rect == null)
			throw new java.lang.IllegalArgumentException("Error: Argument can't be null.");
		Queue<Point2D> out = new Queue<Point2D>();
		rangeHelper(rect, root, out);
		return out;
	}
	
	// recursive helper method for range(); takes query RectHV, current node,
	// and the iterable to be returned by range()
	private void rangeHelper(RectHV rect, Node n, Queue<Point2D> out) {
		if (n == null)
			return;
		// if Node is a horizontal node, check to see if it's vertical "spliting
		// line" intersects the given RectHV
		if (n.horizontal) {
			// if "splitting line" intersects given RectHV, check if point at node
			// is in the RectHV
			if (rect.xmin() <= n.point.x() && n.point.x() <= rect.xmax()) {
				if (rect.contains(n.point))
					out.enqueue(n.point);
				// also recursively call rangeHelper() on both subtrees since
				// both could possible be in given RectHV
				rangeHelper(rect, n.l_b, out);
				rangeHelper(rect, n.r_t, out);
			}
			// if "splitting line" doesn't intersect given RectHV
			// check if splitting line is to right of given RectHV
			else if (rect.xmax() < n.point.x())
				// if it is, then call rangeHelper on left subtree since we know
				// no point to the right of "splitting line" will be in given RectHV
				rangeHelper(rect, n.l_b, out);
				// if not, then the given RectHV is to the right, call rangHelper()
				// on right subtree
			else 
				rangeHelper(rect, n.r_t, out);
		}
		// if Node is a vertical node, check to see if it's horizontl "spliting
		// line" intersects the given RectHV
		else {
			// if "splitting line" intersects given RectHV, check if point at node
			// is in the RectHV
			if (rect.ymin() <= n.point.y() && n.point.y() <= rect.ymax()) {
				if (rect.contains(n.point))
					out.enqueue(n.point);
				// also recursively call rangeHelper() on both subtrees since
				// both could possible be in given RectHV
				rangeHelper(rect, n.l_b, out);
				rangeHelper(rect, n.r_t, out);
			}
			// if "splitting line" doesn't intersect given RectHV
			// check if splitting line is to right of given RectHV
			else if (rect.ymax() < n.point.y())
				// if it is, then call rangeHelper on left subtree since we know
				// no point to the above of "splitting line" will be in given RectHV
				rangeHelper(rect, n.l_b, out);
				// if not, then the given RectHV is above, call rangHelper()
				// on right subtree
			else 
				rangeHelper(rect, n.r_t, out);
		}
	}
	
	// a nearest neighbor of point p; null if the symbol table is empty
	public Point2D nearest(Point2D p) {
		if (p == null)
			throw new java.lang.IllegalArgumentException("Error: Argument can't be null.");
		if (isEmpty())
			return null;
		//Point2D out = nearestHelper(p, root, root.point);
		return nearestHelper(p, root, root.point);
	}
	
	// recursive helper method that takes in query point, current node, and currently
	// marked nearest mark
	private Point2D nearestHelper(Point2D p, Node n, Point2D near) {
		// get distance from point at current node to given point
		double check_dist = n.point.distanceSquaredTo(p);
		// assign value for distance to nearest point
		double min_dist = near.distanceSquaredTo(p);
		
		// if the distance to point from current node is less than the current
		// min_distance, assign current node point to nearest point, and its
		// distance to nearest distance
		if (check_dist < min_dist) {
			near = n.point;
			min_dist = check_dist;
		}
		// if both subtrees of given Node have axis rectangles closer to given point
		// than the nearest distance so far, then check both subtrees
		if (n.l_b != null && n.r_t != null && n.l_b.rect.distanceSquaredTo(p) < min_dist && n.r_t.rect.distanceSquaredTo(p) < min_dist) {
			// for whichever orientation, check which side of "splitting line"
			// the given point is at, then check the subtree of that side first
			// 
			// NOTE: might be problem here. might need to check distances from point to splitting line
			if (n.horizontal) {
				// if point on left of current node splitting line
				if (p.x() < n.point.x()) {
					// check left subtree then right
					near = nearestHelper(p, n.l_b, near);
					near = nearestHelper(p, n.r_t, near);
				}
				// if point on right of current node splitting line
				else {
					// check right subtree then left
					near = nearestHelper(p, n.r_t, near);
					near = nearestHelper(p, n.l_b, near);
				}
			}
			else {
				// if point is under current node splitting line 
				if (p.y() < n.point.y()) {
					// check bottom subtree then top
					near = nearestHelper(p, n.l_b, near);
					near = nearestHelper(p, n.r_t, near);
				}
				// if point is over current node splitting line
				else {
					// check top subtree then bottom
					near = nearestHelper(p, n.r_t, near);
					near = nearestHelper(p, n.l_b, near);
				}
			}
		}
		// if only one subtree of given node has an axis rectangle closer than 
		// the min_dist then check that subtree only
		else if (n.l_b != null && n.l_b.rect.distanceSquaredTo(p) < min_dist)
			near = nearestHelper(p, n.l_b, near);
		else if (n.r_t != null && n.r_t.rect.distanceSquaredTo(p) < min_dist)
			near = nearestHelper(p, n.r_t, near);
		
		// return whatever point is nearest by this point
		return near;
	}
	
	// unit testing (required)
	public static void main(String[] args) {
		KdTreeST test = new KdTreeST();
		StdOut.println("A PointST is made with no points yet. It is empty:");
		StdOut.println("" + test.isEmpty() + "\n");
		
		Point2D p1 = new Point2D(.3, .7);
		Point2D p2 = new Point2D(.3, .4);
		test.put(p1, 1); test.put(p2, 2);
		StdOut.println("Two points, " + p1 + " and " + p2 + ", were put into the PointST.");
		StdOut.println("The size of the PointST is: " + test.size() + "\n");
		
		StdOut.println("The point " + p1 + " is in PointST with the value 1.");
		StdOut.println("If I get " + p1 + " from the PointST the value I get is: " + test.get(p1));
		StdOut.println("Point2D contains " + p1 + ": " + test.contains(p1) + "\n");
		
		Iterable<Point2D> points = test.points();
		StdOut.println("The points in Point2D are: ");
		for (Point2D n : points)
			StdOut.println(n);
		StdOut.println();
		
		RectHV r1 = new RectHV(.2, .1, .5, .5);
		StdOut.println("The only point in the rectangle " + r1 + " should be " + p2);
		Iterable<Point2D> range_test = test.range(r1);
		StdOut.println("All the points in " + r1 + " from PointSt are:");
		for (Point2D n : range_test)
			StdOut.println(n);
		StdOut.println();
		
		Point2D query = new Point2D(.4, .6);
		StdOut.println("The point closest to " + query + " should be " + p1);
		StdOut.println("The point closest to " + query + " in PointST is: " + test.nearest(query) + "\n");
		
		// testing throws
		try { test.put(null, null); }
		catch (java.lang.IllegalArgumentException e) {
			StdOut.println(e.getMessage());
		}
		try { test.get(null); }
		catch (java.lang.IllegalArgumentException e) {
			StdOut.println(e.getMessage());
		}
		try { test.contains(null); }
		catch (java.lang.IllegalArgumentException e) {
			StdOut.println(e.getMessage());
		}
		try { test.nearest(null); }
		catch (java.lang.IllegalArgumentException e) {
			StdOut.println(e.getMessage());
		}
		try { test.range(null); }
		catch (java.lang.IllegalArgumentException e) {
			StdOut.println(e.getMessage());
		}
	}
}