#Entering a Swamp, Castle, Dungeon...

#Swamp: Swamp monsters, Giant Poisonous Spiders, Big Serpents, ...
#Castle: Warriors under the control of a dark wizard
#Dungeon: undeads, Big Skeletons, Orcs, ...
#After each successfull win, warrior can have a Stamina boost, obtain a Chield, a weapon that can cause more damage,...

#Defining Player's HP
warrior = 1000

#Start of the story
print("""Early in the morning, you left Villagetown, as necesary, to hunt for food and resources.
      After a lond day, you are returning home, but... something is way off. Villagetown is dark and hostile.
      There are 2 pathways to enter Villagetown. To your left, there're vicious blood-thirsty dwarves, and to your
      right, ferocious Orcs smashing all over the place.""")
print()

path_way = input("Choose your path (left or right): ")
print()

if path_way == "left":
    print('''You engaged the bloodthirsty dwarves, all of them go for you in pure hunger of your blood.
          You fought them fiercely and defeated them, even thought they left you shalow cuts all over your body''')
    damage_taken = warrior - 133
    print(f"Your HP is {damage_taken}")
else:
    print("You went right and fought the fierce orcs")
    damage_taken = warrior - 178
    print(f"Your HP is {damage_taken}")