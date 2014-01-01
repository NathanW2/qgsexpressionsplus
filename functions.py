"""
Extra functions for QgsExpression

register=False in order to delay registring of functions before we load the plugin
"""

from qgis.utils import qgsfunction
from qgis.core import QgsStyleV2, QgsExpression, QgsSymbolLayerV2Utils
from PyQt4.QtCore import QObject, QDateTime, QDate
from PyQt4.QtGui import QColor
import math

import colorfunctions

def getFloat(value):
    try:
        return value, None
    except ValueError:
        return 0, "Can not convert {} to float".format(value)

@qgsfunction(2, "Expressions +", register=False)
def ramp_color_rgb(values, feature, parent):
    """
        Return only the rgb part of a defined color ramp
        
        <h4>Syntax</h4>
        <p>ramp_color_rgb(<i>ramp_name,value</i>)</p>

        <h4>Arguments</h4>
        <p><i>  ramp_name</i> &rarr; the name of the color ramp as a string, for example 'Spectral'.<br>
        <i>  value</i> &rarr; the position on the ramp to select the color from as a real number between 0 and 1.<br></p>
        
        <h4>Example</h4>
        <p><!-- Show example of function.-->
             ramp_color_rgb('Spectral',0.3) &rarr; '253,190,115'</p>
        
        <h4>Note:</h4>
        <p>The color ramps available vary between QGIS installations.  This function
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
def get_color_part(values, feature, parent):
    partname = "get_{0}".format(values[0])
    return colorfunctions.color_part(partname, values, feature, parent)
        
@qgsfunction(1, "Expressions +", register=False)
def set_color_part(values, feature, parent):
    partname = "set_{0}".format(values[0])
    return colorfunctions.color_part(partname, values, feature, parent)
      
@qgsfunction(1, "Expressions +", register=False)
def dow(values, feature, parent):
    """
        Returns an integer representing the day of week for a given date. Returned 
        values range from 0-6, where 0 is Sunday.
        
        <h4>Syntax</h4>
        <p>dow(<i>date</i>)</p>

        <h4>Arguments</h4>
        <p><i>  date</i> &rarr; a date value. Must be a valid date or datetime field, or a 
        string in the format 'yyyy-mm-dd'.<br></p>
        
        <h4>Example</h4>
        <p><!-- Show example of function.-->
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

@qgsfunction(2, "Expressions +", register=False)
def halton_sequence(values, feature, parent):        
    """
        Returns a quasi-random number from the deterministic, low-discrepancy Halton sequence.
        
        <h4>Syntax</h4>
        <p>halton_sequence(<i>index</i>, <i>base</i>)</p>

        <h4>Arguments</h4>
        <p><i>  index</i> &rarr; the position within the sequence to return. Since Halton sequences are deterministic,
        the number returned for a given index and base will always be the same.<br>
        <i>  base</i> &rarr; must be a prime number, and should differ between dimensions if generating n-dimensional
        points (eg, base=2 and base=3 for generating 2 dimensional points). If unsure, 2 is a good choice for base.
        </p>
    """
    
    index = values[0]
    base = values[1]
    return halton(index, base)
    
def halton( index, base = 2 ):
    """
        Returns a quasi-random number from the deterministic, low-discrepancy Halton sequence.
    """
    result = 0
    f = 1.0 / base
    i = float(index)
    while i > 0:
       result += f * ( i % base )
       i = math.floor( i / base )
       f = f / base
    return result
    
@qgsfunction(4, "Expressions +", register=False)
def quasi_rand(values, feature, parent):        
    """
        Returns a quasi-random integer within the range specified by the minimum and maximum argument (inclusive). 
        This function takes four arguments. 
        
        <h4>Syntax</h4>
        <p>quasi_rand(<i>seed</i>, <i>base</i>, <i>min</i>, <i>max</i>)</p>

        <h4>Arguments</h4>
        <p><i>  seed</i> &rarr; an integer representing the position of the quasi-random number in the sequence. The returned
                result will always be the same for a given seed and base.<br>
        <i>  base</i> &rarr; an integer prime number representing a quasi-random sequence to use. 2, 3 or 5 are good choices. Use different
                base values for each dimension when creating multi-dimensional random number sets.<br>                
        <i>  min</i> &rarr; an integer representing the smallest possible quasi random number desired.<br>
        <i>  max</i> &rarr; an integer representing the smallest possible quasi random number desired.
        </p>
    """
    seed = values[0]
    base = values[1]
    min = values[2]
    max = values[3]
    
    return math.floor(halton(seed, base) * (max - min + 1) + min)
        
@qgsfunction(1, "Expressions +", register=False)
def dow(values, feature, parent):
    """
        Returns an integer representing the day of week for a given date. Returned 
        values range from 0-6, where 0 is Sunday.
        
        <h4>Syntax</h4>
        <p>dow(<i>date</i>)</p>

        <h4>Arguments</h4>
        <p><i>  date</i> &rarr; a date value. Must be a valid date or datetime field, or a 
        string in the format 'yyyy-mm-dd'.<br></p>
        
        <h4>Example</h4>
        <p><!-- Show example of function.-->
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

functions = [ramp_color_rgb,  dow, halton_sequence, quasi_rand, get_color_part, set_color_part]
        
def registerFunctions():
    for func in functions:
        if QgsExpression.registerFunction(func):
            yield func.name()
            
def unregisterFunctions():            
    # Unload all the functions that we created.        
    for func in functions:
        QgsExpression.unregisterFunction(func.name())
