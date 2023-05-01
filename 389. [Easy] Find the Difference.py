# 389. Find the Difference

def findTheDifference(s, t):
    """
    :type s: str
    :type t: str
    :rtype: str
    """
    ascii_result = 0
    s_length = max(len(s), len(t))
    for idx in range(0, s_length):
        if idx < len(s):
            ascii_result += ord(s[idx])
        if idx < len(t):
            ascii_result -= ord(t[idx])
    return chr(abs(ascii_result))


tests = [
    {
        'line1': "abcd",
        'line2': "abcde",
        'answer': "e"
    },
    {
        'line1': "",
        'line2': "y",
        'answer': "y"
    }
]
print("\n\nTESTING\n")
for test in tests:
    result = findTheDifference(test['line1'], test['line2'])
    isPassed = result == test['answer']
    if (isPassed):
        print("Passed")
    else:
        print("\n------")
        print("Not passed. Exprected: ", test['answer'], " recieved: ", result) 
        print("\n------")