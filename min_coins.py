
def min_coins(amount,denomination):
    # x=denomination.sort()
    count=0
    for i in range(len(denomination)-1,0,-1):
        while amount>=denomination[i]:
            count +=1
    print(count)

amount=int(input("Enter Amount"))
denomination=list(map(int,input().split()))
print(min_coins(amount,denomination))