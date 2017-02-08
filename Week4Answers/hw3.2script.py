import math

temp  = float(input("Enter a temp in C: "))

numer = 17.625 * temp
denom = temp + 243.04
exponent = numer / denom

svp = 6.1094 *  math.exp(exponent)

print('The saturated vapor pressure is for', temp,'C is ',svp)

