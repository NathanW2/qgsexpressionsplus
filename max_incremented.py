from qgis.core import *
from qgis.gui import *
from qgis.utils import *

@qgsfunction(args=1, group='Custom')
def max_incremented(fieldName, feature, parent):
	""" Generates a new value (1 + maximum value) for the given field """
	layer = iface.activeLayer()
	fieldNameIndex = layer.fieldNameIndex(fieldName[0])
	return layer.maximumValue(fieldNameIndex) + 1
