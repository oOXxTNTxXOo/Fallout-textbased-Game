import json
import os
import random
from character_selection import create_character, display_character_sheet, reallocate_points, generate_random_character
from Ch_inventory import CharacterInventory, manage_inventory
from lore_start import GAME_START_YEAR, create_starting_map

class Player:
    def __init__(self, name, age, birth_year, player_class, gender, body_type, height, weight, background, family, special_stats):
        self.name = name
        self.age = age
        self.birth_year = birth_year
        self.player_class = player_class
        self.gender = gender
        self.body_type = body_type
        self.height = height
        self.weight = weight
        self.background = background
        self.family = family
        self.special_stats = special_stats
        self.inventory = CharacterInventory()

def calculate_birth_year(age):
    return GAME_START_YEAR - age

def main_menu():
    characters = []
    print("Welcome to Fallout Wasteland Wanderer!")
    
    while True:
        print("\n1. Create a new character")
        print("2. Generate a random character")
        print("3. View characters")
        print("4. Edit character stats and inventory")
        print("5. View character inventory")
        print("6. Start game")
        print("7. Exit")
        choice = input("> ").strip().lower()
        
        if choice == '1':
            character = create_character()
            birth_year = calculate_birth_year(character.age)
            character.birth_year = birth_year
            characters.append(character)
        elif choice == '2':
            character = generate_random_character()
            birth_year = calculate_birth_year(character.age)
            character.birth_year = birth_year
            characters.append(character)
            print("\nRandom Character Created:")
            display_character_sheet(character)
        elif choice == '3':
            if not characters:
                print("\nNo characters created yet.")
            else:
                for i, character in enumerate(characters):
                    print(f"\nCharacter {i + 1}: {character.name}")
                try:
                    char_index = int(input("Enter character number to view: ")) - 1
                    if 0 <= char_index < len(characters):
                        display_character_sheet(characters[char_index])
                    else:
                        print("Invalid character number.")
                except ValueError:
                    print("Invalid input. Please enter a valid character number.")
        elif choice == '4':
            if not characters:
                print("\nNo characters created yet.")
            else:
                for i, character in enumerate(characters):
                    print(f"\nCharacter {i + 1}: {character.name}")
                try:
                    char_index = int(input("Enter character number to edit: ")) - 1
                    if 0 <= char_index < len(characters):
                        char_choice = characters[char_index]
                        print("\n1. Edit Stats")
                        print("2. Manage Inventory")
                        edit_choice = input("> ").strip().lower()
                        if edit_choice == '1':
                            reallocate_points(char_choice.special_stats, 0)
                        elif edit_choice == '2':
                            manage_inventory(char_choice.inventory)
                        else:
                            print("Invalid choice.")
                    else:
                        print("Invalid character number.")
                except ValueError:
                    print("Invalid input. Please enter a valid character number.")
        elif choice == '5':
            if not characters:
                print("\nNo characters created yet.")
            else:
                for i, character in enumerate(characters):
                    print(f"\nCharacter {i + 1}: {character.name}")
                try:
                    char_index = int(input("Enter character number to view inventory: ")) - 1
                    if 0 <= char_index < len(characters):
                        display_character_sheet(characters[char_index], show_inventory=True)
                    else:
                        print("Invalid character number.")
                except ValueError:
                    print("Invalid input. Please enter a valid character number.")
        elif choice == '6':
            if not characters:
                print("\nNo characters created yet. Please create a character first.")
            else:
                start_event, start_location = create_starting_map()
                print(f"\nStarting Year: {GAME_START_YEAR}")
                print(f"Starting Event: {start_event}")
                print(f"Starting Location: {start_location}")
                
                for character in characters:
                    character.birth_year = calculate_birth_year(character.age)
                
                with open('characters.json', 'w') as file:
                    json.dump([char.__dict__ for char in characters], file)
                
                print("Game is now set up with the starting details. Proceeding to the game...")
                # Here you should have the main game loop or call another script to start the actual game play.
                # os.system('python main_game.py characters.json')
                break
        elif choice == '7':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main_menu()