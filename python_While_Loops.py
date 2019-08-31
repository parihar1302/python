#while loop simple programme

num = 1
while num < 10:
    print ("add 1 more: ", num)
    num = 1 + num
    
print ("this is an end of while loop")

########################

#while loop with input function

num = int(input("enter your num: "))
while num <= 10:
    print (num)
    num = 1 + num
print ("perfect")


###########################

#(infinite loop)

num = 5
while num < 10:
    print("this is an infinite loop: ", num)
