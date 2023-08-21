array1 = ["ada","burak","ahmet","deified","car","rotator"]
def myFunction(array1):
    array2 = []
    for word in array1:
        nonReverse = word
        reverse=word[::-1]
        if nonReverse == reverse:
            array2.append(nonReverse)
    return array2
