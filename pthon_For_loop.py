# Range function

print (range(0, 5))

print (list(range(0, 5)))

print (list(range(2, 20, 3)))
                  #   #  #
              #start end differnce#

print (list(range(3, 31, 3)))     #3's table


#######################

num = list(range(0, 10))
for score in num:
    print (score)
    

###########################

count = range(0, 10, 2)
for test in count:
    print (test)

######################

num = list(range(0, 10))
for score in num:
    print (score, end=",")          #end function for single line

print ("\n")      ##\n for new line
###################################


name = "ABHISHEK"
for i in name:
    print (i)
    
###########################
    
name = "ABHISHEK"
for a in name:
    print (a, end=",")
print ("\n")

