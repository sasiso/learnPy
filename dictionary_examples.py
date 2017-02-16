test = {}

test[1] = "A"
test[2] = "B"
test[3] = "C"
test[4] = "D"
test[5] = "E"

for k, v in test.iteritems():
    print k, v


for k in test.itervalues():
    print k

for k in test.iterkeys():
    print k

