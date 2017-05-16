QgsExpression Plus
==================

Extra expression functions for the QGIS expression engine that didn't make it into QGIS 2.0

Contributors welcome :)

Current functions so far
---------------------

::

	ramp_color_rgb -> Return just rgb from the given color ramp

Function ideas
---------------------

:: 

	 red()
	 green()
	 blue()
	 alpha()
	 hue()
	 saturation()

Just a quick note
+++++++++++++++++

Functions used from this project will not be available in other QGIS installs without
first installing and enabling this plugin.

Function Description and Usage
---------------------

- **max_incremented('field_name')**

	Given the name of the field (field_name), returns 1 + the maximum value for the field. Can be used to automatically generate primary keys (eg. id, fid) when adding features in QGIS. 
	
	To use this function:   
	
	1. Go to Layer Properties -> Fields -> Click on the *Text Edit* button in the *Edit widget column* to open up the *Edit Widget Properties* dialog box. 
	2. Click on the Expression symbol to the right of the *Default value* text box. This would open the *Expression dialog*.
	3. Enter an expression like the following in the Expression tab. 

		::	

			max_incremented('id')

	To avoid the user from editing the automatically generated id, uncheck the *Editable* checkbox in the *Edit Widget Properties* dialog.

- **get_env_variable('var_name')**

	Returns the value of the variable 'var_name'. The variable can be a global, project or layer variable. See *Layer Properties -> Variables*.  
	
	This function is not an expression function as we generally wouldn't need to call it for each feature on the layer (it will return the same value for each feature), but it can be called from the Python console in QGIS, or from another expression function. 
	
	Save the file *qgs_variables.py* in `%userprofile%/.qgis2/python` and call the function in the Python console as:   
	::	
		import qgs_variables
		qgs_variables.get_env_variable('user_full_name')

- **set_env_variable('scope, 'var_name', 'var_value')**

	Sets the value of the variable 'var_name' as 'var_value'. The 'scope' can be a global ('g'), project ('p) or layer ('l'). Similar to *get_env_variable()*, save the file *qgs_variables.py* in `%userprofile%/.qgis2/python` and call the function in the Python console as:   
	::	
		import qgs_variables
		qgs_variables.set_env_variable('l', 'layer_type', 'vector_point')


- **hstore_get_value(hstore_attr, key)**

    Given the key, this function returns its value from the hstore string.
    If the key is not present, it returns *null*.
    
    ::
    
    	Example usage: hstore_get_value('other_tags', 'tourism')

    The query above will select all features for which this function returns a non-null value, i.e. all features that contain the key `tourism` in their hstore.


- **hstore_exist(hstore_attr, key)**

    Returns whether the given key exists in the hstore string (True or False).
    
    ::
    
    	Example usage: hstore_exist('other_tags', 'tourism')

    The query above will select all features which contain the key `tourism` in their hstore.


- **hstore_contains_key_value(hstore_attr, key_value)**

    Returns whether the given key value pair exists in the hstore string (True or False).
    
    ::
    
    	Example usage: hstore_contains_key_value('other_tags', 'tourism=>information')

    The query above will select all features which contain the key value pair `tourism=>information` in their hstore.


- **hstore_contains_hstore(hstore_attr, hstore_input_string)**

    Returns whether the given hstore string exists in the feature's hstore attribute (True or False).
    
    ::
    
    	Example usage: hstore_contains_hstore('other_tags', 'tourism=>information,information=>guidepost')

    The query above will select all features which contain both the key-value pairs, `tourism=>information` and `information=>guidepost` in their hstore. The function also accepts and returns the correct result for input hstore strings that have spaces or double quotes surrounding the keys and values.
