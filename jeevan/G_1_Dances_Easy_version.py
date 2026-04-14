# # 1 4 3 3 2 2 1 1
# # 1 1 1 1 3 3 3 3

# # 1 2 3 4 5
# # 2 3 4 5 6

# 1 2 3 4 5 6 7 8 9
# 1 1 2 2 3 4 5 5 6




def upper_bound(i,j,x,arr):
    ans = -1
    while i<=j:
        mid = (i+j)//2
        if arr[mid] <= x:
            i = mid + 1
        else:
            ans = mid
            j = mid - 1
    return ans



    
   