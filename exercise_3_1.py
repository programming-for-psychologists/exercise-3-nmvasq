def repetition(letters, numberBeforeSwitch, numRepetitions):
    for rep in range(numRepetitions):
        for i in range(numberBeforeSwitch):
            print letters[0]
        for i in range(numberBeforeSwitch):
            print letters[1]
            
repetition(['A','B'], 3, 2)