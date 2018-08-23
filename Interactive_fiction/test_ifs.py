import pytest
import engine

def test_map():
    #to test if a json file is loaded.
    assert engine.open_map("./maps.json") == True

def test_if_firstroom():
    #to test if the first room is loaded.

    assert engine.zeroth_room() == "You are standing at the end of a corridor. There is a door in front of you."
