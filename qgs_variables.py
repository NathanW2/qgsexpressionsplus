from qgis.core import *
from qgis.utils import *

def get_env_variable(var_name):
    """ Returns the value of the variable 'var_name' """
    active_layer = iface.activeLayer()
    value = QgsExpressionContextUtils.layerScope(active_layer).variable(var_name) \
         or QgsExpressionContextUtils.projectScope().variable(var_name) \
         or QgsExpressionContextUtils.globalScope().variable(var_name)  
    return str(value)

    
def set_env_variable(scope, var_name, var_value):
    """
    Sets the value of the variable 'var_name' as 'var_value' 
    The scope can be global ('g'), project ('p') or layer ('l')
    """
    if scope.lower() in ('global', 'g'):
        QgsExpressionContextUtils.setGlobalVariable(var_name, var_value)
    if scope.lower() in ('project', 'p'):
        QgsExpressionContextUtils.setProjectVariable(var_name, var_value)
    if scope.lower() in ('layer', 'l'):
        active_layer = iface.activeLayer()
        QgsExpressionContextUtils.setLayerVariable(active_layer, var_name, var_value) 