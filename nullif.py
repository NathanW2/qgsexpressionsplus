@qgsfunction(args='auto', group='Custom')
def nullif(argument_1, argument_2, feature, parent):
	"""
		Returns a None/NULL value if argument_1 is equal to argument_2,
		otherwise it returns argument_1 (SQL alike).
		
		<p><h4>Syntax</h4>
		nullif(<i>argument_1</i>, <i>argument_2</i>)</p>

		<p><h4>Arguments</h4>
		<i>  argument_1</i> &rarr; the first argument<br></p>
		<i>  argument_2</i> &rarr; the second argument<br></p>
		
		<p><h4>Example</h4>
		<!-- Show example of function.-->
			 nullif('hello world,'') &rarr; 'hello world'</p>
	"""  
	if argument_1 == argument_2:
		return None
	return argument_1
