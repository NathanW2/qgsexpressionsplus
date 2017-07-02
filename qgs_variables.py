from qgis.core import *
from qgis.utils import *

def get_env_variable(var_name):
	"""
		Returns the value of a layer, project or global variable
		
		<p><h4>Syntax</h4>
		get_env_variable(<i>var_name</i>)</p>

		<p><h4>Arguments</h4>
		<i>  var_name</i> &rarr; the name of the variable whose value is required<br></p>
		
		<p><h4>Example</h4>
		<!-- Show example of function.-->
			 get_env_variable('qgis_release_name') &rarr; 'Las Palmas'</p>
	"""  
	active_layer = iface.activeLayer()
	value = QgsExpressionContextUtils.layerScope(active_layer).variable(var_name) \
		 or QgsExpressionContextUtils.projectScope().variable(var_name) \
		 or QgsExpressionContextUtils.globalScope().variable(var_name)  
	return str(value)

    
def set_env_variable(scope, var_name, var_value):
	"""
		Sets a user-defined value for a layer, project or global variable
		
		<p><h4>Syntax</h4>
		set_env_variable(<i>scope</i>, <i>var_name</i>, <i>var_value</i>)</p>

		<p><h4>Arguments</h4>
		<i>  scope</i> &rarr; the scope of the variable ('global'/'g', 'project'/'p' or 'layer'/'l')<br></p>
		<i>  var_name</i> &rarr; the name of the variable<br></p>
		<i>  var_value</i> &rarr; a value for the variable<br></p>
		
		<p><h4>Example</h4>
		<!-- Show example of function.-->
			 set_env_variable('l', 'layer_type', 'vector point')</p>
	"""  
	if scope.lower() in ('global', 'g'):
		QgsExpressionContextUtils.setGlobalVariable(var_name, var_value)
	if scope.lower() in ('project', 'p'):
		QgsExpressionContextUtils.setProjectVariable(var_name, var_value)
	if scope.lower() in ('layer', 'l'):
		active_layer = iface.activeLayer()
		QgsExpressionContextUtils.setLayerVariable(active_layer, var_name, var_value)
