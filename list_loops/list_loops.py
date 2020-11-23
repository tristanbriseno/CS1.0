songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0], songs[2])

songs = ["ROCKSTAR", "Do It", "For The Night"]
print(songs[0:2])

songs = ["ROCKSTAR", "Do It", "For The Night"]
songs[0] = "Dynamite"
print(songs)

songs = ["ROCKSTAR", "Do It", "For The Night"]
songs.append("Forever") 
songs.append("All Me")
songs.append("Trophies")
del songs[1]
print(songs)

# adds an element to the end of the list
#songs.append("Mood")
# adds a list to end of a list
#songs.extend(["Laugh Now Cry Later", "Blinding Lights"])
# adds element at specific index followed by item
#songs.insert(0, "Life Is Good")

# removes element from list
#songs.remove("ROCKSTAR")
# removes and returns element at specific index
#songs.pop(1)
# removes all elements from a list
#songs.clear()
#delete the 3rd element
#del songs[3]

# Option 1
#for song in songs:
#    print(song)
# Option 2
#for i in range(len(songs)):
#    print(songs[i])

animals = ["Cat", "Dog", "Bird"]
animals.append("Lion")
print(animals[2])
del animals[0]
for i in range(len(animals)):
    print(animals[i])