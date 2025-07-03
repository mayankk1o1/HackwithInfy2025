#leetcode 942
#link - https://leetcode.com/problems/di-string-match/

def diStringMatch(s):
        low = 0
        high = len(s)
        result = []
        for char in s:
            if char =="I":
                result.append(low)
                low +=1
            else:
                result.append(high)
                high -=1
        return result + [low]

s=input("Enter String, Only the combination of I and D are allowed: ")
print(diStringMatch(s))
