@qgsfunction(args='auto', group='Custom')
def hstore_exist(field, key, feature, parent):
    """
    Does key exist in the hstore tags field?
    Returns True or False
    Usage example: hstore_exists("tags", 'amenity')
    """
    hstore_string = field
    search_string = '"'+key+'"=>' 
    return search_string in hstore_string
