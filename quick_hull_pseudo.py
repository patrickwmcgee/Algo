#quickhull pseudo
def quickhull(set_of_points):
	# the point of this algorithm is to find the convex hull of a given set of set_of_points
	convex_hull = set{} # set of convex points making up the hull
	min_x,max_x = find_min_and_max_x

	subset_above, subset_below = split_set_above_and_below(set_of_points, line(min_x,max_x))
	recursive_step(subset_above,line,convex_hull)
	recursive_step(subset_below,line,convex_hull)

	return convex_hull

def recursive_step(set_of_points, line,convex_hull):
	if set_of_points.size() == 0 # If the number of points in the set are 0, there are no more points to process and we return up

	# find the point farthest from the line and make a triangle out of it
	point_to_make_triangle = find_point_farthest_from_line(set_of_points)
	triangle = create_triangle(line.point1,line.point2, point_to_make_triangle)

	# append the farthest point to the convex hull set
	convex_hull.append(point_to_make_triangle)

	#iterate through the points to check to see if they are in the triangle that has been made
	for point in set_of_points:
		if is_point_in_triangle(point, triangle)
			# if the the point is in the triangle, delete it from the set of points

	recursive_step(set_of_points, make_line(line.point1, point_to_make_triangle))
	recursive_step(set_of_points, make_line(line.point2, point_to_make_triangle))

def find_min_and_max_x(set_of_points):
	# find the min and max x points

def find_point_farthest_from_line(line, set_of_points):
	# find the points farthest from the given line

def make_line(point1,point2):
	# given two points, create a line

def create_triangle(point1,point2,point3):
	# create a triangle 

def is_point_in_triangle(point,triangle):
	# check to see if a point is in a triangle

def split_set_above_and_below(set_of_points, line):
	# split the set of points above or below a line