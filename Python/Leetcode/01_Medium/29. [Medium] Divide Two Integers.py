# 29. [Medium] Divide Two Integers

def divide(dividend, divisor):
    """
    :type dividend: int
    :type divisor: int
    :rtype: int
    """
    isNegative = ((dividend < 0) and (divisor > 0)) or ((divisor < 0) and (dividend > 0))
    div = 1 if not isNegative else -1

    result = 0

    if (divisor == 0):
        return 0
    
    if (dividend == divisor):
        return 1

    while abs(result * divisor) < abs(dividend):
        result += 1

    if result * abs(divisor) > abs(dividend):
        return (result - 1) * div

    return result * div


tests = [
    {
        'input1': 0,
        'input2': 0,
        'answer': 0
    },
    {
        'input1': 1,
        'input2': 1,
        'answer': 1
    },
    {
        'input1': 0,
        'input2': 1,
        'answer': 0
    },
    {
        'input1': 2,
        'input2': 1,
        'answer': 2
    },
    {
        'input1': 1,
        'input2': 2,
        'answer': 0
    },
    {
        'input1': 2,
        'input2': -2,
        'answer': -1
    },
    {
        'input1': -2,
        'input2': 2,
        'answer': -1
    },
    {
        'input1': -2,
        'input2': -2,
        'answer': 1
    },
    {
        'input1': -15,
        'input2': -2,
        'answer': 7
    }
]
print("\n\nTESTING\n")
for test in tests:
    result = divide(test['input1'], test['input2'])
    isPassed = result == test['answer']
    if (isPassed):
        print("Passed")
    else:
        print("\n------")
        print("Not passed. Exprected: ", [test['input1'], test['input2']], test['answer'], " recieved: ", result) 
        print("\n------")