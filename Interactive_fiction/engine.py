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
