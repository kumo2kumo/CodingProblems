#TODO チラ見
from typing import List, Optional

#preorder traversalは親→left->rightと表示されている
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Input: preorder = [8,5,1,7,10,12]
# Output: [8,5,10,1,7,null,12]
#left < root < right
#[0]より大きい数字を探す=right
#そこまでが、全部leftということ
#その中でまたright, leftを配置
# class Solution:
preorder = [8,5,1,7,10,12]

def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    if not preorder:
        return None

    root = TreeNode(preorder[0])
    i = 1
    #preorder[0]の右子が出るまでiを探す
    while i < len(preorder) and preorder[i] < root.val:
        i += 1
    #左木の一番左葉まで
    root.left = bstFromPreorder(preorder[1:i])
    #左木の一番右葉まで
    root.right = bstFromPreorder(preorder[i:])
    # print(root)
    return root

'''
34行目の結果
preorder = [8,5,1,7,10,12]
TreeNode{val: 1, left: None, right: None}
TreeNode{val: 7, left: None, right: None}
TreeNode{val: 5, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}
TreeNode{val: 12, left: None, right: None}
TreeNode{val: 10, left: None, right: TreeNode{val: 12, left: None, right: None}}
TreeNode{val: 8, left: TreeNode{val: 5, left: TreeNode{val: 1, left: None, right: None}, right: TreeNode{val: 7, left: None, right: None}}, right: TreeNode{val: 10, left: None, right: TreeNode{val: 12, left: None, right: None}}}
'''
