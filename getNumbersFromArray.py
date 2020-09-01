def getNumbers(array):
    numbersArray = []
    for n in array:
        if type(n) == int or type(n) == float:
            numbersArray.append (n)
        elif type(n) == tuple:
            for index,anyThing in enumerate(n):
                if type(n[index]) == int or type(n[index]) == float:
                    numbersArray.append(n[index])
        elif type(n) == dict:
            for x, y in n.items():
                if type(x) == int or type(x) == float:
                    numbersArray.append (x)
                if type(y) == int or type(y) == float:
                    numbersArray.append (y)
    return numbersArray