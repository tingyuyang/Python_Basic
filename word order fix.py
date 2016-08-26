#so basically s[i]<s[i-1], the second letter should not be bigger than the first one, and so on. print out the length till the loop stop.

def alphabetical(s):
	i=1
	found = False
	if (len(s)==0):
		return 0
	if len(s)==1:
		return 1
	else:
		while i<len(s) and found==False:
			if s[i]<s[i-1]:
				found = True
			else:
				i = i +1
	return i
print(alphabetical('ransom')) #output is 1, coz r>1...
