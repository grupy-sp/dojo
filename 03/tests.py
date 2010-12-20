import bowl

def testSimples():
	soma = bowl.CalcularPlacar("9-9-9-9-9-9-9-9-9-9-")
	assert soma == 90, soma
	
def testSimples2():
	soma = bowl.CalcularPlacar("1-2-3-4-5-6-7-8-9---")
	assert soma == 45, soma
	
def testSemCanaleta():
	soma = bowl.CalcularPlacar("81818181818181818181")
	assert soma == 90, soma
	
def testSpare():
	soma = bowl.CalcularPlacar("8/818181818181818181")
	assert soma == 99, soma
	
def testSpare2():
	soma = bowl.CalcularPlacar('8/718181818181818181')
	assert soma == 97, soma

def testSpare3():
	soma = bowl.CalcularPlacar('8/71815/818181818181')
	assert soma == 106, soma

def testUltimoSpare():
	soma = bowl.CalcularPlacar('8/71815/81818181818/8')
	assert soma == 115, soma
	
#def testTudoSpare():
#	soma = bowl.CalcularPlacar('8/8/8/8/8/8/8/8/8/8/8')
#	assert soma == 180, soma
	
def testStrike():
	soma = bowl.CalcularPlacar('X818181818181818181')
	assert soma == 100, soma 
	
#def testStrike2():
#	soma = bowl.CalcularPlacar('X8181818181818181XXX')
#	assert soma == 121, soma
	
#def testTudoStrike():
#	soma = bowl.CalcularPlacar('XXXXXXXXXXXX')
#	assert soma == 300, soma