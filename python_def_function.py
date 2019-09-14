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
