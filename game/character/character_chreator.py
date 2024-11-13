# character_creator.py

import random
from inventory import CharacterInventory

class Character:
    def __init__(self, name, age, race, gender, birthday, body_type, height, weight, background, family, special_stats, new_points, health, lvl):
        self.name = name
        self.age = age
        self.race = race
        self.gender = gender
        self.birthday = birthday
        self.body_type = body_type
        self.height = height
        self.weight = weight
        self.background = background
        self.family = family
        self.special_stats = special_stats
        self.new_points = new_points
        self.health = health
        self.lvl = lvl

def select_option(options, prompt):
    while True:
        try:
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
        except Exception as e:
            print(f"An error occurred: {e}")

def create_character():
    try:
        print("Welcome to Wasteland Wanderer Character Creation!")
        while True:
            name_input = input("Enter your character's name in the format (F: name, M: name, L: name, N: name): ").strip()
            if name_input:
                name_parts = name_input.split(", ")
                first_name, middle_name, last_name, nickname = "", "", "", ""
                
                valid_format = True
                for part in name_parts:
                    if part.startswith("F: "):
                        first_name = part[3:].strip()
                    elif part.startswith("M: "):
                        middle_name = part[3:].strip()
                    elif part.startswith("L: "):
                        last_name = part[3:].strip()
                    elif part.startswith("N: "):
                        nickname = part[3:].strip()
                    else:
                        valid_format = False
                        print("Invalid input. Please use the format (F: name, M: name, L: name, N: name).")
                        break
                
                if valid_format and any([first_name, middle_name, last_name, nickname]):
                    break
                print("Please provide at least one valid name.")
            else:
                print("Name input cannot be empty. Please enter a valid name.")
        
        age = select_age()
        race = select_race()
        gender = select_gender()
        body_type = select_body_type()
        height = select_height()
        weight = select_weight()
        special_stats = assign_special_stats()
        background = generate_random_details(gender, age, race, body_type, height, weight, special_stats)
        health = calculate_health()
        lvl = 1
        family = FM()

        player = Character(f"{first_name} {middle_name} {last_name} ({nickname})".strip(), age, race, gender, body_type, height, weight, background, family, special_stats, health, lvl)
        player.inventory = CharacterInventory()  # Automatically add inventory
        return player
    except Exception as e:
        print(f"An error occurred: {e}")

def select_race():
    races = ["Vault Dweller", "Wasteland Survivor", "Raider", "Ghoul", "Robot", "Mutant"]
    return select_option(races, "Choose your race:")

def select_gender():
    genders = ["Male", "Female"]
    return select_option(genders, "Choose your gender:")

def select_body_type():
    body_types = ["Lean", "Average", "Athletic", "Bulky"]
    return select_option(body_types, "Choose your body type:")

def select_height():
    while True:
        try:
            print("Enter your height in feet (3 to 12):")
            height = input("> ").strip()
            height = float(height)
            if 3 <= height <= 12:
                return height
            print("Invalid input. Please enter a height between 3 and 12 feet.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An error occurred: {e}")

def select_age():
    while True:
        try:
            print("Enter your age (1 to 212):")
            age = input("> ").strip()
            age = int(age)
            if 1 <= age <= 212:
                return age
            print("Invalid input. Please enter an age between 1 and 212 years.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
        except Exception as e:
            print(f"An error occurred: {e}")

def generate_random_details():
    try:
        # Placeholder for actual implementation
        # Add your code here
    except Exception as e:
        print(f"An error occurred: {e}")

def assign_special_stats():
    try:
        print("Assign your S.P.E.C.I.A.L stats (each stat starts at 1, total additional points: 21, max points per stat: 20):")
        stats = ["Strength", "Perception", "Endurance", "Charisma", "Intelligence", "Agility", "Luck"]
        special_stats = {stat: 1 for stat in stats}  # Initialize all stats to 1
        total_points = 21  # Total points available to distribute

        for stat in stats:
            while True:
                try:
                    print(f"Assign points to {stat} (remaining points: {total_points}):")
                    points = int(input("> ").strip().lower())
                    if 0 <= points <= total_points and special_stats[stat] + points <= 20:
                        special_stats[stat] += points
                        total_points -= points
                        break
                    print("Invalid input. Please enter a value within the available points and ensure the total does not exceed 20 for any stat.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
                except Exception as e:
                    print(f"An error occurred: {e}")

    
    except Exception as e:
        print(f"An error occurred: {e}")

def calculate_health():
    # Placeholder for actual implementation
    # Add your code here
    return HP

def select_weight():
    # Placeholder for actual implementation
    # Add your code here
    return weight

def FM():
    # Placeholder for actual implementation
    return Family


