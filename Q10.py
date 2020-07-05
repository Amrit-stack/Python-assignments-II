def snake_case(str):
	res = [str[0].lower()] 
	for c in str[1:]:
		if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
			res.append('_') 
			res.append(c.lower()) 
		else: 
			res.append(c) 
	
	return ''.join(res) 
	
def kebab_case(str):
	res = [str[0].lower()] 
	for c in str[1:]:
		if c in ('ABCDEFGHIJKLMNOPQRSTUVWXYZ'): 
			res.append('-') 
			res.append(c.lower()) 
		else: 
			res.append(c) 
	
	return ''.join(res) 

str = input('Enter Camel Case String\n')
print(snake_case(str))
print(kebab_case(str)) 
