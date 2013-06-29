"""
Extra functions for QgsExpression

register=False in order to delay registring of functions before we load the plugin
"""

from qgis.utils import qgsfunction
from qgis.core import QgsStyleV2
from PyQt4.QtCore import QObject 
from PyQt4.QtGui import QColor

def getFloat(value):
    try:
        return value, None
    except ValueError:
        return 0, "Can not convert {} to float".format(value)

@qgsfunction(2, "Expressions +", register=False)
def ramp_color_rgb(values, feature, parent):
    """
        Return only the rgb part of a defined color ramp
    """  
    ramp_name = values[0]
    ramp_position = values[1]
    
    ramp = QgsStyleV2.defaultStyle().colorRampRef(ramp_name)
    if not ramp:
        parent.setEvalErrorString( QObject.tr( '"{}" is not a valid color ramp'.format(ramp_name)))
        return QColor(0,0,0).name()
    
    value, error = getFloat(ramp_position)
    if error:
        parent.setEvalErrorString(error)
    
    color = ramp.color(value)
    return "{},{},{}".format(color.red(), color.green(), color.blue())
 
    
        