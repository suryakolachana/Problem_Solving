s = 'aab'
res = []

for i in s:
    if res and res[-1] == i:
        res.pop()
    else:
        res.append(i)
res =  ''.join(res)

print(res)


