#binary search
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num: int) -> int:
def guessNumber(n: int) -> int:
    lo, hi = 1, n
    while True:
        mid = (lo + hi) // 2
        if guess(mid) == 0:
            return mid
        if guess(mid) == -1:
            hi = mid - 1
        if guess(mid) == 1:
            lo = mid + 1

    #ややこしく考えすぎ↓
    # num_range = [i for i in range(1, n + 1)]
    # while True:
    #     half_index =  (len(num_range) // 2) - 1
    #     if guess(num_range[half_index]) == 0:
    #         return num_range[half_index]
    #     if guess(num_range[half_index]) == -1:
    #         num_range = num_range[:half_index]
    #     if guess(num_range[half_index]) == 1:
    #         num_range = num_range[half_index + 1:]

#nの範囲を狭めないと…
    # def half_search(n: int, num_range) -> int:
    #     half = n // 2
    #     if guess(half) == 0:
    #         return half
    #     if guess(half) == -1:
    #         num_range = [:half]
    #         half = half // 2
    #         half_search(half, num_range)
    #     if guess(half) == 1:
    #         num_range = [half + 1:]
    #         half =  n - (half + 1) // 2 + (half + 1)


    


