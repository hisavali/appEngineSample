def rot13(client_str):
	if client_str:
		output=[]
		for c in client_str:
			print 'Processing character %s' %c
			if c.isalpha():
				if ord(c) in range(ord('a'),ord('m')+1):
					c = chr(ord(c) + 13)
				elif ord(c) in range(ord('A'),ord('M')+1):
					c = chr(ord(c) + 13)
				elif ord(c) in range(ord('n'),ord('z')+1):
					c = chr(ord(c) - 13)
				elif ord(c) in range(ord('N'),ord('Z')+1):
					c = chr(ord(c) - 13)
			
			output.append(c)
	return ''.join(output)


print rot13("H&^%£$\"\"")