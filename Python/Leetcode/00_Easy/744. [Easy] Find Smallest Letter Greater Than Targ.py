# 744. [Easy] Find Smallest Letter Greater Than Target


def nextGreatestLetter(letters, target):
    left = 0
    right = len(letters) - 1 
    while left <= right:
        center = (left + right) // 2
        letter = letters[center]
        letter_left = letters[center - 1]

        if letter_left <= target and target < letter:
            return letter
        if letter > target:
            right = center - 1
        else:
            left = center + 1
    return letters[0]


print(nextGreatestLetter(["c","f","j"], "a"))
print(nextGreatestLetter(["c","f","j"], "g"))
print(nextGreatestLetter(["c","f","j"], "c"))
print(nextGreatestLetter(["x","x","y","y"], "z"))
