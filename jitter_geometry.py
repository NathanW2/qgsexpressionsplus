""" Ref: https://nathanw.net/2012/08/05/generating-chainage-distance-nodes-in-qgis/ """

from qgis.utils import *
from math import atan, radians, sin, cos
from random import uniform

@qgsfunction(args='auto', group='Custom', usesgeometry=True)
def jitter_geometry(max_offset_percent, segment_length_percent, feature, parent):
	"""
		Returns a jittered geometry
		
		<p><h4>Syntax</h4>
		jitter_geometry(<i>max_offset_percent</i>, <i>segment_length_percent</i>)</p>

		<p><h4>Arguments</h4>
		<i>  max_offset_percent</i> &rarr; the maximum offset in percentage by which a point on the geometry should be moved (between 1 and 99)<br></p>
		<i>  segment_length_percent</i> &rarr; the length of the segment in percentage (between 1 and 99)<br></p>
		
		<p><h4>Example</h4>
		<!-- Show example of function.-->
			 jitter_geometry(5, 20)</p>
			 
		<p><h4>Note</h4>
			For polygons, small values for the maximum_offset_percent and segment_length_percent are recommended.
			Following are the recommended ranges:
			<ul>
				<li>maximum_offset_percent = [1,5]</li>
				<li>segment_length_percent  = [1,10]</li>
			</ul>
	"""  
	geom = feature.geometry()
	length = geom.length()
	max_offset = float(max_offset_percent*length)/100.0
	point_distance = 0
	points_list = []
	while point_distance <= length:
		point = geom.interpolate(point_distance).asPoint()
		points_list.append(point)
		point_distance += float(segment_length_percent*length)/100.0
	jittered_line = QgsGeometry.fromPolyline(get_displaced_points(points_list, max_offset))
	geom = jittered_line.convertToType(QgsVectorLayer.geometryType(iface.activeLayer()))
	return geom

def get_displaced_points(points_list, max_offset):
	""" 
		Displaces the points perpendicular to the line by a 
		random distance less than or equal to max_offset
	"""  
	if points_list[0].y() != points_list[-1].y():
		a = atan((points_list[0].x() - points_list[-1].x())/(points_list[0].y() - points_list[-1].y()))
	else:
		a = radians(90)
	# 'a' is the angle that the perpendicular to the line makes with the y axis 
	for point in points_list[1:-1]:
		offset = uniform(-1*max_offset, max_offset)
		point.set(point.x() + offset*sin(a), point.y() - offset*cos(a))
	return points_list
