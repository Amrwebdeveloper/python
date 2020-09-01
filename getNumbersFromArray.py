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



# How to use...

testArarry = [56485,35.5,(410),('sdf','asd',34),'Amr',('wer',45.985),(452,'word'),23,{'aaa':123,'bbb':456}]

getNumbers(testArarry)