""" Custom Python expression functions for searching for specific keys and
values in the hstore attribute. """

from qgis.core import *
from qgis.gui import *


@qgsfunction(args='auto', group='Custom')
def hstore_get_value(hstore_attr, key, feature, parent):
    """
    Given a key, return the value from hstore_attr
    If the key does not exist, return null
    Usage example: hstore_get_value('other_tags', 'tourism')
    """

    hstore_string = feature[hstore_attr]
    hstore_dict = hstore_to_dict(hstore_string)
    if key in hstore_dict.keys():
        return hstore_dict[key]
    else:
        return ""


@qgsfunction(args='auto', group='Custom')
def hstore_exist(hstore_attr, key, feature, parent):
    """
    Does the given key exist in hstore_attr?
    Returns True or False
    Usage example: hstore_exist('other_tags', 'tourism')
    """

    hstore_string = feature[hstore_attr]
    hstore_dict = hstore_to_dict(hstore_string)
    return key in hstore_dict.keys()


@qgsfunction(args='auto', group='Custom', usesgeometry=True)
def hstore_contains_key_value(hstore_attr, key_value, feature, parent):
    """
    Does key/value exist in hstore_attr?
    Returns True or False
    Usage example: hstore_contains_key_value('other_tags', 'tourism=>information')
    """

    hstore_string = feature[hstore_attr]
    hstore_dict = hstore_to_dict(hstore_string)
    # Remove all spaces from key_value, if any
    key_value.replace(" ", "")
    [key, value] = key_value.split("=>")
    # Remove surrounding double quotes from the key and value, if any
    key = key.strip('"')
    value = value.strip('"')
    return key in hstore_dict.keys() and hstore_dict[key] == value


@qgsfunction(args='auto', group='Custom')
def hstore_contains_hstore(hstore_attr, hstore_input_string, feature, parent):
    """
    Does hstore_attr contain hstore_string?
    Returns True or False
    Usage example:
    hstore_contains_hstore('other_tags', '"tourism"=>"information","information"=>"guidepost"')
    OR (no double quotes for keys and values)
    hstore_contains_hstore('other_tags', 'tourism=>information,information=>guidepost')
    """

    hstore_attr_string = feature[hstore_attr]
    hstore_attr_dict = hstore_to_dict(hstore_attr_string)
    # Remove all spaces from hstore_input_string, if any
    hstore_input_string = hstore_input_string.replace(" ", "")
    hstore_input_dict = hstore_to_dict(hstore_input_string)
    '''
    If a key in the input hstore is not present in hstore attribute
    or if the key is present, but the value is different, return False
    '''
    for key in hstore_input_dict.keys():
        if key not in hstore_attr_dict.keys() or hstore_input_dict[key] != \
                hstore_attr_dict[key]:
            return False
    return True


def hstore_to_dict(hstore_string):
    """ Accepts an hstore string and returns a dict """

    hstore_list = hstore_string.split(",")
    hstore_dict = dict()
    for item in hstore_list:
        [key, value] = item.split("=>")
        # Remove surrounding double quotes from the key and value, if any
        key = key.strip('"')
        value = value.strip('"')
        hstore_dict[key] = value
    return hstore_dict
