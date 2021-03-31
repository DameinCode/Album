x = input()
ans =''
isTrue = False
for i in range(len(x)-1, -1, -1):
    if(i == len(x)-1 and int(x[i]) == 0): 
        isTrue = True
        continue
    if(isTrue == True and int(x[i]) == 0):
        continue
    
    ans += x[i]
    isTrue = False

print(ans)