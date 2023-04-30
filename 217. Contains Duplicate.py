print("~ 217. Contains Duplicate ~")

def containsDuplicate(nums):
    myDict = {}
    for number in nums:
        print(myDict)
        if (myDict.get(number)):
            return True
        myDict[number] = 1
        print(myDict)
    return False

print(containsDuplicate([1,2,3,4]))