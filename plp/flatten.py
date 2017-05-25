def flatten(l1, l2, depth):

    assert depth >= 0  # ensure that depth is bigger than 0 , else assertion error
    if depth == 0:
        return l1, l2 # return the lists as they are if depth is 0

    resultl1 = []
    resultl2 = []

    while depth != 0: # while loop until depth = 0
        for elements in l1:
            try:
                resultl1.extend(iter(elements)) # try to add iterate the elements contained in the element of the list (elelemts of a list can be list as well)
            except TypeError:
                resultl1.append(elements) #if element is not iterrabil , just append the element as is
        for elements in l2: # same for list number two
            try:
                resultl2.extend(iter(elements))
            except TypeError:
                resultl2.append(elements)
        depth -= 1 # decrement the depth 
        l1 = resultl1 # copy result to list for reprocesing the list again
        l2 = resultl2
        resultl1 = [] #clear the result list
        resultl2 = []
    return l1, l2
