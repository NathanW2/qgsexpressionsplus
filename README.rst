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

jitter_geometry('max_offset_percent', 'segment_length_percent')
+++++++++++++++++

This function creates a jittered geometry from a linestring or polygon geometry. Given the maximum offset and segment length as percentages, it first interpolates points on the line at the segments. Then it displaces the point perpendicular to the line by a random distance less than or equal to the maximum offset. Finally it joins all these displaced points and returns a linestring.

To use this function:   

1. Go to Layer Properties -> Style -> Click on the green *Plus* button to *Add a Symbol layer*.
2. Set the *Symbol layer type* as *Geometry generator*.
3. Set the *Geometry Type* as *LineString/MultiLineString* for linestrings or *Polygon/Multipolygon* for polygons.
4. *Load* the *jitter_geometry.py* file in the Function Editor.
5. In the Expression Tab, call the function as:

::	

	jitter_geometry(5, 20)
Where '5' and '20' are the maximum_offset_percent and segment_length_percent respectively. These values can range between 1 and 99.

6. On clicking 'OK' the jitter lines will be displayed on the layer.



**Note:**

The maximum offset is calculated from the maximum_offset_percent as:
::
	maximum_offset = (max_offset_percent*length_of_line)/100

Similarly the  segment length is calculated from the segment_length_percent as:
::
	segment_length = (segment_length_percent*length_of_line)/100
	
The reason is that if the user enters absolute values for the offset and segment lengths, they maybe too large or small compared to the length of the line, and we would not get the desired output. A smaller value for the max_offset_percent and segment_length_percent generates a better output, especially for polygons. Recommended range for max_offset_percent and segment_length_percent for polygons would be [1,5] and [1,10] respectively.


max_incremented('field_name')
+++++++++++++++++

Given the name of the field (field_name), returns 1 + the maximum value for the field. Can be used to automatically generate primary keys (eg. id, fid) when adding features in QGIS. 

To use this function:   

1. Go to Layer Properties -> Fields -> Click on the *Text Edit* button in the *Edit widget column* to open up the *Edit Widget Properties* dialog box. 
2. Click on the Expression symbol to the right of the *Default value* text box. This would open the *Expression dialog*.
3. Enter an expression like the following in the Expression tab. 

::	

	max_incremented('id')

To avoid the user from editing the automatically generated id, uncheck the *Editable* checkbox in the *Edit Widget Properties* dialog.

get_env_variable('var_name')
+++++++++++++++++

Returns the value of the variable 'var_name'. The variable can be a global, project or layer variable. See *Layer Properties -> Variables*.  

This function is not an expression function as we generally wouldn't need to call it for each feature on the layer (it will return the same value for each feature), but it can be called from the Python console in QGIS, or from another expression function. 

Save the file *qgs_variables.py* in `%userprofile%/.qgis2/python` and call the function in the Python console as:   
::	
	import qgs_variables
	qgs_variables.get_env_variable('user_full_name')

set_env_variable('scope, 'var_name', 'var_value')
+++++++++++++++++

Sets the value of the variable 'var_name' as 'var_value'. The 'scope' can be a global ('g'), project ('p) or layer ('l'). Similar to *get_env_variable()*, save the file *qgs_variables.py* in `%userprofile%/.qgis2/python` and call the function in the Python console as:   
::	
	import qgs_variables
	qgs_variables.set_env_variable('l', 'layer_type', 'vector_point')


hstore_get_value("field", 'key')
+++++++++++++++++

Given the field containing the hstore tags and a key, this function returns the key's value from the hstore tags.
If the key is not present, it returns *null*.

For example:

::

	hstore_get_value("tags", 'amenity')

**Note** The name of the field must be surrounded with double quotes, while strings with single quotes. In the example above, the hstore tags are contained in the field "tags", and the key to be searched for is 'amenity'.

hstore_exist("field", 'key')
+++++++++++++++++

Returns whether the given key exists in the hstore string (True or False). *field* is the name of the field containing the hstore tags.

For example:

::

	hstore_exist("tags", 'amenity')

The expression above can be used to *Select Features by Expression*, and would select all features which have the `amenity` tag.

hstore_contains_key_value("field", 'key_value')
+++++++++++++++++

Returns whether the given key value pair exists in the hstore string (True or False).

For example:

::

	hstore_contains_key_value("tags", 'amenity=>restaurant')

The expression above can be used to *Select Features by Expression*, and would select all restaurants, i.e. all features which have the `amenity=>restaurant` tag.


hstore_contains_hstore("field", 'hstore_input')
+++++++++++++++++

Returns whether the hstore tags field contains all the keys and values in the hstore_input (True or False).

::

	hstore_contains_hstore("tags", 'amenity=>restaurant,cuisine=>swiss')

The query above will select all features which contain both the key-value pairs, `amenity=>restaurant` and `cuisine=>swiss` in their hstore tags.
