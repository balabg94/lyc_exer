#import pytest
import sys

def open_map(maps):
    maps = open(maps)
    if maps:
        print(maps.read())
        return 1
    
