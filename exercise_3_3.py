blockTotal = 5
trialTotal = 6
block = 0
lst1 = []
lst2 = []
lst3 = []

for i in range(blockTotal):
    block += 1
    rng = range(0, trialTotal)
    for i in rng:
        if i < 4:
            condition = 'masked'
        else:
            condition = 'nonmasked'
        if i%2 != 0:
            side = 'right'
        else:
            side = 'left'
        lst1.append(str(block))
        lst2.append(condition)
        lst3.append(side)

lst1 = set(lst1)
lst2 = set(lst2)# set will erase all the repetitive stuff . . .
lst3 = set(lst3)

lst1 = list(lst1)
lst2 = list(lst2)
lst3 = list(lst3)

s = ','

for i in range(len(lst1)):
    strng = s.join([lst1[0], lst2[0], lst3[0]])
    print strng