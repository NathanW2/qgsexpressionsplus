"""
nullif() - Returns a None/NULL value if argument_1 equals to argument_2, 
otherwise it returns argument_1 (SQL alike).
Usage e.g.: coalesce(nullif("name",''), nullif("name_en",''), 'unknown')
"""

@qgsfunction(args='auto', group='Custom')
def nullif(argument_1, argument_2, feature, parent):
    if argument_1 == argument_2:
        return None
    return argument_1
