"""
Problem : Simplify a List
Input = [1,2,[3],[4,[5,6]]]
Output = [1,2,3,4,5,6]
"""
a = [1,2,[3],[4,[5,6]]]

b = []

for i in a:
  if isinstance(i,list):
    for i in i:
      if isinstance(i,list):
        for i in i:
          b.append(i)
      else:
        b.append(i)
  else:
    b.append(i)
print(b)
