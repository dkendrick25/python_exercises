## String split

# Implement the string split function: split(string, delimiter). Examples;
#
# split('abc,defg,hijk', ',') => ['abc', 'defg', 'hijk']
# split('JavaScript', 'a') => ['J', 'v', 'Script']
# split('JaaScript', 'a') => ['J', '', 'Script']
# split('JaaaScript', 'aa') => ['J', 'aScript']


def split(string, delim):
    newList = []
    startIndx = 0
    endIndx = string.index(delim)

    while True:
        part = string[:endIndx]
        newList.append(part)
        startIndx = endIndx + len(delim)
        string = string[startIndx:]

        if delim in string:
            endIndx = string.index(delim)
        else:
            newList.append(string)
            break
    return newList

print split("JavaScript", "a")
