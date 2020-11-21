# py-roman-numbers

This package can be used to convert integers to roman numbers and vice versa.

2 Functions are available for use:

1) intToRoman(integer) => String

2) romanToInt(roman) => Integer

# 1) Integer to Roman Number:
Function call: intToRom(1232)

Return Value : 'MCCXXXII' string
- while calling the Function, both integer and string are supported as parameters. 
  intToRoman(1232) and intToRoman('1232'), both returns 'MCCXXXII'
 
# 2) Roman to Integer Number:
Function call: romanToInt('MCCXXXII')

Return Value : 1232 integer

- While Calling the function, the parameter is not case-sensitive. 
  romanToInt('MCCXXXII') and romanToInt('mccxxxii'), both returns 1232
