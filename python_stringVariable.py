str = "AvengerAssemble"
num = 55

print (str)
print ("str")
print (str[1])    ##indexing :- number start from 0 
print (str[4:10])    ##range :- including from given number : excluding only last value
print (str[2:])   ##giving value to last value
print (str[:4])    ##from first value to second last value

print (str, "india")
print (str + "india")
print (str, num)
#print (str + num)     ##error in concatnation
print (str.upper())
print (str.lower())
print (str.swapcase())
