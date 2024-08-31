# Steam Engines v0.02

import pygame
import random
import math
from global_time import GlobalTime
from loco_steam import Loco_Steam

# Initialize global time
global_time = GlobalTime()


# Menu function
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


# Start menu to select a locomotive
def start_menu():
    loco_01 = Loco_Steam("Talyllyn", 0, 10, 0, 0, 0, 10, 10, 10)

    loco_list = [loco_01]

    print("Select a locomotive:")
    for i, loco in enumerate(loco_list):
        print(f"{i}: {loco.name}")

    selected_index = -1
    while selected_index < 0 or selected_index >= len(loco_list):
        try:
            selected_index = int(input("\nEnter the number of the desired locomotive: "))
            if selected_index < 0 or selected_index >= len(loco_list):
                print("Invalid selection. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    chosen_loco = loco_list[selected_index]
    print(f"\nYou have chosen: {chosen_loco.name}")
    return chosen_loco


show_menu()




    # #  Test the steam locomotive
    # loco_01.start_engine()
    # loco_01.make_steam()
    # loco_01.accelerate()
    # print(loco_01.get_speed())
    # pygame.time.wait(500)