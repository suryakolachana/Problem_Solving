def compare_array(a,b):
    c = 0
    d = 0
    for x in zip(a,b):
        if x[0] < x[1]:
            c += 1
        elif x[0] > x[1]:
            d += 1
        elif x[0] == x[1]:
            pass
    return (c,d)

a = [6,8,12]
b = [7,9,15]

print(compare_array(a,b))