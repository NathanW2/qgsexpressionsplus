import re

@qgsfunction(args='auto', group='Custom')
def hstore_get_value(field, key, feature, parent):
    """
    Give the field containing the hstore tags and a key return the key's value.
    If the key does not exist, return null
    Usage example: hstore_get_value("tags", 'amenity')
    """
    hstore_string = field
    reg_exp = '"'+key+'"=>"(.+?)"'
    re_output = re.search(reg_exp, hstore_string)
    if re_output:
    	return re_output.group(1)
