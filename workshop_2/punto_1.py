#!/usr/bin/python3

"""
Your mission is simple sailor, but important for the crew,
when you see one of these creatures you must say so:
- Ahoy! captain, a Kraken
- Ahoy! captain, some Mermaids
- Ahoy! captain, a Whale
- Ahoy! captain, a Hippocampus
- Ahoy! captain, one Macaraprono
- Ahoy! captain, an Octopus
- Ahoy! captain, some Leviathans
- Ahoy! captain, a Hydra

Your life is on it sailor, you must pronounce them with the correct article
according to their species
according to their species (uno, una, unos, unas).
In addition, you must say the direction of the ship in which the creature
appears:
- To port
- To starboard
- By the bow
- Stern

To fulfill the mission you must create a program that, given the creature and
the location, builds the correct chain.
location, builds the correct chain. The program must be run as many times as
necessary until the capital tells you to "stop".

For example, if they appear:
- Kraken and Port should say: Ahoy! captain, one Kraken to port.
- Leviathans and Bow should say: Ahoy! captain, some Leviathans by the bow.

And so on until you enter the word to stop the program.
"""

run = True

while run:
    creature_list = ["kraken", "hipocampo", "pulpo", "leviatanes",
                     "ballena", "macaraprono", "sirenas", "hidras"]
    location_list = ["babor", "estribor", "proa", "popa"]

    creature = str(input("\nIngresa una criatura: ")).lower()
    location = str(input("Ingresa una ubicación: ")).lower()

    sentence = "¡Ahoy! capitán,"

    if creature != "" and location != "":
        if creature in creature_list and location in location_list:
            if location in location_list[0:2]:
                w2 = "a"
            else:
                w2 = "por la"

            if creature in creature_list[0:3]:
                w1 = "un"
            elif creature in creature_list[3]:
                w1 = "unos"
            elif creature in creature_list[4:6]:
                w1 = "una"
            elif creature in creature_list[6:]:
                w1 = "unas"

            print(f"{sentence} {w1} {creature.capitalize()} {w2} {location}.")

        else:
            print("Valores incorrectos")
    else:
        print("\nPor favor llenar los campos correctamente")

    play = str(input(
        """
Ingresa 'stop' para finalizar o presiona cualquier tecla para continuar: """))\
        .lower()
    if play == "stop":
        print("\nAdios marinero!")
        run = False
