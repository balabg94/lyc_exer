import game_of_life

def test_return():
    grid = 4
    grid_out = [['+', '+', '+', '+'],
                ['+', '+', '+', '+'],
                ['+', '+', '+', '+'],
                ['+', '+', '+', '+']]
    #print(grid_out[0][1])
    assert game_of_life.grid(grid) == grid_out

