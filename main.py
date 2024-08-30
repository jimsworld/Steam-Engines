#  Steam Engines v0.02

import pygame
import random
import math
from global_time import GlobalTime
from loco_steam import Loco_Steam

# Initialize global time
global_time = GlobalTime()

# Initialize steam locomotive
loco_01 = Loco_Steam("Talyllyn", 0, 10, 0, 0, 0, 10, 10, 10)


show_menu = True

while True:

    # if show_instructions:
    #     print("\nEnter command:"
    #         "\n'help':    shows this menu"
    #         "\n'0':"
    #         "\n'1':"
    #         "\n'2':"
    #         "\n'3':"
    #         "\n'quit':    exits.")
    #     show_instructions = False  # Stops repetitive instructions

    # user_input = input("Enter command: ")
    # match user_input:

    loco_01.start_engine()
    loco_01.make_steam()
    loco_01.accelerate()
    print(loco_01.get_speed())
    pygame.time.wait(500)