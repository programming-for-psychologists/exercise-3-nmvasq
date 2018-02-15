blockTotal = 5
trialTotal = 12
block = 0

for i in range(blockTotal):
    block += 1
    conShuffle = set(range(0, trialTotal))
    sideShuffle = set(range(0, trialTotal))
    for i in conShuffle:
        if i%3 == 0:
            condition = 'masked'
        else:
            condition = 'nonmasked'
    for i in sideShuffle:
        if i%2 == 0:
            side = 'right'
        else:
            side = 'left'
        print str(block) + ", " + condition + ", " + side 
    
