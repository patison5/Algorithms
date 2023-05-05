# 557. [Easy] Reverse Words in a String III

def reverseWords(s):
    words = s.split(" ")
    result = ""
    for word in words:
        result += word[::-1] + " "
    return result

def reverseWords(s):
    return " ".join([word[::-1] for word in s.split(" ")])


print(reverseWords("Let's take LeetCode contest"))