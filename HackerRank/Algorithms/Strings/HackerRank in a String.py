#sの中に'hackerrank'が含まれているか、return YES or NO
def hackerrankInString(s):
    keyword = "hackerrank"
    for word in keyword:
        index = s.find(word)
        if index == -1:
            return 'NO'
        s = s[index+1:]
    return 'YES'


    # def helper(word, s):
    #     for i in range(len(s)):
    #         if s[i] == word:
    #             s = s[i+1:]
    #         else:
    #             return 'NO'

    # for word in 'hackerrank':
    #     helper(word, s)
    # return 'YES'

print(hackerrankInString('rhbaasdndfsdskgbfefdbrsdfhuyatrjtcrtyytktjjt'))
