import pytest
import engine

def test_map():
    #to test if a json file is loaded.
    assert engine.open_map("./maps.json") == True
