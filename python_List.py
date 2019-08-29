myNameOne = [56, 7.9, "Robert", 3, "Jr"]
myNameSecond = [36, "downy", 5.2, 2]

print (myNameOne) 
print (myNameSecond)

print (myNameOne[2])          ##indexing
print (myNameSecond[3])


print (myNameOne[1:4])
print (myNameSecond[:3])
print (myNameOne[0:])

print (myNameOne*2)
print (myNameSecond+myNameOne)  ##concatnation


myNameOne[3]="john"   ##Replacement value
print (myNameOne)


myNameSecond[0] = "thor"
print (myNameSecond)
