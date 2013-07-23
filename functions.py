"""
Extra functions for QgsExpression

register=False in order to delay registring of functions before we load the plugin
"""

from qgis.utils import qgsfunction
from qgis.core import QgsStyleV2, QgsExpression
from PyQt4.QtCore import QObject, QDateTime, QDate
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
        
        <p><h4>Syntax</h4>
        ramp_color_rgb(<i>ramp_name,value</i>)</p>

        <p><h4>Arguments</h4>
        <i>  ramp_name</i> &rarr; the name of the color ramp as a string, for example 'Spectral'.<br>
        <i>  value</i> &rarr; the position on the ramp to select the color from as a real number between 0 and 1.<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             ramp_color_rgb('Spectral',0.3) &rarr; '253,190,115'</p>
        
        <p><h4>Note:</h4>
        The color ramps available vary between QGIS installations.  This function
        may not give the expected results if you move your Quantum project.
        </p>
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

@qgsfunction(1, "Expressions +", register=False)
def dow(values, feature, parent):
    """
        Returns an integer representing the day of week for a given date. Returned 
        values range from 0-6, where 0 is Sunday.
        
        <p><h4>Syntax</h4>
        dow(<i>date</i>)</p>

        <p><h4>Arguments</h4>
        <i>  date</i> &rarr; a date value. Must be a valid date or datetime field, or a 
        string in the format 'yyyy-mm-dd'.<br></p>
        
        <p><h4>Example</h4>
        <!-- Show example of function.-->
             dow('2013-07-01') &rarr; 1</p>
    """  
    input_date = values[0]
    
    # Return dayOfWeek() % 7 so that values range from 0 (sun) to 6 (sat)
    # to match Postgresql behaviour
    if type(input_date) == QDateTime:
      return input_date.date().dayOfWeek() % 7
    elif type(input_date) == QDate:
      return input_date.dayOfWeek() % 7
    elif type(input_date) in (str, unicode):      
      # Convert string to qdate
      input_qdate = QDate.fromString(input_date, 'yyyy-MM-dd')
      if input_qdate.isValid():
        return input_qdate.dayOfWeek() % 7     
      else:
        return None

 
functions = [ramp_color_rgb, dow]
        
def registerFunctions():
    for func in functions:
        if QgsExpression.registerFunction(func):
            yield func.name()
            
def unregisterFunctions():            
    # Unload all the functions that we created.        
    for func in functions:
        QgsExpression.unregisterFunction(func.name())
