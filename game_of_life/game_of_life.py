def grid(n):
    row = []
    for i in range(n):
        row.append(0)
    table = []
    for i in range(n):
        table.append(row)

    return table


def initial_position():
    pos =  [[0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]]
    pos[0][1] = 0
    pos[1][1] = 1
    pos[2][1] = 1
    pos[3][1] = 1
    
    return pos

    
