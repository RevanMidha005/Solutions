'''
Given an array of integers of size ‘n’,
calculate the maximum sum of ‘k’ consecutive elements in the array.
'''

arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = int(input('Enter K: '))
cur_sum = 0
ans = 0
first = last = 0
start = 0

for i in range(0,len(arr)):
    cur_sum += arr[i]
    
    if i >= k-1:
        if cur_sum > ans:            
            ans = cur_sum
            first = start
            last = i

        cur_sum -= arr[start]
        start += 1

print(ans, arr[first:last+1])


            
        
        
        
