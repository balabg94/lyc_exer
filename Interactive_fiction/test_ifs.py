import pytest
import engine

def test_map():
    #to test if a json file is loaded.
    assert engine.open_map("./maps.json") == True

def test_if_firstroom():
    #to test if the first room is loaded.

    assert engine.zeroth_room("./maps.json") == "You are standing at the end of a corridor. There is a door in front of you."

def test_get_exits():
    #to test if exists from current room are available
    current_room = "0"
    assert engine.get_exits(current_room) == [['S', 1]]

def test_no_exit():
    # to test the output in case of no exit
    assert engine.if_exit("N") == "No exit that way"
