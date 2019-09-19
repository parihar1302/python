## def function

## return :- shows that programme has been ended, even if you do not mention return, the programme will work

def entry():
    print ("hello")
    return
entry()

######################

def data(name):
    print ("hi dude", name)
    return
data("abhishek")

########################

def data(name):
    print ("hi dude", name)
    return
data(5)

#############################

def detail(name, email, mob):
    print ("fill the detail:-", name, email, mob)
    return
detail("abhishek", "abhi13.rjpt@gmail.com", "8722020118")

##########################

def detail(name, email, mob=8722020118):
    print ("fill the detail:-", name, email, mob)
    return
detail("abhishek", "abhi13.rjpt@gmail.com")

###########################

def abhishek():
    print ("abhishek you'r awesome man")
    return
abhishek()

########################

def info(nature):
    print ("info you are gajab", nature)
    return
info("rider")

##########################

#def detail(name, email=ab@gmail.com, mob):
#    print ("detail is:", name, email, mob)   errro
#    return
#detail("abhishek", "898989898")     


def detail(name, email, num):
    print ("enter name:-", name)
    print ("enter email:-", email)
    print ("enter num:-", num)
    return
detail("ab", "ab@gmail.com", "1302")

###########################################

def skore(num=89):      ##can give the value here also
    print ("this is he:-", num)
    return
skore()

######################################3
##def_advance

def count(num1, num2):      #method-1.)   addition
    total = num1 + num2
    print ("sum is :-", total)
    return
count(5, 3)

###########################

def count(num1, num2):      #method-2.)   addition
    total = num1 + num2
    return total
print (count(6, 7))

######################################

def count(*num):          ## method-1.)  addition multi num
    total = 0
    for a in num:
        total = total + a
        print (total)
    return
count(3, 2, 5, 10, 1)

#######################################

def count(*num):       ## method-2.) addition multi num
    total = 0
    for a in num:
        total = total + a
    print (total)
    return
count(3, 2, 5, 10, 1)

#######################################

def count(*num):
    total = 0
    for a in num:
        if a < 50:
            total = total + a
            print ("this exceptable:-", total)
    else:
        print ("total not exceptable", total)
count(2, 6, 10, 5, 20, 8, 15, 30, 49, 50)

#################################################

def score(*num):
    total = 0
    for i in num:
        if i < 27:
            total = total + i
            print ("need more", total)
            continue
    else:
        print ("we got", total)
score(3, 2, 8, 2, 10, 13, 15, 7,)










































