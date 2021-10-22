#s文の単語数を返す
import re

def camelcase(s):
    #use re
    # upper_char = re.findall('[A-Z]', s)
    # return len(upper_char) + 1

    #n
    count = 1
    for cha in s:
        if cha.isupper():
            count += 1
    return count

s = input()
print(camelcase(s))