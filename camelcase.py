a = '   saveChangesInTheEditor   '

a = a.strip()
if len(a) > 1:
    v_count = 1
    for i in a:
        if  i.isupper():
            v_count += 1
            
    print(v_count)
           





