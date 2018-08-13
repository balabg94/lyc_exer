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

    
def sum_of(i,j):
    current_position = initial_position()
    total = 0
    N = len(current_position)
    #return current_position[i][j]
    total = current_position[(i-1)%N][(j-1)%N] + current_position[(i-1)%N][j] + current_position[(i-1)%N][(j+1)%N] + current_position[i][j-1] +  current_position[i][(j+1)%N] + current_position[(i+1)%N][(j-1)%N] + current_position[(i+1)%N][j] + current_position[(i+1)%N][(j+1)%N]
    return total

def if_alive(i, j):
    current_position = initial_position()    
    sum_ = sum_of(i,j)
    if sum_< 2 or sum_ >3:
        return 0
    else:
        return 1

def if_dead(i, j):
    current_position = initial_position()    
    sum_ = sum_of(i,j)
    if sum_ == 3:
        return 1
    else:
        return 0

