#List is a mutable
#enclosed with []

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
print (myNameSecond+myNameOne)     ##concatnation


myNameOne[3]="john"   ##Replacement value
print (myNameOne)


myNameSecond[0] = "thor"
print (myNameSecond)

marvel = ["thor", "ironman", "cap.america"]
dc = ["superman", "batman", "aquaman"]

heros = marvel + dc   ##concatenation
print (heros)

print (marvel[1])    ##indexing

del marvel[2]   ##del :- delete the index data
print (marvel)

dc.remove("batman")         ##remove:- remove the specific data
print (dc)

marvel.append("hulk")    ##append:- add the data at last location
print (marvel)

marvel.insert(2, "cap.america")     ## insert:- add the data in specific location
print (marvel)


marvel.reverse()      ##reverse:- it reverses the data (order)location
print (marvel)


marvel.insert(1, "ironman")
print (marvel)
print ("\n")


print (marvel.count("ironman"))      ##count:- it counts the data in the string 












