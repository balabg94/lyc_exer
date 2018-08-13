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

    
def sum_of(i,j, new_position):
    #new_position = initial_position()
    total = 0
    N = len(new_position)
    #return new_position[i][j]
    total = new_position[(i-1)%N][(j-1)%N] + new_position[(i-1)%N][j] + new_position[(i-1)%N][(j+1)%N] + new_position[i][j-1] +  new_position[i][(j+1)%N] + new_position[(i+1)%N][(j-1)%N] + new_position[(i+1)%N][j] + new_position[(i+1)%N][(j+1)%N]
    return total

def if_alive(i, j, new_position):
    #new_position = initial_position()    
    sum_ = sum_of(i,j, new_position)
    if sum_< 2 or sum_ >3:
        new_position[i][j] = 0
        return new_position
    else:
        new_position[i][j] = 1
        return new_position

def if_dead(i, j, new_position):
    #new_position = initial_position()    
    sum_ = sum_of(i,j, new_position)
    if sum_ == 3:
        new_position[i][j] = 1
        return new_position
    else:
        new_position[i][j] = 0
        return new_position

# def main():
#     new_position = initial_position()
#     while True:
        
