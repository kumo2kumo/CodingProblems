#return  int: the number of letters changed during transmission
#input: SOSSPSSQSSOR

def marsExploration(s):
    count = 0
    for i in range(0, len(s), 3):
        if s[i] != 'S':
            count += 1
        if s[i + 1] != "O":
            count += 1
        if [s + 2] != "S":
            count += 1

        #もう少し簡潔に
        # check_str = ['S', 'O', 'S']
        # for i in range(0, len(s), 3):
        #     each_str = [i:i+3]
        #     for k, j in zip(check_str, each_str):
        #         if k != j:
        #         count += 1 
    return count