def count(idx):
    if idx == -1:
        return 0
    return count(idx-1) + (s[idx].lower() in vowel)

vowel = ['a','e','i','o','u']
s = input()
print(count(len(s)-1))
