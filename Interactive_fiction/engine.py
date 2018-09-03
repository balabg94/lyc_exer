import sys
import json



def open_map(maps):
    maps = open(maps)
    
    if maps:
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

    for i in loaded_map[current_room][1:]:
        if out_path not in i:
            #print(len(loaded_map[current_room]))
            #print(loaded_map[current_room][i])
            out = 0
            
        elif out_path in i:
            #print(loaded_map[current_room][i][1])
            current_room = i[1]
            out = 1
            break
        else:
            return "ERROR"
    if out == 0:
        return out_str, current_room
    elif out == 1:
        return loaded_map[current_room][0], current_room
           
def main():
    print("The directions are N, S, E and W for North South East and West respectively.\n")
    print(zeroth_room("./maps.json"))
    current_room ="0"
    while True:
        # print("This is", current_room)
        direction = input("Enter direction: ")
        #print(if_exit(current_room, direction))
        if direction in ["N", "S", "E", "W"]:
            description, current_room = if_exit(current_room, direction)
            #print(current_room)
            print(description)
        else:
            print("\nInvalid direction. Please enter a valid direction.\n")


if __name__ == "__main__":
    main()
