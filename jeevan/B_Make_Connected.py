

# def solve():
#     n = int(input())
#     mat = []
#     c = 0
#     for i in range(n):
#         l = list(input())
#         mat.append(l)
#         c += l.count("#")


#     # row = []
#     # for i in range(n):
#     #     row.append(mat[i].count("#"))


#     # column = []
#     # for j in range(n):
#     #     temp = 0
#     #     for i in range(n):
#     #         if mat[i][j] == "#":
#     #             temp += 1

#     #     column.append(temp)




#     def ddd_row():
#         row = []
#         for i in range(n):
#             row.append(mat[i].count("#"))


#         return row

#     def ddd_col():
#         column = []
#         for j in range(n):
#             temp = 0
#             for i in range(n):
#                 if mat[i][j] == "#":
#                     temp += 1

#             column.append(temp)
#         return column


    


#     if c == 0:
#         print("YES")
#     else:

#         def dfdfr(start,end,step,tra,den,pet,dia):
#             for i in range(start,end,step):
#                 for j in range(tra,den,pet):
#                     if mat[i][j] == "#":

#                         row = ddd_row()
#                         column = ddd_col()
#                         st_i = i
#                         st_j = j
#                         temp = 0
#                         while (st_i < n and st_j < n):

#                             kkk = 0
#                             if mat[st_i][st_j] == "#":
#                                 temp += 1
#                             if st_i + 1 < n and mat[st_i + 1][st_j] == "#":
#                                 kkk += 1
#                                 temp += 1
#                             if st_j + 1 < n and mat[st_i][st_j + 1] == "#":
#                                 kkk += 1
#                                 temp += 1

#                             if temp == c:
#                                 print("YES")
#                                 return True
                            


#                             luck = 0

                            

#                             if (st_j + 1 < n and mat[st_i][st_j + 1] == "#" and row[st_i] <= 2 and column[st_j + 1] <= 2) or (st_j + 1 < n and mat[st_i][st_j + 1] != "#" and row[st_i] <= 1 and column[st_j + 1] <= 1):
#                                 luck += 1
#                                 row[st_i] = 2
#                                 if mat[st_i][st_j + 1] != "#":
#                                     column[st_j + 1] += 1
#                             elif (st_i + 1 < n and mat[st_i + 1][st_j] == "#" and column[st_j] <= 2 and row[st_i + 1] <= 2) or (st_i + 1 < n and mat[st_i + 1][st_j] != "#" and column[st_j] <= 1 and row[st_i + 1] <= 1):
#                                 luck += 1
#                                 column[st_j] = 2
#                                 if mat[st_i + 1][st_j] != "#":
#                                     row[st_i + 1] += 1


#                             if luck == 0:
#                                 # print(st_i,st_j)
#                                 break
                            
#                             st_j += 1
#                             st_i += 1

#                             if kkk == 2 and (not (temp == c - 1 and st_i < n and st_j < n and mat[st_i][st_j] == "#")):
#                                 break
#                             else:
#                                 if st_i < n and st_j >= 0 and st_i >= 0 and st_j < n and (row[st_i] - (mat[st_i][st_j] == "#") >= 2 or column[st_j] - (mat[st_i][st_j] == "#") >= 2):
#                                     break

#                         row = ddd_row()
#                         column = ddd_col()
#                         st_i = i
#                         st_j = j
#                         temp = 0
#                         while (st_i >= 0 and st_j < n):
#                             kkk = 0
#                             if mat[st_i][st_j] == "#":
#                                 temp += 1
#                             if st_i - 1 >= 0 and mat[st_i - 1][st_j] == "#":
#                                 temp += 1
#                                 kkk += 1
#                             if st_j + 1 < n and mat[st_i][st_j + 1] == "#":
#                                 temp += 1
#                                 kkk += 1

#                             if temp == c:
#                                 print("YES")
#                                 return True
                            


#                             luck = 0

                            

