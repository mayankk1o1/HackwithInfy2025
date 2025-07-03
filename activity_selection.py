# Activity Selection Problem
# Description:
# You are given n activities with start and end times. Select the maximum number of activities that can be performed by a single person, asInput Format:
# n
# start1 end1
# start2 end2
# ...
# startn endn
# Output Format:
# Maximum number of non-overlapping activities
# Sample Input:
# 6
# 1 3
# 2 4
# 3 5
# 0 6
# 5 7
# 8 9
# Sample Output:
# 4
# Greedy Approach:
# Sort activities by end time. Always pick the next activity that starts after the last selected activity ends.

def activity_selection(n, activities):
    activities.sort(key=lambda x:x[1])
    count = 1
    end_time= activities[0][1]
    for i in range(n):
        if activities[i][0]>=end_time:
            count +=1
            end_time = activities[i][1]
    return count

n=int(input("Enter Number"))
activities=[]
for i in range(n):
    start,end=(map(int, input().split()))
    activities.append((start,end))
    
print(activity_selection(n,activities))


