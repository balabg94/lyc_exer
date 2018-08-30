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
    assert engine.get_exits(current_room) == [['S', '1']]

    
# Zeroth Room
    
def test_wrong_exit_0_1():
    # to test the output in case of no exit
    assert engine.if_exit("0", "N") == ("No exit that way", "0")

def test_wrong_exit_0_2():
    # to test the output in case of no exit
    assert engine.if_exit("0", "E") == ("No exit that way", "0")

def test_wrong_exit_0_3():
    # to test the output in case of no exit
    assert engine.if_exit("0", "W") == ("No exit that way", "0")

def test_correct_exit_0_4():
    # to test in case of correct exit
    assert engine.if_exit("0", "S") == ("You are standing in what seems to be a living room.", '1')

    
# First Room

def test_wrong_exit_1_1():
    # to test the output in case of no exit
    assert engine.if_exit("1", "W") == ("No exit that way", "1")

def test_wrong_exit_1_2():
    # to test the output in case of no exit
    assert engine.if_exit("1", "S") == ("No exit that way", "1")

def test_correct_exit_1_3():
    # to test in case of correct exit
    assert engine.if_exit("1", "E") == ('You are standing in what seems to be a hall way connecting many room.', '2')

def test_correct_exit_1_4():
    # to test in case of correct exit
    assert engine.if_exit("1", "N") == ("You are standing at the end of a corridor. There is a door in front of you.", '0')


# Room number 2
    
def test_correct_exit_2_1():
    # to test in case of correct exit
    assert engine.if_exit("2", "S") == ('You are standing in a connecting hallway. Three doors await you.', '6')

def test_correct_exit_2_2():
    # to test in case of correct exit
    assert engine.if_exit("2", "N") == ('Your are standing in what seems to be a bedroom. It has got a balcony attached.', '3')

def test_correct_exit_2_3():
    # to test in case of correct exit
    assert engine.if_exit("2", "E") == ('You are standing in the balcony attached to the hallway.', '5')

def test_correct_exit_2_4():
    # to test in case of correct exit
    assert engine.if_exit("2", "W") == ('You are standing in what seems to be a living room.', '1')

    
# Third Room    

def test_wrong_exit_3_1():
    # to test the output in case of no exit
    assert engine.if_exit("3", "N") == ("No exit that way", "3")

def test_wrong_exit_3_2():
    # to test the output in case of no exit
    assert engine.if_exit("3", "W") == ("No exit that way", "3")

def test_correct_exit_3_3():
    # to test in case of correct exit
    assert engine.if_exit("3", "S") == ('You are standing in what seems to be a hall way connecting many room.', '2')

def test_correct_exit_3_4():
    # to test in case of correct exit
    assert engine.if_exit("3", "E") == ('You are standing in the balcony of Room number 3.', '4')

    
# Forth Room

def test_wrong_exit_4_1():
    # to test the output in case of no exit
    assert engine.if_exit("4", "N") == ("No exit that way", "4")
    
def test_wrong_exit_4_2():
    # to test the output in case of no exit
    assert engine.if_exit("4", "E") == ("No exit that way", "4")

def test_wrong_exit_4_3():
    # to test the output in case of no exit
    assert engine.if_exit("4", "S") == ("No exit that way", "4")

def test_correct_exit_4_4():
    # to test in case of correct exit
    assert engine.if_exit("4", "W") == ('Your are standing in what seems to be a bedroom. It has got a balcony attached.', '3')

    
# Fifth Room

def test_wrong_exit_5_1():
    # to test the output in case of no exit
    assert engine.if_exit("5", "N") == ("No exit that way", "5")
    
def test_wrong_exit_5_2():
    # to test the output in case of no exit
    assert engine.if_exit("5", "E") == ("No exit that way", "5")

def test_wrong_exit_5_3():
    # to test the output in case of no exit
    assert engine.if_exit("5", "S") == ("No exit that way", "5")

