def saluteCount(s):
    matchCount = 0

    for i in range(len(s)):
        if (s[i] == '>'):
            """ 
            IDEA: Starting from the index where we found the current '>',
            check for the number of occurrances of '<'
            """
            matchCount += s[i:len(s)].count('<')

    return matchCount * 2

def solution(s):
    return saluteCount(s)