import pygame
import random
import math
from global_time import GlobalTime
from loco_steam import loco_list
from stations import station_list

# Initialize global time
global_time = GlobalTime()

# Start menu to select a locomotive
def loco_menu(loco_list):
    
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


# Prepare the locomotive with coal and water
def prepare_loco(chosen_loco):
    add_coal = input("\nAdd Coal?"
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
    
    add_water = input("\nAdd Water?"
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


# Stat menu to display the locomotive stats
def stat_menu(chosen_loco):
    print(f"\n--- {chosen_loco.name} Stats ---\n"
            f"\nMax Coal: {chosen_loco.max_coal}"
            f"\nMax Water: {chosen_loco.max_water}"
            f"\nMax Steam: {chosen_loco.max_steam}"
            f"\nMax Speed: {chosen_loco.max_speed}")


# Command list
def command_list():
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


# Start the game
def start_game(chosen_loco):
    print("\nLet's get ready..."
            "\nWhat would you like to do?\n"
            "\n'1': Prepare your locomotive"
            "\n'2': View your locomotive stats"
            "\n'3': View Station Map"
            "\n'0': Confirm and Start"
            "\n'help': Show commands")

    def start_menu(chosen_loco):
        while True:
            start_menu_choice = input("\n> ")
            match start_menu_choice:
                case "1":
                    prepare_loco(chosen_loco)
                    print("\nPreperations complete. What would you like to do?")
                case "2":
                    stat_menu(chosen_loco)
                case "3":
                    print("Station Map coming soon.")
                case "help":
                    command_list()
                case "0":
                    break
                case _:
                    print("Invalid command. Please try again.")

    
    start_menu(chosen_loco)


#  Test the steam locomotive
def test_loco(chosen_loco):
    while True:
        chosen_loco.start_engine()
        chosen_loco.make_steam()
        print(chosen_loco.get_speed(), chosen_loco.get_resources())
        pygame.time.wait(500)


# Main loop
def main():
    chosen_loco = loco_menu(loco_list)

    start_game(chosen_loco)

    test_loco(chosen_loco)


main()