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


