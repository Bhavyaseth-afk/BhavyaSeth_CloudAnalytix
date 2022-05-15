str = input()
arr = str.split("-")
arr.reverse()
ans =  ""
for i in arr :
    ans = ans + i + "-" 
fa = ans[:-1]
print(fa)