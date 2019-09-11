##dictionary is a combination of keys and values.
##enclosed with {}.
##syntex:- var = {"key1": "value1", "key2": "value2"}

information = {
               "cricketer": "dhoni",
               "actor": "srk",
               "rapper": "eminem"
               }

print (information)

print ("infromation")

print (information["actor"])

##print (information[1])     error:- cann't use index as number 

##print (information[actor])     error of:- ""

##print (information["dhoni"])  error :- give key data only not value

##print (information("rapper"))    error:- () dictionary object is "LIST"(mutable) not "TUPLE"(IMMUTABLE).

print (information.keys())     ##list all keys

print (information.values())    ##list all values

information["rapper"] = "raftaar"     ##Replacement value 
print (information)

information["captain"] = information.pop("cricketer")     ##Replacement Keys:- method1.) dic["newkey"]=dic.pop("oldkey")
print (information)                                       ##it creates new key nd delete old key


information["hero"] = information["actor"]      ##Replacement Keys:- method2.)
del information["actor"]
print (information)

information["singer"] = information["rapper"]   ##create new key with same value from existing key
print (information)
print ("\n")

print (len(information))


heros = {"johnwick":51, "thor":20, "spiderman":89}
print (heros["johnwick"])
## print (heros("johnwick"))    error of perenthisis
## print (heros[51])      error cnn't use number

information.update(heros)      ##update:- merge both dictionary variable
print (information)

#action = information + heros
#print (action)
