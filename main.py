# Steam Engines v0.04

import pygame
import random
import math
from global_time import GlobalTime
from loco_steam import Loco_Steam

# Initialize global time
global_time = GlobalTime()

# Locomotive list
loco_01 = Loco_Steam("Talyllyn", 10, 10, 0, 0, 10, 10, 10, 10)
loco_02 = Loco_Steam("Dolgoch", 8, 10, 0, 0, 8, 10, 10, 12)
loco_list = [loco_01, loco_02]

# Start menu to select a locomotive
def start_menu(loco_list):
    
    print("\n--- Start Menu"
          "\nSteam Locomotive List:")
    for i, loco in enumerate(loco_list):
        print(f"\n{i}: {loco.name}")

    selected_index = -1
    while selected_index < 0 or selected_index >= len(loco_list):
        try:
            selected_index = int(input("\nEnter the number of the desired locomotive: "))
            if selected_index < 0 or selected_index >= len(loco_list):
                print("No loco with that number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    chosen_loco = loco_list[selected_index]
    print(f"\nYou have chosen: {chosen_loco.name}")
    return chosen_loco


# Stat menu to display the locomotive stats
def stat_menu(chosen_loco):
    user_input = input("Would you like to view the stats of the locomotive? (y/n): ")
    if user_input.lower() == "y":
        print(f"\n--- {chosen_loco.name} Stats ---"
              f"\nTop Speed: {chosen_loco.max_speed}"
              f"\nCoal: {chosen_loco.max_coal}"
              f"\nWater: {chosen_loco.max_water}"
              f"\nSteam: {chosen_loco.max_steam}")
    
    elif user_input.lower() == "n":
        print("No stats will be displayed, let's continue.")


# Input menu shows commands
show_menu = True
def show_menu():
    global show_menu
    print("\nEnter command:"
          "\n'help':       shows this menu"
          "\n'start':      start engine"
          "\n'stop':       stop engine"
          "\n'1':          add water"
          "\n'2':          add coal"
          "\n'3':          make steam"
          "\n'4':          accelerate"
          "\n'5':          brake"
          "\n'quit':       exits.")
    show_menu = False


#  Test the steam locomotive
def test_loco(chosen_loco):
    while True:
        chosen_loco.start_engine()
        chosen_loco.make_steam()
        chosen_loco.accelerate()
        print(chosen_loco.get_speed(), chosen_loco.get_resources())
        pygame.time.wait(500)


# Main
def main():
    chosen_loco = start_menu(loco_list)
    stat_menu(chosen_loco)
    show_menu()
    test_loco(chosen_loco)


main()


# Make loco_01 selectable as 1 instead of 0, loco_02 as 2 instead of 1, etc.
# Deplete steam when accelerating.