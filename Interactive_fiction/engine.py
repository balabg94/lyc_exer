#import pytest
import sys
import json

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
    for i in range(1, len(loaded_map)):
        if out_path in loaded_map[current_room][i]:
            current_room = loaded_map[current_room][i][1]
            return loaded_map[current_room][0], current_room
        else:
            return "No exit that way"

def main():
    current_room = 0
