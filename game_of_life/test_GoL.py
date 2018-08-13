import game_of_life

def test_return():
    grid = 4
    grid_out = [['+', '+', '+', '+'],
                ['+', '+', '+', '+'],
                ['+', '+', '+', '+'],
                ['+', '+', '+', '+']]
    #print(grid_out[0][1])
    assert game_of_life.grid(grid) == grid_out

def test_cell_position():
    grid_size = 4
    grid_matrix = game_of_life.grid(grid_size)
    initial_positions = [['+', '+', '+', '+'],
                         ['+', '1', '+', '+'],
                         ['+', '1', '+', '+'],
                         ['+', '1', '+', '+']]
    
    assert game_of_life.initial_position() == initial_position
