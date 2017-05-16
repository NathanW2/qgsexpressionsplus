from qgis.core import *
from qgis.gui import *

@qgsfunction(args='auto', group='Custom')
def max_incremented(field_name, feature, parent):
	""" Generates a new value (1 + maximum value) for the given field """
	layer = iface.activeLayer()
	field_name_index = layer.fieldNameIndex(field_name)
	return layer.maximumValue(field_name_index) + 1
