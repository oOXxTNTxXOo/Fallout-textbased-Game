import random

# Random starting events based on Fallout lore
starting_events = [
    "You wake up in Vault 101, ready to explore the outside world for the first time.",
    "You find yourself in Megaton, a town built around an undetonated nuclear bomb.",
    "You are in Rivet City, a sprawling ship-turned-city on the Potomac River.",
    "You emerge from Vault 13, a legend among the wasteland survivors.",
    "You are a courier left for dead in the Mojave Desert, ready to seek revenge.",
    "You start in the ruins of the Capital Wasteland, amidst the broken monuments of Washington, D.C."
]

# Map locations based on Fallout lore
map_locations = [
    "Vault 101",
    "Megaton",
    "Rivet City",
    "Vault 13",
    "Mojave Desert",
    "Capital Wasteland",
    "New Vegas Strip",
    "Goodneighbor",
    "Diamond City",
    "Far Harbor",
    "Nuka-World",
    "The Institute"
]

def get_random_start_event():
    return random.choice(starting_events)

def get_random_start_location():
    return random.choice(map_locations)

def create_starting_map():
    start_event = get_random_start_event()
    start_location = get_random_start_location()
    return start_event, start_location

def get_starting_year():
    while True:
        try:
            year = int(input("Enter the starting year (e.g., 2277): ").strip())
            return year
        except ValueError:
            print("Invalid input. Please enter a valid year.")

if __name__ == "__main__":
    GAME_START_YEAR = get_starting_year()
    start_event, start_location = create_starting_map()
    print(f"Starting Year: {GAME_START_YEAR}")
    print(f"Starting Event: {start_event}")
    print(f"Starting Location: {start_location}")
