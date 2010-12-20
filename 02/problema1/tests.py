import roman

def testDigitosRomanos():
	assert roman.Roman2Decimal('I') == 1
	assert roman.Roman2Decimal('V') == 5
	assert roman.Roman2Decimal('X') == 10
	assert roman.Roman2Decimal('L') == 50	
	assert roman.Roman2Decimal('C') == 100	
	assert roman.Roman2Decimal('D') == 500
	assert roman.Roman2Decimal('M') == 1000	

def testDigitosRomanosDeAlgarismosIguais():
	assert roman.Roman2Decimal('II') == 2
	assert roman.Roman2Decimal('XX') == 20
	assert roman.Roman2Decimal('CCC') == 300
	
def testDigitosRomanosDeAlgarismosDiferentes():
	assert roman.Roman2Decimal('XI') == 11, roman.Roman2Decimal('XI')
	assert roman.Roman2Decimal('CI') == 101
	assert roman.Roman2Decimal('MCCLXXII') == 1272
	
def testDigitosRomanosComAlgarismoInvertido():
	assert roman.Roman2Decimal('IX') == 9,roman.Roman2Decimal('IX')
	assert roman.Roman2Decimal('CXIX') == 119, roman.Roman2Decimal('CXIX')
	assert roman.Roman2Decimal('XCIX') == 99, roman.Roman2Decimal('XCIX')
	assert roman.Roman2Decimal('CCCXCIX') == 399
	
	