import pprint
def grid(n):
    table = []
    for i in range(n):
        row = [0]*n
        table.append(row)
        
    return table


def initial_position():
    pos =  grid(4)
    pos[0][1] = 0
    pos[1][1] = 1
    pos[2][1] = 1
    pos[3][1] = 1
    
    return pos

    
def sum_of(i,j, new_position):
    total = 0
    N = len(new_position)
    total = new_position[(i-1)%N][(j-1)%N] + new_position[(i-1)%N][j] + new_position[(i-1)%N][(j+1)%N] + new_position[i][j-1] +  new_position[i][(j+1)%N] + new_position[(i+1)%N][(j-1)%N] + new_position[(i+1)%N][j] + new_position[(i+1)%N][(j+1)%N]
    return total

def if_alive(i, j, new_position):    
    sum_ = sum_of(i,j, new_position)
    if sum_< 2 or sum_ >3:
        #print(sum_)
        new_position[i][j] = 0
        #print("if alive  ", new_position)
        return new_position
    elif sum_==2 or sum_==3:
        new_position[i][j] = 1
        return new_position

def if_dead(i, j, new_position):    
    sum_ = sum_of(i,j, new_position)
    if sum_ == 3:
        new_position[i][j] = 1
        return new_position
    else:
        new_position[i][j] = 0
        return new_position
def main():
    first_position = initial_position()
    current_position = initial_position()
    #print(new_position)
    for x in range(2):
        for i in range(4):
            for j in range(4):
                print(f"{i}, {j}")
                if first_position[i][j] == 1:
                    print(first_position)
                    current_position[i][j] = if_alive(i, j, first_position[:])
                    print(current_position)
                else:
                    print(first_position)
                    current_position[i][j] = if_dead(i, j, first_position)
                    print(current_position)

        first_position = current_position
        #print(new_position)
        if x ==1:
            exit()
