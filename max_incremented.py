from qgis.utils import *

@qgsfunction(args='auto', group='Custom')
def max_incremented(field_name, feature, parent):
	"""
		Auto-generates a new value (1 + maximum value) for the given field 
		
		<p><h4>Syntax</h4>
		max_incremented(<i>field_name</i>)</p>

		<p><h4>Arguments</h4>
		<i>  field_name</i> &rarr; name of the field for which new values are to be generated<br></p>
		
		<p><h4>Example</h4>
		<!-- Show example of function.-->
			 max_incremented('id') &rarr; 7</p>
	"""  
	layer = iface.activeLayer()
	field_name_index = layer.fieldNameIndex(field_name)
	return layer.maximumValue(field_name_index) + 1
