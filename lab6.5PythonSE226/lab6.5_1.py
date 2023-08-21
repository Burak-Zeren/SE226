array1 = [1,15,48,96,2,5,6,75]
array2 = [2,45,7,15,23,68,48,5]
def myFunction(array1,array2):
    array3 = []
    for a1 in array1:
        for a2 in array2:
            if a1 == a2:
                array3.append(a1)
    return array3

