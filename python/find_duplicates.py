def find_duplicates_nested_loop(l: list) -> list:
    returnList = []
    for i in range(len(l)):
        for j in range(len(l) - i - 1):
            if (l[i] == l[i + j + 1]):
                if (not(returnList.__contains__(l[i]))):
                    returnList.append(l[i])
                # This is awful but it works.
    return returnList

def find_duplicates_dict(l: list) -> list:
    tempDict = {}
    returnList = []
    for x in l:
        dictSize = len(tempDict)
        tempDict[x] = x
        if (len(tempDict) == dictSize):
            if (not(returnList.__contains__(x))): 
                returnList.append(x)
            #Again this is awful but I hate seeing dupes
    return returnList

    

if __name__ == "__main__":
    sample1 = [3, 7, 5, 6, 7, 4, 8, 5, 7, 66]
    sample2 = [3, 5, 6, 4, 4, 5, 66, 6, 7, 6]
    sample3 = [3, 0, 5, 1, 0]
    sample4 = [3]
    
    print("Sample 1:", find_duplicates_dict(sample1))
    print("Sample 2:", find_duplicates_nested_loop(sample2))
    print("Sample 3:", find_duplicates_nested_loop(sample3))
    print("Sample 4:", find_duplicates_nested_loop(sample4))