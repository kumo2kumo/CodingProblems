#return the bitwise AND of all numbers between left and right
# left = 5, right = 7 output = 4
'''
どこかの数字が0を持っているとその位は0になる
右から０か１が追加されていくから、隣り合う数の一番右は絶対違う数字になる
一緒の数になるまで右ビットシフトさせる→シフトした回数分左ビットシフトさせる
'''
left = 5
right = 7

def rangeBitwiseAnd(left: int, right: int) -> int:   
    count = 0
    while left != right:
        left >>= 1 #bin(left)にしなくてもいいのか…
        print(left)
        right >>= 1
        count += 1
    left <<= count
    return left

#time limit exceed
# left = 5
# right = 7
# base_bit = int(format(left, 'b'))
# for num in range(left + 1, right + 1): #6, 7
#     bit_int = int(format(num, 'b'))
#     base_bit = base_bit & bit_int
# print(int(str(base_bit), 2))    

