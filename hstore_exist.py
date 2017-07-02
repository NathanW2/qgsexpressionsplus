@qgsfunction(args='auto', group='Custom')
def hstore_exist(field, key, feature, parent):
	"""
		Returns True if the input key exists in the hstore tags field. False otherwise.
		
		<p><h4>Syntax</h4>
		hstore_exist(<i>field</i>, <i>key</i>)</p>

		<p><h4>Arguments</h4>
		<i>  field</i> &rarr; name of the field containing the hstore tags (in double quotes)<br></p>
		<i>  key</i> &rarr; the key to search<br></p>
		
		<p><h4>Example</h4>
		<!-- Show example of function.-->
			 hstore_exists("tags", 'amenity') &rarr; True</p>
	"""  
	hstore_string = field
	search_string = '"'+key+'"=>' 
	return search_string in hstore_string
