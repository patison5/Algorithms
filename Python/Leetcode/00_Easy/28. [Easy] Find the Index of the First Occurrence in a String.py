# 28. Find the Index of the First Occurrence in a String

def strStr(haystack, needle):
    for idx, el in enumerate(haystack):
        is_substring = True
        for sub_idx, sub_el in enumerate(needle):
            if idx + sub_idx >= len(haystack):
                is_substring = False
                break

            if sub_el != haystack[idx + sub_idx]:
                is_substring = False
                break
        if is_substring:
            return idx
    return -1

print(strStr("sadbutsad", "sad"))