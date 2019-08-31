## continue keyword

name = "captainamerica"
for i in name:
    if i == "a":  
        print ("termnate this: ", i)
        continue    ##continue keyword remove charactor from variable value
    else:
        print("print rest char: ", i)
print ("\n")


### Pass keyword

name = "captainamerica"
for i in name:
    if i == 'a':
        print ("pass this value:", i)
        pass       ##just pass the value
    else:
        print ("rest value is:", i)
