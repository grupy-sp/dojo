digits = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000 }

def Roman2Decimal(roman):
	total = 0
	lastLetter = roman[-1]
	roman = list(roman)
	roman.reverse()
	 
	for letter in roman:
		if digits[lastLetter] <= digits[letter]:
	  	    total += digits[letter]
		else:
			total -= digits[letter]
		lastLetter = letter
	return total