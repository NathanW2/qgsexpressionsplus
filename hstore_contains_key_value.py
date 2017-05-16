@qgsfunction(args='auto', group='Custom')
def hstore_contains_key_value(field, key_value, feature, parent):
    """
    Does key/value exist in the hstore tags field?
    Returns True or False
    Usage example: hstore_contains_key_value("tags", 'amenity=>restaurant')
    """
    hstore_string = field
    [key, value] = key_value.split('=>')
    search_string = '"'+key.strip()+'"=>"'+value.strip()+'"' 
    return search_string in hstore_string
