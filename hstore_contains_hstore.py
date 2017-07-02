@qgsfunction(args='auto', group='Custom')
def hstore_contains_hstore(field, hstore_input, feature, parent):
	"""
		Returns True if the hstore tags field contains all the keys and values in the hstore_input.
		False otherwise.
		
		<p><h4>Syntax</h4>
		hstore_contains_hstore(<i>field</i>, <i>hstore_input</i>)</p>

		<p><h4>Arguments</h4>
		<i>  field</i> &rarr; name of the field containing the hstore tags (in double quotes)<br></p>
		<i>  hstore_input</i> &rarr; hstore containing keys and values<br></p>
		
		<p><h4>Example</h4>
		<!-- Show example of function.-->
			 hstore_contains_hstore("tags", 'amenity=>restaurant,cuisine=>swiss') &rarr; True</p>
	"""  
	hstore_string = field
	key_value_list = hstore_input.split(',')
	for key_value in key_value_list: 
		[key, value] = key_value.split('=>')
		search_string = '"'+key.strip()+'"=>"'+value.strip()+'"'
		if search_string not in hstore_string:
			return False
	return True
