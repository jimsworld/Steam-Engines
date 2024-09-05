import pygame
import random
import math
from global_time import GlobalTime
from loco_steam import Loco_Steam

# Initialize global time
global_time = GlobalTime()

# Locomotive list
loco_01 = Loco_Steam("Talyllyn", 0, 0, 0, 0, 10, 10, 10, 10)
loco_02 = Loco_Steam("Dolgoch", 0, 0, 0, 0, 8, 10, 10, 12)
loco_list = [loco_01, loco_02]

# Start menu to select a locomotive
def start_menu(loco_list):
    
    print("\n--- Start Menu"
          "\nSteam Locomotive List:")
    for i, loco in enumerate(loco_list, start=1):
        print(f"\n{i}: {loco.name}")

    selected_index = -1
    while selected_index < 1 or selected_index > len(loco_list):
        try:
            selected_index = int(input("\nEnter the number of the desired locomotive: "))
            if selected_index < 1 or selected_index > len(loco_list):
                print("No loco with that number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    chosen_loco = loco_list[selected_index - 1]
    print(f"\nYou have chosen: {chosen_loco.name}")
    return chosen_loco


# Stat menu to display the locomotive stats
def stat_menu(chosen_loco):
    print(f"\n--- {chosen_loco.name} Stats ---"
            f"\nMax Coal: {chosen_loco.max_coal}"
            f"\nMax Water: {chosen_loco.max_water}"
            f"\nMax Steam: {chosen_loco.max_steam}"
            f"\nMax Speed: {chosen_loco.max_speed}")


# Start the game
def start_game(chosen_loco):
    print("\nLet's get ready..."
            "\nWhat would you like to do?\n"
            "\n'1': Prepare your locomotive"
            "\n'2': View your locomotive stats"
            "\n'3': View Station Map"
            "\n'help': Show commands")

    start_game_choice = input("\n> ")
    match start_game_choice:

        case "1":
            add_coal = input("\nAdd some Coal?"
                                "\n'1': Full Coal"
                                "\n'2': Choose amount"
                                "\n'3': Skip\n"
                                "\n> ")
            match add_coal:
                case "1":
                    chosen_loco.current_coal = chosen_loco.max_coal
                    print("Full Coal added.")
                case "2":
                    coal_amount = int(input("Enter the amount of coal to add: "))
                    chosen_loco.current_coal += coal_amount
                case "3":
                    print("No Coal added.")
            
            print(f"{chosen_loco.current_coal} / {chosen_loco.max_coal} Coal added")
            
            add_water = input("\nAdd some Water?"
                                "\n'1': Full Water"
                                "\n'2': Choose amount"
                                "\n'3': Skip\n"
                                "\n> ")
            match add_water:
                case "1":
                    chosen_loco.current_water = chosen_loco.max_water
                    print("Full Water added.")
                case "2":
                    water_amount = int(input("Enter the amount of Water to add: "))
                    chosen_loco.current_water += water_amount
                case "3":
                    print("No Water added.")
            
            print(f"{chosen_loco.current_water} / {chosen_loco.max_water} Water added")
    
        case "2":
            stat_menu(chosen_loco)
        
        case "3":
            print("Feature coming soon.")

        case "help":
            show_menu()
    
    start_game_choice = input("\nAnything else?: ")


# Input menu shows commands
def show_menu():
    print("\nEnter command:"
          "\n'help':       shows this menu"
          "\n'start':      start engine"
          "\n'stop':       stop engine"
          "\n'1':          add add"
          "\n'2':          add water"
          "\n'3':          make steam"
          "\n'4':          accelerate"
          "\n'5':          brake"
          "\n'quit':       exits.")


#  Test the steam locomotive
def test_loco(chosen_loco):
    while True:
        chosen_loco.start_engine()
        chosen_loco.make_steam()
        print(chosen_loco.get_speed(), chosen_loco.get_resources())
        pygame.time.wait(500)


# Main loop
def main():
    chosen_loco = start_menu(loco_list)

    stat_menu(chosen_loco)

    start_game(chosen_loco)

    test_loco(chosen_loco)


main()