import edu.princeton.cs.algs4.StdDraw;
import edu.princeton.cs.algs4.StdOut;
import edu.princeton.cs.algs4.StdRandom;

public class RandomConnections {
	// constants
	public static final double R = .5;
	public static final double center_x = .5;
	public static final double center_y = .5;
	// static methods (functions)
	public static double yFromRad(double rad, double radius) {
		return radius * Math.sin(rad); // y = r * sin(theta)
	}
	public static double xFromRad(double rad,double radius) {
		return radius * Math.cos(rad); // x = r * cos(theta)
	}
	public static boolean yesNo(double chance) { // chance should be double from 0 to 1, anything 1 or higher gets an automatic true return
		if (StdRandom.uniform() <= chance)
			return true;
		else
			return false;
	}
	// main method
	public static void main(String[] args) {
		int N = Integer.parseInt(args[0]); // number of points; from cmd line
		double p = Double.parseDouble(args[1]); // probability of each line getting drawn; from cmd line
		double distribute = ((360 * Math.PI) / 180 ) / N; // divides circle angle by number of points (N) in radians
		// create canvas and background
		StdDraw.setCanvasSize();
		StdDraw.setPenColor(StdDraw.BLACK);
		StdDraw.filledRectangle(center_x,center_y,R,R);
		// create and draw points
		StdDraw.setPenRadius(.01);
		StdDraw.setPenColor(StdDraw.BLACK);
		double[][] points = new double [N][2]; // 2D array; [number of points] [ each array has 2 indexes: x then y of point]
		for (int i = 0; i < N; i++) {
			// assigned x and y positions to each points, relative to origin
			points[i][0] = xFromRad(distribute * i, R) + center_x;
			points[i][1] = yFromRad(distribute * i, R) + center_y;
			StdDraw.point(points[i][0], points[i][1]);
			// all print commands in main were set up for my debugging, but looked nice so I kept them
			StdOut.printf("Point %d :\n", i + 1);
			StdOut.printf("angle(rads) = %f\n", distribute * i);
			StdOut.printf("x-position of Point: %f\ny-position of Point: %f\n", points[i][0], points[i][1]);
			StdOut.printf("Cos of angle: %f\nSin of angle: %f\n\n", Math.cos(distribute * i), Math.sin(distribute * i));
		}
		// draw lines
		StdDraw.setPenRadius();
		StdDraw.setPenColor(StdDraw.MAGENTA);
		StdOut.print("Drawing Lines. . . ");
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < N; j++) {
				// was going to have a case where if i == j to skip the loop but realized it would just draw no line anyways
				if (yesNo(p))
					StdDraw.line(points[i][0], points[i][1], points[j][0], points[j][1]);
			}
		}
		StdOut.print("Done!");
	}
}