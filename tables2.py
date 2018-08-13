def tables2(n):
    table = []
    for x in range(1, n+1):
        row=[]
        for y in range(1, n+1):
            m = str(x*y)
            row.append(m.rjust(5))
            # spc = ' '*(4-len(str(m)))
            # table.append(str(m)+spc)
        table.append(''.join(row))
    print("\n\n".join(table))
