import game_of_life

def test_return():
    grid = 4
    grid_out = [[0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0],
                [0, 0, 0, 0]]
    #print(grid_out[0][1])
    assert game_of_life.grid(grid) == grid_out

def test_cell_position():
    grid_size = 4
    grid_matrix = game_of_life.grid(grid_size)
    initial_positions = [[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0]]
    
    assert game_of_life.initial_position() == initial_positions


def test_sum_of_neighbors():
    initial_positions = [[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0]]
    assert game_of_life.sum_of(2, 1, initial_positions) == 2
    


    
def test_if_alive():
    initial_positions = [[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0]]
    assert game_of_life.if_alive(2, 1, initial_positions) == [[0, 0, 0, 0],
                                                              [0, 1, 0, 0],
                                                              [0, 1, 0, 0],
                                                              [0, 1, 0, 0]]
    
    
def test_if_alive_sides():
    initial_positions = [[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0]]
    assert game_of_life.if_alive(3, 3, initial_positions) == [[0, 0, 0, 0],
                                                              [0, 1, 0, 0],
                                                              [0, 1, 0, 0],
                                                              [0, 1, 0, 0]]
    

def test_if_alive_left_mid():
    initial_positions = [[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0]]
    assert game_of_life.if_alive(2, 0, initial_positions) == [[0, 0, 0, 0],
                                                              [0, 1, 0, 0],
                                                              [1, 1, 0, 0],
                                                              [0, 1, 0, 0]]
    

def test_if_alive_right_mid():
    initial_positions = [[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0]]
    assert game_of_life.if_alive(2, 3, initial_positions) == [[0, 0, 0, 0],
                                                              [0, 1, 0, 0],
                                                              [0, 1, 0, 0],
                                                              [0, 1, 0, 0]]
    


def test_if_dead():
    initial_positions = [[0, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0],
                         [0, 1, 0, 0]]
    assert game_of_life.if_alive(2, 0, initial_positions) == [[0, 0, 0, 0],
                                                              [0, 1, 0, 0],
                                                              [1, 1, 0, 0],
                                                              [0, 1, 0, 0]]
    
