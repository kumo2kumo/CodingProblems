#return an array that indicates appearing twice in array nums
#input nums = [4,3,2,7,8,2,3,1], return [2,3]
from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    # *O(n)search* dicを作り、keyにnumsの数字、valueに出てきた回数を記録
    dic = {}
    for i in range(len(nums)):
        if nums[i] not in dic:
            dic[nums[i]] = 1
        else:
            dic[nums[i]] += 1

    return [twice for twice in dic if dic[twice] == 2]

nums = [4,3,2,7,8,2,3,1]
print(findDuplicates(nums))
