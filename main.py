print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
# Introduction
import time

# Character Creation
print("Welcome, brave adventurers, to the realm of Eldoria!")
time.sleep(1)
print("Before we begin our epic journey, let's create your characters.")
time.sleep(1)

heroes = []
num_heroes = int(input("How many heroes will embark on this quest? "))
for i in range(1, num_heroes + 1):
    hero_name = input(f"What is the name of hero {i}? ")
    hero_class = input(f"What class is {hero_name}? (e.g. warrior, mage, rogue) ")
    hero_weapon = input(f"Choose a weapon for {hero_name}: ")
    heroes.append({"name": hero_name, "class": hero_class, "weapon": hero_weapon})

time.sleep(1)
print("\nA fellowship is born! Our heroes are:")
for hero in heroes:
    print(f"{hero['name']}, the {hero['class']}, wielding a mighty {hero['weapon']}!")

# Prologue
print("\nOur tale begins in the bustling town of Silverbrook.")
time.sleep(2)
print("Rumors have spread of a dragon's lair filled with unimaginable treasures.")
time.sleep(2)
print("The townsfolk are in need of champions to embark on this perilous journey.")
time.sleep(2)
print("Will our brave heroes answer the call?")

# Quest Start
start_quest = input("Heroes, do you accept the quest to find the dragon's hoard? (yes/no) ").lower()
if start_quest == "yes":
    print("The fellowship gathers their gear and sets forth on their adventure.")
    time.sleep(2)
    print("After days of traveling, you arrive at the entrance of the Dragon's Cavern.")
    time.sleep(2)
    print("A foreboding darkness lies ahead. You must choose your path wisely.")

    chosen_path = input("There are two paths: the winding tunnels or the abandoned minecart tracks. "
                        "Which do you choose? (tunnels/tracks) ").lower()

    if chosen_path == "tunnels":
        print("The tunnels are damp and narrow, with mysterious shadows lurking.")
        time.sleep(2)
        print("You encounter a riddle-guardian blocking your way.")
        time.sleep(2)
        riddle_answer = input("Answer this riddle to pass: What has keys but can't open locks? ").lower()
        
        if riddle_answer == "a piano":
            print("The guardian nods and allows you to proceed deeper into the cavern.")
            time.sleep(2)
            print("As you journey further, you discover a hidden chamber with a shimmering pool.")
            time.sleep(2)
            print("The pool's waters can reveal your deepest desires or your greatest fears.")

            desire_or_fear = input("Do you drink from the pool to face your desire or your fear? (desire/fear) ").lower()

            if desire_or_fear == "desire":
                print("You drink from the pool and are granted visions of your heart's greatest wish.")
                time.sleep(2)
                print("Refreshed and inspired, you continue your quest.")
            elif desire_or_fear == "fear":
                print("You drink from the pool and are forced to confront your darkest fears.")
                time.sleep(2)
                print("Though shaken, you emerge stronger and more determined.")
                time.sleep(2)
                print("With newfound courage, you press on.")

            print("The tunnels lead to a massive chamber where the dragon's lair awaits.")
            time.sleep(2)
            print("The dragon stirs, sensing your presence. The final battle begins!")

            # ... (Continue with a thrilling dragon battle and epic conclusion)
            
        else:
            print("The guardian's eyes flare with anger as you answer incorrectly.")
            time.sleep(2)
            print("The ground trembles as the guardian attacks!")
            # ... (Continue with a challenging battle against the guardian)

    elif chosen_path == "tracks":
        print("The minecart tracks are rickety and overgrown, but you find an abandoned minecart nearby.")
        time.sleep(2)
        print("You hop into the minecart and begin a wild and exhilarating ride deeper into the cavern.")
        time.sleep(2)
        print("The tracks suddenly split into multiple paths, each leading to a different destination.")

        chosen_track = input("Which track do you take? (left/center/right) ").lower()

        if chosen_track == "left":
            print("The left track leads you to a hidden chamber filled with precious gemstones.")
            time.sleep(2)
            print("Your haul will surely earn you riches beyond your wildest dreams.")
            time.sleep(2)
            print("However, your celebrations are cut short as the chamber's entrance collapses.")
            time.sleep(2)
            print("You must find another way out and continue your quest.")

        elif chosen_track == "center":
            print("The center track takes you through a perilous maze of traps and pitfalls.")
            time.sleep(2)
            print("It's a treacherous journey, but your wits and agility guide you safely to the other side.")
            time.sleep(2)
            print("As you emerge, you feel a sense of accomplishment and camaraderie with your companions.")

        elif chosen_track == "right":
            print("The right track leads to a subterranean river with bioluminescent plants.")
            time.sleep(2)
            print("The beauty of the underground ecosystem is mesmerizing, but danger lurks below.")
            time.sleep(2)
            print("A massive cave-dwelling creature emerges from the water, ready to attack!")
            # ... (Continue with an intense battle against the creature)

    else:
        print("Unable to make a decision, you stand paralyzed at the entrance.")
        time.sleep(2)
        print("Moments later, the cavern's entrance collapses, sealing your fate.")
        time.sleep(2)
        print("Your journey ends here, with the dragon's hoard forever out of reach.")

else:
    print("The townsfolk's pleas fall on deaf ears as you turn away from the quest.")
    time.sleep(2)
    print("The legend of the dragon's hoard lives on, waiting for new champions to rise.")
    time.sleep(2)
    print("Eldoria's destiny remains uncertain...")
