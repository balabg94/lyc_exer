#import pytest
import sys
import json
#current_room = "0"

def open_map(maps):
    maps = open(maps)
    
    if maps:
        #print(maps.read())
        return 1
    
def zeroth_room(maps):
   wrapper = open(maps,"r")
   data = wrapper.readline()
   loaded_map = json.loads(data)
   return loaded_map["0"][0]

def get_exits(current_room):
    wrapper = open("./maps.json","r")
    data = wrapper.readline()
    loaded_map = json.loads(data)
    return loaded_map[current_room][1:]

def if_exit(current_room, out_path):
    wrapper = open("./maps.json","r")
    data = wrapper.readline()
    loaded_map = json.loads(data)
    out = 0
    out_str = "No exit that way"
    for i in range(1, len(loaded_map[current_room])):
        #print(current_room)
        if out_path not in loaded_map[current_room][i]:
            #print(len(loaded_map[current_room]))
            #print(loaded_map[current_room][i])
            #return out_str
            out = 0
        #continue
        elif out_path in loaded_map[current_room][i]:
            #print(out_path)
            current_room = loaded_map[current_room][i][1]
            out = 1
            #break
        else:
            return "ERROR"
    if out == 0:
        return out_str, current_room
    elif out == 1:
       # return loaded_map[current_room][i][1]
        return loaded_map[current_room][0], current_room
           
def main():
    print(zeroth_room("./maps.json"))
    current_room ="0"
    while True:
        #print("This is", current_room)
        direction = input("Enter direction: ")
        #print(if_exit(current_room, direction))
        a, current_room = if_exit(current_room, direction)
        #print(current_room)
        print(a)
