num = [2, 5, 8, 68, 56, 13, 77, 93]
for var in num:
    if var == 13:
        print ("this is the num:", var)
        break
    else:
        print ("no match")
print ("\n")


##now same programm but without unnessary "no match" by taking out "else:" from for loop

num = [2, 5, 8, 68, 56, 13, 77, 93]
for var in num:
    if var == 13:
        print ("this is the num:", var)
        break
else:
    print ("no match")
print ("\n")



#for loop with input function

num = [2, 5, 8, 68, 56, 13, 77, 93]
count = int(input("enter your num: "))
for var in num:
    if var == count:
        print ("this is your num: ", var)
        break
else:
    print ("no more match")
print ("\n")


##taking 1 nummber out from nelow list
num = [3573481865432]
score = int(input("enter your digite: "))
for i in num:
    if i == score:
        print ("we got from list: ", i)
        print ("we got this from list: ", score)
        break
else:
    print ("no more matches")      ##could not successed


####################

for i in "abhishek":
    if i == 's':
        print ("this is the shek:", i)  
        break
    print ("this is the abhishek:", i)
else:
    print ("not here")

######################
    
name = "avenger"
char = str(input("enter the charactor: "))
for a in name:
    if a == char:
        print ("this is the charactor:", a)
        break
    else:
        print ("this is the display:", a)
#else:
 #   print ("no maches")
    










    







    
