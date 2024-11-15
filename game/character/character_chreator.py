# character_creator.py

import random
from inventory import CharacterInventory

class Character:
    def __init__(self, name, age, race, gender, birthday, body_type, height, weight, background, family, special_stats, new_points,total_points, health, lvl):
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
        self.total_points = total_points
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
    body_types = ["Emaciated", "Bony", "Lean", "Fit", "Athletic", "Average", "Stocky", "Bulky", "Chubby", "Fat"]
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
    while True:
        print("Assign your S.P.E.C.I.A.L stats (each stat starts at 1, total additional points: 21, max points per stat: 20):")
        New_points = 0
        total_points = 21  # Total points available to distribute
        stat_inputs = input(f"distribute your {total_points} stats, please use the format (S: stat, P: stat, E: stat, C: stat, I: stat, A: stat, L: stat):\n")
        stats = [["Strength", 1], ["Perception", 1], ["Endurance", 1], ["Charisma", 1], ["Intelligence", 1], ["Agility", 1], ["Luck", 1]]
        Strength_stat, Perception_stat, Endurance_stat, Charisma_stat, Intelligence_stat, Agility_stat, Luck_stat = "0", "0", "0", "0", "0", "0", "0"
        if stat_inputs:
            stat_parts = stat_inputs.split(", ")
            valid_format = True

            for st in stat_parts:
                if st.startswith("S: "):
                    try:
                        Strength_stat = st[3:].strip()
                        stats[0][1] = int(stats[0][1]) + int(st[3:].strip())
                        if 0 < int(stats[0][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("P: "):
                    try:
                        Perception_stat = st[3:].strip()
                        stats[1][1] = int(stats[1][1]) + int(st[3:].strip())
                        if 0 < int(stats[1][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("E: "):
                    try:
                        Endurance_stat = st[3:].strip()
                        stats[2][1] = int(stats[2][1]) + int(st[3:].strip())
                        if 0 < int(stats[2][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("C: "):
                    try:
                        Charisma_stat = st[3:].strip()
                        stats[3][1] = int(stats[3][1]) + int(st[3:].strip())
                        if 0 < int(stats[3][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("I: "):
                    try:
                        Intelligence_stat = st[3:].strip()
                        stats[4][1] = int(stats[4][1]) + int(st[3:].strip())
                        if 0 < int(stats[4][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("A: "):
                    try:
                        Agility_stat = st[3:].strip()
                        stats[5][1] = int(stats[5][1]) + int(st[3:].strip())
                        if 0 < int(stats[5][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("L: "):
                    try:
                        Luck_stat = st[3:].strip()
                        stats[6][1] = int(stats[6][1]) + int(st[3:].strip())
                        if 0 < int(stats[6][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                else:
                    valid_format = False
                    print("Invalid input. please use the format (S: stat, P: stat, E: stat, C: stat, I: stat, A: stat, L: stat).")
                    break
            if valid_format and any([Strength_stat, Perception_stat, Endurance_stat, Charisma_stat, Intelligence_stat, Agility_stat, Luck_stat]):
                Va = True
                if int(Strength_stat) + int(Perception_stat) + int(Endurance_stat) + int(Charisma_stat) + int(Intelligence_stat) + int(Agility_stat) + int(Luck_stat) < int(total_points):
                    New_points = int(New_points) + (int(total_points) - (int(Strength_stat) + int(Perception_stat) + int(Endurance_stat) + int(Charisma_stat) + int(Intelligence_stat) + int(Agility_stat) + int(Luck_stat)))
                    while True:
                        print(stats)
                        YorN = input(f"you still have {New_points} points to spend, would you like to spend them? Y/N:\n").upper()
                        if YorN == "Y":
                            break
                        elif YorN == "N":
                            Va = False
                            break
                        else:
                            print("invalid input use Y/N")
                    if Va == False:
                        break
                elif int(Strength_stat) + int(Perception_stat) + int(Endurance_stat) + int(Charisma_stat) + int(Intelligence_stat) + int(Agility_stat) + int(Luck_stat) > int(total_points):
                    print("too many points distributed. try again")
                else: 
                    print(stats)
                    break
            print("Please provide at least one valid stat.")
        else:
            print("Stats input cannot be empty. Please distribute your stats.")

def calculate_health(special_stats):
    base_health = 90
    endurance_points = special_stats.get("Endurance", 0)
    strength_points = special_stats.get("Strength", 0)
    max_health = base_health + (endurance_points * 10)
    strength_multiplier = 1 + (strength_points / 100)
    max_health = int(max_health * strength_multiplier)
    return max_health

def select_weight(race, gender, height, body_type):
    body_type_weights = {
        "Emaciated": 100,
        "Bony": 120,
        "Lean": 140,
        "Fit": 160,
        "Athletic": 180,
        "Average": 200,
        "Stocky": 220,
        "Bulky": 240,
        "Chubby": 260,
        "Fat": 280
    }

    race_multipliers = {
        "Vault Dweller": 1,
        "Wasteland Survivor": 1,
        "Raider": 1,
        "Ghoul": 1.2,
        "Mutant": 1.75,
        "Robot": 2
    }

    gender_multipliers = {
        "Male": 1,
        "Female": 0.75
    }

    base_weight = body_type_weights.get(body_type, 200)
    race_multiplier = race_multipliers.get(race, 1)
    gender_multiplier = gender_multipliers.get(gender, 1)
    height_multiplier = 1 + (height - 3) / 9 * 2.5  # Scales from 1 at 3 feet to 3.5 at 12 feet

    weight = base_weight * race_multiplier * gender_multiplier * height_multiplier

    return weight

def FM():
    # Placeholder for actual implementation
    return Family


create_character()