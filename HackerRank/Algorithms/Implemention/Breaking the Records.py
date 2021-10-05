def breakingRecords(scores):
    # Write your code here
    times_of_update_score = [0, 0]

    lowest_score = highest_score = scores[0]
    #一回ずつ探索していく
    for i in range(1, len(scores)): #1~n-1
        if scores[i] > highest_score:
            highest_score = scores[i]
            times_of_update_score[0] += 1
        elif scores[i] < lowest_score:
            lowest_score = scores[i]
            times_of_update_score[1] += 1
        else:
            pass
    
    return times_of_update_score

n = int(input().strip())
scores = list(map(int, input().rstrip().split()))

print(*breakingRecords(scores))