#                             if (st_j + 1 < n and mat[st_i][st_j + 1] == "#" and row[st_i] <= 2 and column[st_j + 1] <= 2) or (st_j + 1 < n and mat[st_i][st_j + 1] != "#" and row[st_i] <= 1 and column[st_j + 1] <= 1):
#                                 luck += 1
#                                 row[st_i] = 2
#                                 if mat[st_i][st_j + 1] != "#":
#                                     column[st_j + 1] += 1
#                             elif (st_i - 1 >= 0 and mat[st_i - 1][st_j] == "#" and column[st_j] <= 2 and  row[st_i - 1] <= 2) or (st_i - 1 >= 0 and mat[st_i - 1][st_j] != "#" and column[st_j] <= 1 and row[st_i - 1] <= 1):
#                                 luck += 1
#                                 column[st_j] = 2
#                                 if (mat[st_i - 1][st_j] != "#"):
#                                     row[st_i - 1] += 1


#                             if luck == 0:
#                                 break
                            
                            
                            

#                             st_i -= 1
#                             st_j += 1


#                             if kkk == 2 and (not (temp == c - 1 and st_i >= 0 and st_j < n and mat[st_i][st_j] == "#")):
#                                 break
#                             else:
#                                 if st_i < n and st_j >= 0 and st_i >= 0 and st_j < n and (row[st_i] - (mat[st_i][st_j] == "#") >= 2 or column[st_j] - (mat[st_i][st_j] == "#") >= 2):
#                                     break
                        
                        
                        
                        
#                         row = ddd_row()
#                         column = ddd_col()
#                         st_i = i
#                         st_j = j
#                         temp = 0
#                         while (st_i >= 0 and st_j >= 0):
#                             kkk = 0
#                             if mat[st_i][st_j] == "#":
#                                 temp += 1
#                             if st_i - 1 >= 0 and mat[st_i - 1][st_j] == "#":
#                                 temp += 1
#                                 kkk += 1
#                             if st_j - 1 >= 0 and mat[st_i][st_j - 1] == "#":
#                                 temp += 1
#                                 kkk += 1



#                             if temp == c:
#                                 print("YES")
#                                 return True
                            
                            

                            

#                             luck = 0

                            

#                             if (st_j - 1 >= 0 and mat[st_i][st_j - 1] == "#" and row[st_i] <= 2 and column[st_j-1] <= 2) or (st_j - 1 >= 0 and mat[st_i][st_j - 1] != "#" and row[st_i] <= 1 and column[st_j-1] <= 1):
#                                 # if st_i == 4 and st_j == 5 and  dia == 3:
#                                 #     print((st_j - 1 >= 0 and mat[st_i][st_j - 1] == "#" and row[st_i] <= 2))
                                
#                                 luck += 1
#                                 row[st_i] = 2
#                                 if (mat[st_i][st_j - 1] != "#"):
#                                     column[st_j - 1] +=  1
                                
#                             elif (st_i - 1 >= 0 and mat[st_i - 1][st_j] == "#" and column[st_j] <= 2 and row[st_i - 1] <= 2) or (st_i - 1 >= 0 and mat[st_i - 1][st_j] != "#" and column[st_j] <= 1 and row[st_i - 1] <= 1):
#                                 luck += 1
#                                 column[st_j] = 2
#                                 if (mat[st_i - 1][st_j] != "#"):
#                                     row[st_i - 1] += 1




#                             if luck == 0:
#                                 break


#                             # if dia == 3:
#                             #     if st_i == 4 and st_j == 5:
#                             #         print(luck)

                            
#                             st_i -= 1
#                             st_j -= 1


#                             if kkk == 2 and (not (temp == c - 1 and st_i >= 0 and st_j >= 0 and mat[st_i][st_j] == "#")):

#                                 break
#                             else:
#                                 if st_i < n and st_j >= 0 and st_i >= 0 and st_j < n and (row[st_i] - (mat[st_i][st_j] == "#") >= 2 or column[st_j] - (mat[st_i][st_j] == "#") >= 2):
                                    

#                                     break
                            
                            


