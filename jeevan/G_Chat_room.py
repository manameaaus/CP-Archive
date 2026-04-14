# s = input()
# temp = ""
# for i in s:
#     if i == "h" and temp == "":
#         temp += i
#     elif i == "e" and temp == "h":
#         temp += i
#     elif i == "l" and (temp == "hel" or temp == "he"):
#         temp += i
#     elif i == "o" and temp == "hell":
#         temp += i

# if temp == "hello":
#     print("YES")
# else:
#     print("NO")

s = input()
temp = ""
tar = "hello"
start = 0
for i in s:
    if start<5 and i == tar[start]:
        temp += tar[start]
        start += 1
    

if tar == temp:
    print("YES")
else:
    print("NO")