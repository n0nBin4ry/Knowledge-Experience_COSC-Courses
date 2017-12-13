// Richard Flores

import edu.princeton.cs.algs4.Bag;
import edu.princeton.cs.algs4.RedBlackBST;
import edu.princeton.cs.algs4.Point2D;
import edu.princeton.cs.algs4.RectHV;
import edu.princeton.cs.algs4.StdOut;

public class PointST<Value> {
	
	private int size = 0;
	private RedBlackBST<Point2D, Value> st = new RedBlackBST<Point2D, Value>();
	// construct an empty symbol table of points 
	public PointST() {
		
	}
	
	// is the symbol table empty? 
	public boolean isEmpty() {
		return st.isEmpty();
	}
	
	// number of points 
	public int size() {
		return st.size();
	}
	
	// associate the value val with point p
	public void put(Point2D p, Value val) {
		if (p == null || val == null)
			throw new java.lang.IllegalArgumentException("Error: Neither argument can be null.");
		st.put(p, val);
	}
	
	// value associated with point p 
	public Value get(Point2D p) {
		if (p == null)
			throw new java.lang.IllegalArgumentException("Error: Argument can't be null.");
		return st.get(p);
	}
	
	// does the symbol table contain point p? 
	public boolean contains(Point2D p) {
		if (p == null)
			throw new java.lang.IllegalArgumentException("Error: Argument can't be null.");
		return st.contains(p);
	}
	
	// all points in the symbol table 
	public Iterable<Point2D> points() {
		return st.keys();
	}
	
	// all points that are inside the rectangle (or on the boundary) 
	public Iterable<Point2D> range(RectHV rect) {
		if (rect == null)
			throw new java.lang.IllegalArgumentException("Error: Argument can't be null.");
		Bag<Point2D> out = new Bag<Point2D>();
		for (Point2D p : st.keys())
			if (rect.xmin() <= p.x() && p.x() <= rect.xmax() && rect.ymin() <= p.y() && p.y() <= rect.ymax())
				out.add(p);
		return out;
	}
	
	// a nearest neighbor of point p; null if the symbol table is empty
	public Point2D nearest(Point2D p) {
		if (p == null)
			throw new java.lang.IllegalArgumentException("Error: Argument can't be null.");
		if (st.isEmpty())
			return null;
		Point2D out = null;
		double min_distance = -1;
		double tar_distance;
		for (Point2D tar : st.keys()) {
			tar_distance = p.distanceSquaredTo(tar);
			if (tar_distance < min_distance) {
				out = tar;
				min_distance = tar_distance;
			}
			else if (min_distance == -1) {
				out = tar;
				min_distance = tar_distance;
			}

		}
		return out;
	}
	
	// unit testing (required)
	public static void main(String[] args) {
		PointST test = new PointST();
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