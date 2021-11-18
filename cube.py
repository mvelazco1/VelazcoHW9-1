#cube.py

#computes all odd number 0 to 19 and print cube.
#when even, iy prints out just number

def cb(x):
    for i in range(1,20):
        if i % 2 != 0:
            f = i ** 2
            print "odd num:", i, "value", f
        else:
            f = i
            print "even num:", i,"value", f
print
cb(20)
