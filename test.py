print (1, 7)

numone = [10, 45, "abhishek", 78, 67]
numtwo = [2, 5, 38, 58, "singh", 99]

print (numone)
print (numtwo[3])
print (numone[1:4])
numtwo[4] = "parihar"
print (numtwo)

print ("\n")
#####list ends



numone = (10, 45, "abhishek", 78, 67)
numtwo = (2, 5, 38, 58, "singh", 99)

print (numone)
print (numtwo[3])
print (numone[1:4])
# error :- numtwo[4] = "parihar"    tuple is immutable
print (numtwo)
print ("\n")
#######tuple ends


data = {"thor":"hammer",
        "ironman":"armor",
        "captainamerica":"shield",
        "batman":"batmobil"
        }
print (data)
print (data["thor"])
print (data.keys())
print (data.values())
data["armor"] = "archreactor"
print (data)
data["thor"] = "stormbreaker"
print (data)
data["thanos"] = data["thor"]
print (data)
data["warmachine"] = data.pop("ironman")
print (data)
print ("\n")
###dictionary ends


num = 100
if num > 50:
    print ("num is less")
else:
    print ("num is greater")
print ("this is end here")

print ("\n")

score = int(input("enter the num: "))
if score < 50:
    print ("num is less")
else:
    print ("num is greater")
print ("\n")
###if_else_condition


num = 1
while num <10:
    print ("add 1 more: ", num)
    num = 1 + num
print ("this is an end")
print ("\n")


score = int(input("enter the value: "))
while score >= 10:
    print (thisscore)
    score = 1 + score
print ("here ends")
print ("\n")

score = int(input("enter the value: "))
while score >= 10:
    print (thisscore)
    score = 1 + score
print ("here ends")
print ("\n")


num = 5
while num < 100:
    print (num)
    num = 5 + num
print ("end")
print ("\n")
####while loop ends here

print (range(0, 10))
print (list(range(0, 20)))
print (list(range(2, 20, 3)))

num = list(range(0, 10))
for a in num:
    print (a)
    print (num)

print ("\n")

count = range(1, 10, 3)
for i in count:
    print (i)
print ("\n")  
count = range(1, 30, 6)
for i in count:
    print (count)
print ("\n")

name = "abhishek"
for i in name:
    print (name)
print ("\n")

num = (10, 3 , 6, 98, 13, 5, 56)
score = int(input("enter the value:-"))
for i in num:
    if i == score:
        print ("this is the num: ", score)
        break
    else:
        print ("this value not")
print ("not here")
print ("\n")

num = (10, 3 , 6, 98, 13, 5, 56)
score = int(input("enter the value:-"))
for i in num:
    if i == score:
        print ("this is the num: ", score)
        continue
    else:
        print ("this value not")
print ("not here")





