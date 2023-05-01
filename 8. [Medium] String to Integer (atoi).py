# 8. String to Integer (atoi)

def isWhitelisted(char):
    whitelist = ["0","1","2","3","4","5","6","7","8","9","-"]
    return char in whitelist

def myAtoi(s):
    """
    :type s: str
    :rtype: int
    """
    isNegative = False
    number = 0

    for idx, char in enumerate(s):
        if not isWhitelisted(char):
            continue
        if char == "-" and idx < len(s) - 1 and isWhitelisted(s[idx+1]):
            isNegative = True
        else:
            number = number * 10 + int(char)
    return number if not isNegative else number * -1




tests = [
    {
        'input': "42",
        'answer': 42
    },
    {
        'input': "words and 987",
        'answer': 987
    }
]
print("\n\nTESTING\n")
for test in tests:
    result = myAtoi(test['input'])
    isPassed = result == test['answer']
    if (isPassed):
        print("Passed")
    else:
        print("\n------")
        print("Not passed. Exprected: ", test['answer'], " recieved: ", result) 
        print("\n------")