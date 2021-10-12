#TODO: 未！！！！
#word[0]がbaseにあるか、あるなら位置把握=board[i][j]
#word[1]がboard[i][j]の各々の+1 or -1にあるかsearch =>繰り返し
#全部通ったらtrue, だめならfalse

from typing import List

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"

#再帰を使う
def exist(self, board, word):
        for i in range(len(board)): #iは列
            for j in range(len(board[0])): #jはカラム
                if self.dfs(board, word, i, j):
                    return 'true'
        return 'false'

#Gで、vからたどることの出来る頂点の内、まだ訪問していない頂点を全て訪問する P221大槻本
# =>boardで i, jから辿ることのできる頂点の内、まだ訪問していない頂点をすべて訪問する
def dfs(self, board, word, i, j):
    if word[0] == board[i][j]:
        #次のwordがなかったら終わり
        if not word[1:]:
            return 'true'
        
        board[i][j] = "#" #訪問済みにする
        
        # next_point = [i + 1][j], [i - 1][j], [i][j + 1], [i][j - 1]
        #rangeに注意して4方向を調べる
        if i < len(board) - 1 and self.dfs(board, word[1:], i+1, j):
            return 'true'
        if i > 0  and self.dfs(board, word[1:], i-1, j):
            return 'true'
        if j < len(board[0]) - 1 and self.dfs(board, word[1:], i, j+1):
            return 'true'
        if j < 0 and self.dfs(board, word[1:], i, j-1):
            return 'true'
        board[i][j] = word[0]
        return 'false'
        
    # 次のポイントとword文字が一致しなければ終わり
    else:
        return 'false'




#解答
def exist(self, board, word):
    if not board:
        return False
    for i in range(len(board)):
        for j in range(len(board[0])):
            if self.dfs(board, i, j, word): #i=0, j=0
                return True
    return False

# check whether can find word, start at (i,j) position    
def dfs(self, board, i, j, word):
    if len(word) == 0: # all the characters are checked
        return True
    if i<0 or i>=len(board) or j<0 or j>=len(board[0]) or word[0]!=board[i][j]:
        return False
    board[i][j] = "#"  # avoid visit agian 

    # check whether can find "word" along one direction, 
    # return bool
    res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])

    board[i][j] = word[0] #tmp:str
    return res

    


# def exist(board: List[List[str]], word: str) -> bool:

#     for i in range(len(board)): #iは列
#         for j in range(len(board[0])): #jはカラム
#             if word[0] == board[i][j]:
#                 board[i][j] = "#" #使われたところを空白にする
                
#                 # wordの二文字目以降の場所を把握
#                 for w in range(1, len(word)):
#                     if i + 1 <= len(board) - 1:
#                         next_pos = board[i + 1][j]
#                         if word[w] == next_pos and next_pos != "#":
#                             i += 1
#                             next_pos = "#"
#                         else:
#                             return 'false'
#                     elif i - 1 >= 0:
#                         next_pos = board[i - 1][j]
#                         if word[w] == next_pos and next_pos != "#":
#                             i -= 1
#                             next_pos = "#"
#                         else:
#                             return 'false'
#                     elif j + 1 <= len(board[i]) - 1:
#                         next_pos = board[i][j + 1]
#                         if word[w] == next_pos and next_pos != "#" :
#                             j += 1
#                             next_pos = "#"
#                         else:
#                             return 'false'
#                     elif j - 1 >= 0:
#                         next_pos = board[i][j - 1]
#                         if word[w] == next_pos and next_pos != "#":
#                             j -= 1
#                             next_pos = "#"
#                         else:
#                             return 'false'
#                 return 'true'
#             else:
#                 return 'false'

# print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABC"))