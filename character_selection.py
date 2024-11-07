import random

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

def reallocate_points(special_stats, total_points):
    try:
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
                        print("Invalid input. Please enter a value within the available points.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
            else:
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
                        if 0 <= points <= total_points and special_stats[stat_choice.capitalize()] + points <= 20:
                            special_stats[stat_choice.capitalize()] += points
                            total_points -= points
                            break
                        print("Invalid input. Please enter a value within the available points and ensure the total does not exceed 20 for any stat.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
            else:
                print(f"Invalid input. Available points: {special_stats[stat_choice.capitalize()]}")

        # Additional prompt to move points from one stat to another
        while input("Do you want to move points from one stat to another? (yes/no) > ").strip().lower() == 'yes':
            print("Move points from one stat to another.")
            from_stat = input("Choose a stat to move points from: ").strip().lower()
            to_stat = input("Choose a stat to move points to: ").strip().lower()
            if from_stat.capitalize() in special_stats and to_stat.capitalize() in special_stats:
                while True:
                    try:
                        points = int(input(f"How many points do you want to move from {from_stat.capitalize()} to {to_stat.capitalize()}? > "))
                        if 1 <= special_stats[from_stat.capitalize()] - points and special_stats[to_stat.capitalize()] + points <= 20:
                            special_stats[from_stat.capitalize()] -= points
                            special_stats[to_stat.capitalize()] += points
                            break
                        print("Invalid input. Ensure no stat goes below 1 and no stat exceeds 20.")
                    except ValueError:
                        print("Invalid input. Please enter a numeric value.")
                    except Exception as e:
                        print(f"An error occurred: {e}")
            else:
                print("Invalid stat choices. Please enter valid stat names.")
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

        if input("Do you want to reallocate your S.P.E.C.I.A.L points? (yes/no) > ").strip().lower() == 'yes':
            reallocate_points(special_stats, total_points)

        return special_stats
    except Exception as e:
        print(f"An error occurred: {e}")

def display_random_stats(special_stats):
    print("Randomly assigned S.P.E.C.I.A.L stats:")
    for stat, value in special_stats.items():
        print(f"{stat}: {value}")

def create_character():
    try:
        print("Welcome to Wasteland Wanderer Character Creation!")
        while True:
            try:
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
            except Exception as e:
                print(f"An error occurred: {e}")
        
        age = select_age()
        player_class = select_class()
        gender = select_gender()
        body_type = select_body_type()
        height = select_height()
        special_stats = assign_special_stats()
        weight, background, family = generate_random_details(gender, age, player_class, body_type, height, special_stats)

        player = Player(f"{first_name} {middle_name} {last_name} ({nickname})".strip(), age, player_class, gender, body_type, height, weight, background, family, special_stats)

        return player
    except Exception as e:
        print(f"An error occurred: {e}")

def generate_random_details(gender, age, player_class, body_type, height, special_stats):
    try:
        weight = random.randint(90, 300)  # Weight in pounds

        backgrounds = {
            "Male": [
                "Grew up in a Vault, trained in survival tactics.",
                "Wasteland native, knows every nook and cranny.",
                "Former Raider, trying to find redemption.",
                "Was a scientist before the bombs fell.",
                "Engineered robot with human-like traits.",
                "Mutant outcast, seeking acceptance.",
                "Escaped from a dangerous gang.",
                "Healer in a small survivor community.",
                "Expert trader with connections everywhere.",
                "Retired soldier with a mysterious past.",
                "A young genius, proficient in hacking systems.",
                "A skilled mechanic who can repair almost anything.",
                "A former athlete, known for his endurance and strength.",
                "A bounty hunter seeking his next target.",
                "A farmer trying to bring life back to the wasteland."
            ],
            "Female": [
                "Grew up in a Vault, trained in survival tactics.",
                "Wasteland native, knows every nook and cranny.",
                "Former Raider, trying to find redemption.",
                "Was a scientist before the bombs fell.",
                "Engineered robot with human-like traits.",
                "Mutant outcast, seeking acceptance.",
                "Escaped from a dangerous gang.",
                "Healer in a small survivor community.",
                "Expert trader with connections everywhere.",
                "Former mercenary now seeking a peaceful life.",
                "A seasoned warrior with decades of experience.",
                "A skilled hunter and tracker.",
                "A former medic who tends to the wounded.",
                "A technician with a knack for electronics.",
                "A scavenger who can find useful items in any ruin."
            ],
            "Non-binary": [
                "Grew up in a Vault, trained in survival tactics.",
                "Wasteland native, knows every nook and cranny.",
                "Former Raider, trying to find redemption.",
                "Was a scientist before the bombs fell.",
                "Engineered robot with human-like traits.",
                "Mutant outcast, seeking acceptance.",
                "Escaped from a dangerous gang.",
                "Healer in a small survivor community.",
                "Expert trader with connections everywhere.",
                "Technological genius with a dark secret.",
                "A wanderer seeking knowledge.",
                "A mysterious figure with a hidden past.",
                "A skilled diplomat who can talk their way out of trouble.",
                "A drifter with no ties to any community.",
                "A builder trying to create a safe haven in the wasteland."
            ]
        }

        families = {
            "Male": [
                "Lost their family to the wasteland.",
                "Trying to reunite with a lost sibling.",
                "Traveling with a loyal canine companion.",
                "Searching for their kidnapped child.",
                "Orphaned at a young age, raised by a mentor.",
                "Living with a small group of survivors.",
                "Only surviving member of their original Vault.",
                "Protecting a group of young orphans.",
                "Estranged from their wealthy family.",
                "Living with a ragtag group of wanderers.",
                "Traveling with an elderly mentor.",
                "Living with fellow athletes, surviving on their skills.",
                "Formed a family with other bounty hunters.",
                "Searching for lost family members in the wasteland.",
                "Living with a farming community."
            ],
            "Female": [
                "Lost their family to the wasteland.",
                "Trying to reunite with a lost sibling.",
                "Traveling with a loyal canine companion.",
                "Searching for their kidnapped child.",
                "Orphaned at a young age, raised by a mentor.",
                "Living with a small group of survivors.",
                "Only surviving member of their original Vault.",
                "Protecting a group of young orphans.",
                "Estranged from their wealthy family.",
                "Living with a group of scientist exiles.",
                "Acting as a leader for young survivors.",
                "Living with other warriors, forming a protective group.",
                "Caring for wounded members of a survivor group.",
                "Working with a team of technicians.",
                "Living with a community of scavengers."
            ],
            "Non-binary": [
                "Lost their family to the wasteland.",
                "Trying to reunite with a lost sibling.",
                "Traveling with a loyal canine companion.",
                "Searching for their kidnapped child.",
                "Orphaned at a young age, raised by a mentor.",
                "Living with a small group of survivors.",
                "Only surviving member of their original Vault.",
                "Protecting a group of young orphans.",
                "Estranged from their wealthy family.",
                "Living with a caravan of traders.",
                "Living with a community of ghouls in an old metro station.",
                "A part of a knowledge-seeking group of wanderers.",
                "A drifter moving from one community to another.",
                "Forming a new family with other builders.",
                "Living with a group of diplomatic mediators."
            ]
        }

        # Additional details based on character traits
        if age < 18:
            backgrounds[gender].append("A young prodigy, known for exceptional intellect.")
            families[gender].append("Traveling with a protective guardian.")
        elif age > 60:
            backgrounds[gender].append("A wise elder, respected for their experience.")
            families[gender].append("Leading a group of young explorers.")

        if player_class == "Ghoul":
            backgrounds[gender].append("Once a human, now a ghoul seeking redemption.")
            families[gender].append("Living with a community of ghouls in an old metro station.")

        if body_type == "Athletic":
            backgrounds[gender].append("Former athlete, known for their endurance and strength.")
            families[gender].append("Traveling with fellow athletes, surviving on their skills.")

        if special_stats["Strength"] > 8:
            backgrounds[gender].append("Renowned for their incredible strength, a protector of the weak.")
            families[gender].append("Living with other strong individuals, forming a protective group.")

        # Adding height-related backgrounds
        if height > 6:
            backgrounds[gender].append("A towering figure, often intimidating to others.")
            families[gender].append("Part of a group known for their exceptional height.")

        # Class-specific backgrounds and families
        if player_class == "Vault Dweller":
            backgrounds[gender].append("Raised in the safety of a Vault, now exploring the outside world.")
            families[gender].append("A Vault family, protected from the horrors of the wasteland.")
        elif player_class == "Wasteland Survivor":
            backgrounds[gender].append("Grew up in the harsh wasteland, learning to survive.")
            families[gender].append("A hardy family, adapted to the wasteland's challenges.")
        elif player_class == "Raider":
            backgrounds[gender].append("Spent years as a Raider, taking what they needed.")
            families[gender].append("A group of Raiders, bound by loyalty and survival.")
        elif player_class == "Robot":
            backgrounds[gender].append("An advanced robot, designed for complex tasks.")
            families[gender].append("A network of robots, communicating and collaborating.")
        elif player_class == "Mutant":
            backgrounds[gender].append("A mutant with unique abilities, shunned by many.")
            families[gender].append("A group of mutants, living on the fringes of society.")

        background = random.choice(backgrounds[gender])
        family = random.choice(families[gender])

        return weight, background, family
    except Exception as e:
        print(f"An error occurred: {e}")

def display_character_sheet(player):
    try:
        print("\nCharacter Created!")
        name_display = " ".join(filter(None, [player.name.split("(")[0], "(" + player.name.split("(")[1] if "(" in player.name and player.name.split("(")[1].strip(")") else None]))
        print(f"Name: {name_display.strip()}")
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
            print(f"{stat}: {value}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    player = create_character()
    display_character_sheet(player)
    try:
        while True:
            print("\nWhat would you like to do next?")
            print("1. Reallocate S.P.E.C.I.A.L points")
            print("2. Change name")
            print("3. See stats")
            print("4. View background and family")
            print("5. Exit")
            choice = input("> ").strip().lower()

            if choice == "1":
                reallocate_points(player.special_stats, 0)
                display_character_sheet(player)
            elif choice == "2":
                player = create_character()
                display_character_sheet(player)
            elif choice == "3":
                display_character_sheet(player)
            elif choice == "4":
                print(f"Background: {player.background}")
                print(f"Family: {player.family}")
            elif choice == "5" or choice == "exit":
                print("Exiting character creation. Goodbye!")
                break
            else:
                print("Invalid input. Please select a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")