#at the same location *at the same time* YES or NO
#0 4 | 4 2      2 1 | 1 1
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    #4 - 0 = 4, 1 - 4 = -3   割り切れる必要性

    #x1とx2のうち大きい方をbig_startとする
    big_start = max(x1, x2)
    start_diff = big_start - min(x1, x2)
    #big_startの方のvからもう一方のvを引いてマイナスだったら(diff)
    diff = v1 - v2 if big_start == x1 else v2 - v1
    
    if diff < 0:
        #diff_startで割り切れるか
        if start_diff % diff == 0:
            return "YES"
    return "NO"

input = input("数字を４つ入力してください\n").strip().split()
x1 = int(input[0])
v1 = int(input[1])
x2 = int(input[2])
v2 = int(input[3])

print(kangaroo(x1, v1, x2, v2))