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

Function usage
---------------------

- **max_incremented('fieldName')**

	Given the name of the field (fieldName), returns 1 + the maximum value for the field. Can be used to automatically generate primary keys (eg. id, fid) when adding features in QGIS. Paste the following expression in the *Default value* box in the *Edit Widget Properties* dialog. 

	::	

		Example usage: max_incremented('fid')

	To avoid the user from editing the automatically generated id, uncheck the `Editable` checkbox in the Edit Widget Properties dialog.
	
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
