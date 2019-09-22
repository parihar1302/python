def count(*num):
    total=0
    for i in num:
        if i <= 50:
            print ("this is total:-", total)
            total = total + i
    else:
        print ("this is not:", total)
        return
count(2, 5, 7, 10, 5, 7, 3, 10, 1, 2)
