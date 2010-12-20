import pdb

romans = {1: 'I', 5: 'V', 10: 'X', 50: 'L', 100: 'C', 500: 'D', 1000: 'M', 5000: '~V'}
anteriores = {1 : 0, 5 : 1, 10 : 1, 50 : 10, 100 : 10, 500 : 100, 1000 : 100, 5000 : 1000}

numbers = romans.keys()
numbers.sort()
numbers.reverse()

def decimal2roman(decimal):
    if decimal in romans:
        return [romans[decimal]]
    
    roman_digits = []
    for number in numbers:
      
        if decimal >= number:
            decimal -= number
            roman_digits.append(romans[number])
            roman_digits.extend(decimal2roman(decimal))
            break
            
        if decimal >= number - anteriores[number]:
            decimal -= number - anteriores[number]
            roman_digits.extend([romans[anteriores[number]],romans[number]])
            roman_digits.extend(decimal2roman(decimal))
            break
        
    return roman_digits
    