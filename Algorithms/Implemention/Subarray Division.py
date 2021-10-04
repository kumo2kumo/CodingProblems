"""
input 
5
s = 1 2 1 3 2 *1<=s[i]<=5
day = sum = 3, month = length = 2
隣り合ったmonth個を足したらdayになる組み合わせが何個あるか
"""
def birthday(s, d, m):
    #start, start + start+1と隣り合わせをm個足していき、sumと合えばcount更新
    count = 0
    # スライスの利用
    for i in range(len(s) - m + 1): #i = 0,3          0,1,2
        if sum(s[i:i+m]) == d:
            count += 1
    return count

    #内包表記使う場合
    # return len([1 for i in range(len(s)-m+1) if sum(s[i:i+m]) == d])


s = list(map(int, input().strip().split()))
input = input().rstrip().split()
d = int(input[0])
m = int(input[1])
print(birthday(s, d, m))


