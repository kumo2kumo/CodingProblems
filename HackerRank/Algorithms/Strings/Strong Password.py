#大文字小文字数字記号全部入れて合わせて6文字以上必要 in password
#あと最低何文字必要か
import re

def minimumNumber(n, password):
    # Return the minimum number of characters to make the password strong
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    count = 0

    #計算量o(4 * n?)
    # if re.search('[0-9]', password) == None:
    #     count += 1
    # if re.search('[A-Z]', password) == None:
    #     count += 1
    # if re.search('[a-z]', password) == None:
    #     count += 1
    # if any([word in special_characters for word in password]) == False:
    #     count += 1

    # 計算量o(n) flag方式
    flag = [1, 1, 1, 1]  #1 = なし、0 = あり
    for word in password:
        if word in numbers:
            flag[0] = 0
        if word in lower_case:
            flag[1] = 0
        if word in upper_case:
            flag[2] = 0
        if word in special_characters:
            flag[3] = 0
        count = sum(flag)
    #count + nが6文字未満の場合、6文字になるまでcountをかさまし
    while count + n < 6:
        count += 1
    return count

print(minimumNumber(7, 'AUzs-nV'))

