n = int(input())
arr=[]
for i in range(n):
    print("enter element at {} index".format(i))
    arr.append(int(input()))
arr.sort() 
hp = dict()
for i in arr :
    if(i not in hp):
        hp[i]= 1
    else:
        hp[i] += 1 
for i in range(len(arr)-1 , -1 , -1) :
    if(hp[arr[i]] > 1):
        print(arr[i],i)
        break 


