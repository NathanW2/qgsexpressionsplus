""" Ref: https://nathanw.net/2012/08/05/generating-chainage-distance-nodes-in-qgis/ """

from math import atan, sin, cos
from random import uniform

@qgsfunction(args='auto', group='Custom', usesgeometry=True)
def jitter_line(max_offset_percent, segment_percent, feature, parent):
	""" Returns a jittered line geometry """

	line = feature.geometry()
	length = line.length()
	max_offset = float(max_offset_percent*length)/100.0
	point_distance = 0
	points_list = []
	while point_distance <= length:
		point = line.interpolate(point_distance).asPoint()
		points_list.append(point)
		point_distance += float(segment_percent*length)/100.0
	jittered_line = QgsGeometry.fromPolyline(get_displaced_points(points_list, max_offset))
	return jittered_line

def get_displaced_points(points_list, max_offset):
	""" 
	Displaces the points perpendicular to the line by a 
	random distance less than or equal to max_offset
	"""

	a = atan((points_list[0].x() - points_list[-1].x())/(points_list[0].y() - points_list[-1].y()))
	# 'a' is the angle that the perpendicular to the line makes with the y axis 
	for point in points_list[1:-1]:
		offset = uniform(-1*max_offset, max_offset)
		point.set(point.x() + offset*sin(a), point.y() - offset*cos(a))
	return points_list
