# BNNBBNAAA
# BNNBBNBNAAAA
# NANNANNANBABBABBAB
# BANBANBANBANBANBAN
# NANNANNANBABBABBAB
# NANNANN.ABBABBAB
# BANBANB.ANBANBAN
# NAN.BAB

t = int(input())
for i in range(t):
    n = int(input())
    i = 1
    j = 3*n
    ans = []
    for i in range(1,j//2+1,3):
        ans.append([i,j])
        j-=3
    print(len(ans))
    for i in ans:
        print(*i)
        

