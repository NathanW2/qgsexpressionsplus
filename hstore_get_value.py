import re

@qgsfunction(args='auto', group='Custom')
def hstore_get_value(field, key, feature, parent):
	"""
		Given the field containing the hstore tags and a key, returns the key's value.
		
		<p><h4>Syntax</h4>
		hstore_get_value(<i>field</i>, <i>key</i>)</p>

		<p><h4>Arguments</h4>
		<i>  field</i> &rarr; name of the field containing the hstore tags (in double quotes)<br></p>
		<i>  key</i> &rarr; a key<br></p>
		
		<p><h4>Example</h4>
		<!-- Show example of function.-->
			 hstore_get_value("tags", 'amenity') &rarr; restaurant</p>
	"""  
	hstore_string = field
	reg_exp = '"'+key+'"=>"(.+?)"'
	re_output = re.search(reg_exp, hstore_string)
	if re_output:
		return re_output.group(1)
