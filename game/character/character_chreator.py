# character_creator.py

import random
from inventory import CharacterInventory

class Character:
    def __init__(self, name, age, race, gender, birthday, body_type, height, weight, background, family, special_stats, health, lvl):
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
        player_class = select_class()
        gender = select_gender()
        body_type = select_body_type()
        height = select_height()
        special_stats = assign_special_stats()
        weight, background, family = generate_random_details(gender, age, player_class, body_type, height, special_stats)

        player = Character(f"{first_name} {middle_name} {last_name} ({nickname})".strip(), age, player_class, gender, body_type, height, weight, background, family, special_stats, health=None, lvl=1)
        player.inventory = CharacterInventory()  # Automatically add inventory
        return player
    except Exception as e:
        print(f"An error occurred: {e}")

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
        # Placeholder for actual implementation
        # Add your code here
    except Exception as e:
        print(f"An error occurred: {e}")
