blockTotal = 5
trialTotal = 6
block = 0

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
        print str(block) + ", " + condition + ", " + side 
    
