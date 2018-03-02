def bit64toint(char):
	if ord(char) > 45 and ord(char) < 58:
		return ord(char) - 46
	elif ord(char) > 64 and ord(char) < 91:
		return ord(char) + 12 + (0 - 65)
	elif ord(char) > 96 and ord(char) < 123:
		return ord(char) + 38 + (0 - 97)
	else:
		return -1

def base64decode(strinput, c):
	total = 0	
	stri = strinput[::-1]	
		
	for x in xrange(c, len(stri)):	
		total = total + (64**(x-c))*(bit64toint(stri[x]))
	
	return total

print base64decode("TisIsDKee", 0)