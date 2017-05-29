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


def flatten_one_list(l, depth):
    result = []
    while depth > 0:
        for element in l:
            if isinstance(element, (list, tuple)):
                result.extend(element)
            else:
                result.append(element)
        l = result
        result = []
        depth -= 1
    return l

#this function has a problem I cannot see
def flatten_one_list_without_while(l, depth):
    result = []
    for element in l:
        if isinstance(element, (list, tuple)):
            result.extend(element)
        else:
            result.append(element)
    l = result # l in this scope points to the flatten list, other l's in other scopes are not affected
    if depth > 1:
        flatten_one_list_without_while(l, depth - 1)
        # the list is not returned. A new list is created with flattened elements, but
        # the list that is received as an argument is never altered
    return l

def flatten_after_feedback(l1, l2, depth):
    if depth == 0:
        return l1, l2
    dp = depth
    # same as:
    # return flatten_one_list(l1, depth), flatten_one_list(l2, depth=dp)
    return flatten_one_list(l1, dp), flatten_one_list(l2, dp)
