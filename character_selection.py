import random

# Import GAME_START_YEAR from lore_start.py
from lore_start import GAME_START_YEAR

class Player:
    def __init__(self, name, age, player_class, gender, body_type, height, weight, background, family, special_stats):
        self.name = name
        self.age = age
        self.player_class = player_class
        self.gender = gender
        self.body_type = body_type
        self.height = height
        self.weight = weight
        self.background = background
        self.family = family
        self.special_stats = special_stats

def select_option(options, prompt):
    while True:
        print(prompt)
        for i, option in enumerate(options):
            print(f"{i + 1}. {option}")
        choice = input("> ").strip().lower()
        
        # Handle numeric input
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        
        # Handle string input
        for option in options:
            if choice == option.lower():
                return option
        
        print("Invalid input. Please select a valid option.")

def select_class():
    classes = ["Vault Dweller", "Wasteland Survivor", "Raider", "Ghoul", "Robot", "Mutant"]
    return select_option(classes, "Choose your class:")

def select_gender():
    genders = ["Male", "Female", "Non-binary"]
    return select_option(genders, "Choose your gender:")

def select_body_type():
    body_types = ["Lean", "Average", "Athletic", "Bulky"]
    return select_option(body_types, "Choose your body type:")

def select_height():
    while True:
        print("Enter your height in feet (3 to 12):")
        height = input("> ").strip()
        try:
            height = float(height)
            if 3 <= height <= 12:
                return height
        except ValueError:
            pass
        print("Invalid input. Please enter a height between 3 and 12 feet.")

def select_age():
    while True:
        print("Enter your age (1 to 212):")
        age = input("> ").strip()
        try:
            age = int(age)
            if 1 <= age <= 212:
                return age
        except ValueError:
            pass
        print("Invalid input. Please enter an age between 1 and 212 years.")

def reallocate_points(special_stats, total_points):
    while True:
        print(f"Reallocate points (total points left: {total_points}):")
        for stat, value in special_stats.items():
            print(f"{stat}: {value}")
        stat_choice = input("Choose a stat to reallocate points from (or type 'done' to finish): ").strip().lower()
        if stat_choice == 'done':
            break
        if stat_choice.capitalize() in special_stats:
            while True:
                try:
                    print(f"Reallocate points from {stat_choice.capitalize()}: ")
                    points = int(input("> "))
                    if 0 <= points <= special_stats[stat_choice.capitalize()]:
                        special_stats[stat_choice.capitalize()] -= points
                        total_points += points
                        break
                except ValueError:
                    pass
        print(f"Invalid input. Available points: {special_stats[stat_choice.capitalize()]}")

    while total_points > 0:
        for stat, value in special_stats.items():
            print(f"{stat}: {value}")
        print(f"Points left to allocate: {total_points}")
        stat_choice = input("Choose a stat to allocate points to: ").strip().lower()
        if stat_choice.capitalize() in special_stats:
            while True:
                try:
                    print(f"Allocate points to {stat_choice.capitalize()}: ")
                    points = int(input("> "))
                    if 0 <= points <= total_points:
                        special_stats[stat_choice.capitalize()] += points
                        total_points -= points
                        break
                except ValueError:
                    pass
        print(f"Invalid input. Points left: {total_points}")

def assign_special_stats():
    print("Assign your S.P.E.C.I.A.L stats (each stat starts at 1, total additional points: 21):")
    stats = ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]
    special_stats = {stat: 1 for stat in stats}  # Initialize all stats to 1
    total_points = 21  # Total points available to distribute

    print("Do you want to allocate points manually or randomly? (Enter 'manual' or 'random')")
    choice = input("> ").strip().lower()
    
    if choice == 'random':
        while total_points > 0:
            stat = random.choice(stats)
            points = random.randint(1, min(10, total_points))
            special_stats[stat] += points
            total_points -= points
        return special_stats

    for stat in stats:
        while True:
            print(f"Assign additional points to {stat} (remaining points: {total_points}): (Base: {special_stats[stat]})")
            points = input("> ").strip().lower()
            if points.isdigit() and 0 <= int(points) <= total_points:
                special_stats[stat] += int(points)
                total_points -= int(points)
                break
            else:
                print(f"Invalid input. You have {total_points} points left.")
                
    return special_stats

def generate_random_details():
    weight = random.randint(90, 300)  # Weight in pounds
    backgrounds = [
        "Grew up in a Vault, trained in survival tactics.",
        "Wasteland native, knows every nook and cranny.",
        "Former Raider, trying to find redemption.",
        "Was a scientist before the bombs fell.",
        "Engineered robot with human-like traits.",
        "Mutant outcast, seeking acceptance.",
        "Escaped from a dangerous gang.",
        "Healer in a small survivor community.",
        "Expert trader with connections everywhere."
    ]
    families = [
        "Lost their family to the wasteland.",
        "Trying to reunite with a lost sibling.",
        "Traveling with a loyal canine companion.",
        "Searching for their kidnapped child.",
        "Orphaned at a young age, raised by a mentor.",
        "Living with a small group of survivors.",
        "Only surviving member of their original Vault.",
        "Protecting a group of young orphans.",
        "Estranged from their wealthy family."
    ]
    background = random.choice(backgrounds)
    family = random.choice(families)
    
    return weight, background, family

def create_character():
    print("Welcome to Wasteland Wanderer Character Creation!")
    name = input("Enter your character's name: ").strip()
    age = select_age()
    player_class = select_class()
    gender = select_gender()
    body_type = select_body_type()
    height = select_height()
    special_stats = assign_special_stats()
    weight, background, family = generate_random_details()
    
    player = Player(name, age, player_class, gender, body_type, height, weight, background, family, special_stats)
    
    return player

def display_character_sheet(player):
    print("\nCharacter Created!")
    print(f"Name: {player.name}")
    print(f"Age: {player.age}")
    print(f"Class: {player.player_class}")
    print(f"Gender: {player.gender}")
    print(f"Body Type: {player.body_type}")
    print(f"Height: {player.height:.2f} feet")
    print(f"Weight: {player.weight} lbs")
    print(f"Background: {player.background}")
    print(f"Family: {player.family}")
    print("S.P.E.C.I.A.L Stats:")
    for stat, value in player.special_stats.items():
        print(f"{stat}: {value} (Base: 1)")

if __name__ == "__main__":
    player = create_character()
    display_character_sheet(player)
    print("\nDo you want to reallocate your S.P.E.C.I.A.L points? (yes/no)")
    if input("> ").strip().lower() == "yes":
        reallocate_points(player.special_stats, 0)
        display_character_sheet