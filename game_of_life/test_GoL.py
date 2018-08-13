import game_of_life

def test_return():
    grid = 4
    grid_out = ['-+-+-+-+',
                '-+-+-+-+',
                '-+-+-+-+',
                '-+-+-+-+']
    assert game_of_life.grid(grid) == grid_out
