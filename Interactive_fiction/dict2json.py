import json

dictio = {'0': ['You are standing at the end of a corridor. There is a door in front of you.',
                ['S', '1']],
          '1': ['You are standing in what seems to be a living room.', ['E','2'],['N','0']],

          '2': ['You are standing in what seems to be a hall way connecting many room.', ['W','1'],
                ['N', '3'], ['E', '5'], ['S', '6']],
          '3': ['Your are standing in what seems to be a bedroom. It has got a balcony attached.',
                ['E', '4'], ['S', '2']],
          '4': ['You are standing in the balcony of Room number 3.', ['W', '3']],

          '5': ['You are standing in the balcony attached to the hallway.', ['W', '2']],

          '6': ['You are standing in a connecting hallway. Three doors await you.', ['N', '2'],
                ['S', '9'], ['E', '7'], ['W', '8']]


}
dumped_dictio = json.dumps(dictio)
loaded_dictio = json.loads(dumped_dictio)

# print (loaded_dictio['0'][0])

# json_file = open("maps.json", "w")

# json_file.write(loaded_dictio)

# json_file.close()

with open('maps.json', 'w') as outfile:
    json.dump(loaded_dictio, outfile)

outfile.close()