def test_correct_exit_5_4():
    # to test in case of correct exit
    assert engine.if_exit("5", "W") == ('You are standing in what seems to be a hall way connecting many room.', '2')

    
# Sixth Room
    
def test_correct_exit_6_1():
    # to test in case of correct exit
    assert engine.if_exit("6", "S") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 3.', '9')

def test_correct_exit_6_2():
    # to test in case of correct exit
    assert engine.if_exit("6", "N") == ('You are standing in what seems to be a hall way connecting many room.', '2')

def test_correct_exit_6_3():
    # to test in case of correct exit
    assert engine.if_exit("6", "E") == ('You are standing in a kitchen. Utensils everywhere.', '7')

def test_correct_exit_6_4():
    # to test in case of correct exit
    assert engine.if_exit("6", "W") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 2.', '8')



# Seventh Room

def test_wrong_exit_7_1():
    # to test the output in case of no exit
    assert engine.if_exit("7", "N") == ("No exit that way", "7")
    
def test_wrong_exit_7_2():
    # to test the output in case of no exit
    assert engine.if_exit("7", "E") == ("No exit that way", "7")

def test_wrong_exit_7_3():
    # to test the output in case of no exit
    assert engine.if_exit("7", "S") == ("No exit that way", "7")

def test_correct_exit_7_4():
    # to test in case of correct exit
    assert engine.if_exit("7", "W") == ('You are standing in a connecting hallway. Three doors await you.', '6')


    
# Eigth Room

def test_wrong_exit_8_1():
    # to test the output in case of no exit
    assert engine.if_exit("8", "N") == ("No exit that way", "8")

def test_wrong_exit_8_2():
    # to test the output in case of no exit
    assert engine.if_exit("8", "W") == ("No exit that way", "8")

def test_correct_exit_8_3():
    # to test in case of correct exit
    assert engine.if_exit("8", "S") == ('You are standing in the balcony of room number 8.', '10')

def test_correct_exit_8_4():
    # to test in case of correct exit
    assert engine.if_exit("8", "E") == ('You are standing in a connecting hallway. Three doors await you.', '6')


# Ninth Room

def test_wrong_exit_9_1():
    # to test the output in case of no exit
    assert engine.if_exit("9", "E") == ("No exit that way", "9")

def test_wrong_exit_9_2():
    # to test the output in case of no exit
    assert engine.if_exit("9", "W") == ("No exit that way", "9")

def test_correct_exit_9_3():
    # to test in case of correct exit
    assert engine.if_exit("9", "N") == ('You are standing in a connecting hallway. Three doors await you.', '6')

def test_correct_exit_9_4():
    # to test in case of correct exit
    assert engine.if_exit("9", "S") == ('You are standing in the balcony of room number 9.', '11')

# Tenth Room

def test_wrong_exit_10_1():
    # to test the output in case of no exit
    assert engine.if_exit("10", "W") == ("No exit that way", "10")
    
def test_wrong_exit_10_2():
    # to test the output in case of no exit
    assert engine.if_exit("10", "E") == ("No exit that way", "10")

def test_wrong_exit_10_3():
    # to test the output in case of no exit
    assert engine.if_exit("10", "S") == ("No exit that way", "10")

def test_correct_exit_10_4():
    # to test in case of correct exit
    assert engine.if_exit("10", "N") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 2.', '8')

# Eleventh Room

def test_wrong_exit_11_1():
    # to test the output in case of no exit
    assert engine.if_exit("11", "W") == ("No exit that way", "11")
    
def test_wrong_exit_11_2():
    # to test the output in case of no exit
    assert engine.if_exit("11", "E") == ("No exit that way", "11")

def test_wrong_exit_11_3():
    # to test the output in case of no exit
    assert engine.if_exit("11", "S") == ("No exit that way", "11")

def test_correct_exit_11_4():
    # to test in case of correct exit
    assert engine.if_exit("11", "N") == ('You are standing in another bedroom. You can see a door that seems to lead to a balcony number 3.', '9')


