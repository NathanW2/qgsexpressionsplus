@qgsfunction(args='auto', group='Custom')
def hstore_contains_hstore(field, hstore_input, feature, parent):
    """
    Does hstore tags field contain all the keys and values in the hstore_input?
    Returns True or False
    Usage example: hstore_contains_hstore("tags", 'amenity=>restaurant,cuisine=>swiss')
    """
    hstore_string = field
    key_value_list = hstore_input.split(',')
    for key_value in key_value_list: 
        [key, value] = key_value.split('=>')
        search_string = '"'+key.strip()+'"=>"'+value.strip()+'"'
        if search_string not in hstore_string:
            return False
    return True
