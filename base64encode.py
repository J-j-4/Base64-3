import math

def inttobit64(i):
	if i >= 0 and i <= 11:
		return chr(i + 46)
	elif i >= 12 and i <= 37:
		return chr(i - 12 + 65)
	elif i >= 38 and i <= 63:
		return chr(i - 38 + 97)
	else:
		return "#"
		print i

def base64encode(inte):
	output = ""
		
	for x in xrange(0, (int(math.log(inte, 64))+1)):		
		output = output + inttobit64(int(inte/(64**x)) % 64)
	
	return output[::-1]