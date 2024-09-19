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


def select_destination(station_list):
    print("\n--- Select Destination Station ---")
    for i, station in enumerate(station_list, start=1):
        print(f"\n{i}: {station.name}")
    
    selected_index = -1
    while selected_index < 1 or selected_index > len(station_list):
        try:
            selected_index = int(input("\nEnter the number of the desired station: "))
            if selected_index < 1 or selected_index > len(station_list):
                print("No station with that number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    
    chosen_station = station_list[selected_index - 1]
    print(f"\nYou have chosen: {chosen_station.name}")
    return chosen_station


def calculate_distance(start_position, end_position):
    return abs(end_position - start_position)  # there is an error here, fix it later


def move_locomotive(loco, destination_station):
    distance = calculate_distance(loco.position, destination_station.distance)
    print(f"\nMoving {loco.name} from {loco.position} to {destination_station.distance}")
    print(f"\nDistance to travel: {distance} miles")

    while loco.position < destination_station.distance:
        loco.start_engine()
        if loco.current_coal > 0 and loco.current_water > 0:
            loco.make_steam()
            if loco.current_steam >= loco.max_steam:
                loco.accelerate()
                loco.position += 0.1  # Move 1 mile at a time
                print(f"Speed: {loco.current_speed}, {loco.get_resources()}, Position: {loco.position}")
                pygame.time.wait(500)  # Simulate time delay
            else:
                print(f"Generating steam... ({loco.current_steam})")
                pygame.time.wait(500)  # Simulate time delay for steam generation
        else:
            print("Out of resources! The locomotive cannot move further.")
            break

    if loco.position >= destination_station.distance:
        loco.position = destination_station.distance
        print(f"\n{loco.name} has arrived at {destination_station.name}")


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
        print(chosen_loco.current_speed, chosen_loco.get_resources())
        pygame.time.wait(500)


# Main loop
def main():
    chosen_loco = loco_menu(loco_list)

    start_game(chosen_loco)

    destination_station = select_destination(station_list)

    move_locomotive(chosen_loco, destination_station)


main()