#                         row = ddd_row()
#                         column = ddd_col()
#                         st_i = i
#                         st_j = j
#                         temp = 0
#                         while (st_i < n and st_j >= 0):
#                             kkk = 0
#                             if mat[st_i][st_j] == "#":
#                                 temp += 1
#                             if st_i + 1 < n and mat[st_i + 1][st_j] == "#":
#                                 temp += 1
#                                 kkk += 1
#                             if st_j - 1 >= 0 and mat[st_i][st_j - 1] == "#":
#                                 temp += 1
#                                 kkk += 1


#                             if temp == c:
#                                 print("YES")
#                                 return True
                            


#                             luck = 0

                            

#                             if (st_j - 1 >= 0 and mat[st_i][st_j - 1] == "#" and row[st_i] <= 2 and column[st_j - 1] <= 1) or (st_j - 1 >= 0 and mat[st_i][st_j - 1] != "#" and row[st_i] <= 1 and column[st_j - 1] <= 1):
#                                 luck += 1
#                                 row[st_i] = 2
#                                 if mat[st_i][st_j - 1] != "#":
#                                     column[st_j - 1] += 1
#                             elif (st_i + 1 < n and mat[st_i + 1][st_j] == "#" and column[st_j] <= 2 and row[st_i + 1] <= 2) or (st_i + 1 < n and mat[st_i + 1][st_j] != "#" and column[st_j] <= 1 and row[st_i + 1] <= 1):
#                                 luck += 1
#                                 column[st_j] = 2
#                                 if mat[st_i + 1][st_j] != "#":
#                                     row[st_i + 1] += 1


#                             if luck == 0:
#                                 # print(st_i,st_j,row[st_i])
#                                 break

                            
#                             st_i += 1
#                             st_j -= 1


#                             if kkk == 2 and (not (temp == c - 1 and st_i < n and st_j >= 0 and mat[st_i][st_j] == "#")):
#                                 # print(st_i,st_j,row[st_i])
#                                 break
#                             else:
#                                 if st_i < n and st_j >= 0 and st_i >= 0 and st_j < n and (row[st_i] - (mat[st_i][st_j] == "#") >= 2 or column[st_j] - (mat[st_i][st_j] == "#") >= 2):
#                                     print("dfv",column[st_j] , (mat[st_i][st_j] == "#"))
                                    
#                                     break
                                


                            
                        
#                     # print("NO")
#                         return False
                


        
                
#         # if dfdfr(0,n,1,0,n,1,1):
#         #     return 1
#         # if dfdfr(0,n,1,n-1,0,-1,2):
#         #     return 2
#         # if dfdfr(n-1,0,-1,0,n,1,3):
#         #     return 3
#         # if dfdfr(n-1,0,-1,n-1,0,-1,4):
#         #     return 4


#         print(dfdfr(0,n,1,0,n,1,1))

#         print("NO")
#         return 5
            
        
                

   

                    


                
                


# t = int(input())
# for i in range(t):
#     kk = solve()
#     # print(kk)
    








def solve():
    n = int(input().strip())
    mat = [list(input().strip()) for _ in range(n)]

    total = sum(row.count('#') for row in mat)

    # Case 1: Only 0 or 1 '#'
    if total <= 1:
        print("YES")
        return

    # Case 2: Check for exact 2x2 block of '#'
    if total == 4:
        for i in range(n - 1):
            for j in range(n - 1):
                if (
                    mat[i][j] == '#' and
                    mat[i][j + 1] == '#' and
                    mat[i + 1][j] == '#' and
                    mat[i + 1][j + 1] == '#'
                ):
                    print("YES")
                    return

    # Case 3: Check diagonals
    main_diag = [0] * (2 * n - 1)
    anti_diag = [0] * (2 * n - 1)

    for i in range(n):
        for j in range(n):
            if mat[i][j] == '#':
                main_diag[i - j + (n - 1)] += 1
                anti_diag[i + j] += 1

    # Adjacent main diagonals
    for k in range(len(main_diag) - 1):
        if main_diag[k] + main_diag[k + 1] == total:
            print("YES")
            return

    # Adjacent anti diagonals
    for k in range(len(anti_diag) - 1):
        if anti_diag[k] + anti_diag[k + 1] == total:
            print("YES")
            return

    print("NO")


# Handle multiple test cases
t = int(input().strip())
for _ in range(t):
    solve()
