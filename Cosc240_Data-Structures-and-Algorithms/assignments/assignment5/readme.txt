/******************************************************************************
 *  Name:       Richard Flores	
 *
 *  Hours to complete assignment (optional): N/A
 *
 ******************************************************************************/

Programming Assignment 5: Kd-Trees


/******************************************************************************
 *  Describe the Node data type you used to implement the
 *  2d-tree data structure.
 *****************************************************************************/

 First I had instance variables for the Point2D (which was the key), the 
 Value, a reference each for the left and right children, RectHV based off the
 value for point and the parent node's rectangle. I also stored a boolean to tell
 if the node is based off a horizontal or verticle orientation. Meaning (kind of
 unintuitively) that if it is horizontal, there is a verticle splitting line 
 between the children nodes. And if it's verticle then there is a horizontal 
 splitting line between the children nodes.
 
 The constructor took a Point2D and a Value to store in the node. It also took
 the reference of the parent node to determine it's RectHV and determine the
 orientation. If the parent was horizontal then the node would be verticle and
 vice versa.
 
/******************************************************************************
 *  Describe your method for range search in a kd-tree.
 *****************************************************************************/

 First I create a Queue<Point2D> to store the points in. Then pass in the 
 reference to the root node, reference to the Queue, and the query RectHV into 
 a recursive helper method.
 
 The method basically first checks if the current node's splitting line intersects
 the query square. If it does then it checks if the point of the current node's 
 point is contained in the query rectangle. If it is, then the point it added to
 the queue through it's passed reference. Whether the point is in the rectangle 
 or not, the mehtod then continues to call itself twice using the each child 
 subtree per call. This is so that it searches both subtrees for any more points.
 
 Now if the current node's splitting line didn't intersect the query square, the
 method checks which side of the splitting line the query rectangle is on then
 call itself using the refence of the subtree that is on the corisponding side.

The base case for this is that if the given node is null, meaning that end of
the tree has been reached. 
 
 By the end of all the recursive calls, the Queue is has all points within the
 query RectHV. The queue is then returned in the original method.

/******************************************************************************
 *  Describe your method for nearest neighbor search in a kd-tree.
 *****************************************************************************/

 If the kd-tree is empty, null is returned. If not then instead the original 
 returns a recursive helper method with the given query point, root node, and
 the point of the root node as arguments.
 
 The helper method takes the query point, the current node in search, and the 
 currently closest point to the query point. Due to the original method, the 
 closest point is the point of the root node; which makes sense since it is the
 only node searched so far.
 
 Anyways for each call of the helper method the distance of the given node's
 point to the query point is stored, along with the distance of the nearest
 point to the query point. And if the distance to the current node's point is
 less than the the distance to the current closest point, then the nearest point
 is now the point of the current node. The distance to the nearest point is then
 recalculated.
 
 Now the helper method checks if the rectangles of both children of the current
 node have a distance to the query point less than the current nearest point
 distance; while also checking that both children aren't null. If both children's
 rectangles are closer then the helper method calls itself twice, passing in
 one then the other children nodes. The order of this is determined by which
 side of the current node's splitting line the query point is. The child node
 that is on the same side as the query point is processed first.
 
 If the children node's rectangles weren't both closer than the currently nearest
 point (or at least one child was null), then the helper method individually checks
 each child node to see if their rectangle is closer than the nearest point (if
 they exist). It then processes that node by calling itself on that child node.
 
 By the end of this each appropriate node has been processed and the nearest 
 point found. The method returns the nearest point.

/******************************************************************************
 *  How many nearest neighbor calculations can your brute-force
 *  implementation perform per second for input100K.txt (100,000 points)
 *  and input1M.txt (1 million points), where the query points are
 *  random points in the unit square?
 *
 *  Show the raw data you used to determine the operations per second.
 *  (Do not count the time to read in the points or to build the 2d-tree.)
 *
 *  Repeat the question but with the 2d-tree implementation.
 *****************************************************************************/

                       calls to nearest() per second
                     brute force               2d-tree
                     ---------------------------------
input100K.txt			113						223

input1M.txt				7						12



/******************************************************************************
 *  Known bugs / limitations.
 *****************************************************************************/


/******************************************************************************
 *  Describe whatever help (if any) that you received.
 *  Don't include readings or lectures, but do
 *  include any help from people and attribute them by name.
 *****************************************************************************/

 Help by you my professor in helping me more clearly understand how rectangles
 of newly added points are based off of their parents in the Kd-Tree 
 implementation.

/******************************************************************************
 *  Describe any serious problems you encountered.                    
 *****************************************************************************/

 Just bad bugs and another really bad typo where I thought my nearest() method 
 in the Kd version was not working but was, I just misstyped something in my
 Node constructor where the rectangles are made.

/******************************************************************************
 *  List any other comments here. Feel free to provide any feedback   
 *  on how much you learned from doing the assignment, and whether 
 *  you enjoyed doing it.
 *****************************************************************************/
 
 Again this was a lot of fun (especially with everything working this time). I
 wasn't sure how you wanted us to test out nearest method so I made a modified
 version of NearestNeighborVisualizer for each implementation. I will include it
 in the submission just so you could see.
 
 Sorry that it is late again and then even with the extra day I couldn't do the 
 challenge of getting the boid simulator to work. I will hopefully have free time
 after my internship submission to play around with that.
