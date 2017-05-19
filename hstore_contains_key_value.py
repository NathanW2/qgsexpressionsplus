@qgsfunction(args='auto', group='Custom')
def hstore_contains_key_value(field, key_value, feature, parent):
	"""
		Returns True if the key/value exists in the hstore tags field. False otherwise.
		
		<p><h4>Syntax</h4>
		hstore_contains_key_value(<i>field</i>, <i>key_value</i>)</p>

		<p><h4>Arguments</h4>
		<i>  field</i> &rarr; name of the field containing the hstore tags (in double quotes)<br></p>
		<i>  key_value</i> &rarr; a key value pair<br></p>
		
		<p><h4>Example</h4>
		<!-- Show example of function.-->
			 hstore_contains_key_value("tags", 'amenity=>restaurant') &rarr; True</p>
	"""  
	hstore_string = field
	[key, value] = key_value.split('=>')
	search_string = '"'+key.strip()+'"=>"'+value.strip()+'"' 
	return search_string in hstore_string
