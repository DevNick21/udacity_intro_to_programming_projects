import random
import time


def print_pause(message):
    print(message)
    time.sleep(1)


def play_game():
    print_pause(
        "You find yourself standing in an open field, filled with grass and yellow wildflowers. ")
    print_pause(
        "Rumor has it that a wicked faire is somewhere around here, and has been terrifying the nearby village.")
    print_pause("...")
    print_pause("You see a cave and a hut")

    print(
        "Enter 1 to knock on the door of the hut.\nEnter 2 to peer into the cave.")
    choice = int(
        input("What would you like to do?\n(Please enter 1 or 2). "))
    while choice != 1 and choice != 2:
        choice = int(input("(Please enter a valid input: 1 or 2). "))

    if choice == 1:
        def first_scene():
            print_pause(
                f"You find a crying child and you see a young fairy in the house, you get confused")
            print_pause(
                f"then the child turns into a three-eyed monster, you pull out your dagger")
            print_pause("the fairy rushes and grabs it from you")
            next_choice = int(
                input("Would stay to fight (1) or do you run away (2) "))

            while next_choice != 1 and next_choice != 2:
                next_choice = int(
                    input("(Please enter a valid input: 1 or 2). "))
            if next_choice == 1:
                print_pause("you are overpowered by the monster and the fairy")
                print_pause("you die")
            else:
                print_pause("you are chased down by the flying fairy")
                print_pause(
                    "you managed to escaped and they get the wing stuck in the bushes")
                print_pause("you survived with some bruises")

        def second_scene():
            print_pause(
                f"That's the wicked fairie's in the house")
            print_pause(
                f"the fairy attacks you!")
            next_choice = int(
                input("Would stay to fight (1) or do you run away (2) "))
            while next_choice != 1 and next_choice != 2:
                next_choice = int(
                    input("(Please enter a valid input: 1 or 2). "))
            if next_choice == 1:
                print_pause("you are overpowered the fairy")
                print_pause("they knock off your dagger and kill you")
            else:
                print_pause("you are chased down by the flying fairy")
                print_pause(
                    "you managed to escaped and they get the wing stuck in the bushes")
                print_pause("you survived with some bruises")

        rand = random.randint(0, 1)
        if rand == 0:
            first_scene()
        else:
            second_scene()
    else:
        print_pause("you peer cautiously into the cave, you find a sword!")
        print_pause(
            "you take it and walk back out, you now discard your dagger")

        print("Enter 1 to knock on the door of the hut.\nEnter 2 to peer into the cave.")
        choice = int(
            input("What would you like to do?\n(Please enter 1 or 2). "))

        while choice != 1 and choice != 2:
            choice = int(input("(Please enter a valid input: 1 or 2). "))

        while choice == 2:
            print_pause(
                "you peer cautiously into the cave, you find a nothing")
            print_pause(
                "you have been here before, its empty except your old dagger")
            print_pause(
                "you see you have no room for it, you leave it and walk back out")
            print(
                "Enter 1 to knock on the door of the hut.\nEnter 2 to peer into the cave.")
            choice = int(
                input("What would you like to do?\n(Please enter 1 or 2). "))
        if choice == 1:
            print_pause(
                "You find a crying child and you see a young fairie in the house, you get confused")
            print_pause(
                "the child turn into a three-eyed monster and you pull out your sword")
            print_pause("the fairy tries to grab it and you cut their wings")
            next_choice = int(
                input("Would stay to fight (1) or do you run away (2) "))
            while next_choice != 1 and next_choice != 2:
                choice = int(
                    input("""(Please enter a valid input: 1 or 2). """))
            if next_choice == 1:
                def fights_with_sword():
                    print_pause(
                        "you cut the three-eyed monster's head and cut the fairy's legs")
                    print_pause(
                        "you go out with their bodies and become a hero to the villager")
                    print_pause("you are rewarded")

                fights_with_sword()
            else:
                def runs_with_sword():
                    print_pause("you are chased down by the monster")
                    print_pause(
                        "you drop your sword and the pick it up and throw it at you")
                    print_pause(
                        "they miss but it scrapes your leg, you manage to escape with some injures")
                    print_pause(
                        "the villagers are now being terrorized by a monster with a sword")

                runs_with_sword()


play_game()
print_pause("GAME OVER")
play_again = input("would you like to play again? (y/n) ").lower()

while play_again != "y" and play_again != "n":
    play_again = input("would you like to play again? (y/n) ").lower()

if play_again == "y":
    play_game()
elif play_game == "n":
    print("Goodbye")
