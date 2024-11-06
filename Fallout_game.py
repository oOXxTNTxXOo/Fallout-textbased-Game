import os

# Import necessary functions from character_selection.py
from character_selection import create_character, display_character_sheet
# Assume lore_start sets up the game's starting year and map.
from lore_start import GAME_START_YEAR, create_starting_map

def start_game():
    characters = []
    print("Welcome to Fallout Wasteland Wanderer!")
    while True:
        print("\n1. Create a new character")
        print("2. View characters")
        print("3. Start game")
        print("4. Exit")
        choice = input("> ").strip().lower()
        
        if choice == '1':
            character = create_character()
            characters.append(character)
        elif choice == '2':
            if not characters:
                print("\nNo characters created yet.")
            else:
                for i, character in enumerate(characters):
                    print(f"\nCharacter {i + 1}:")
                    display_character_sheet(character)
        elif choice == '3':
            if not characters:
                print("\nNo characters created yet. Please create a character first.")
            else:
                print("\nStarting the game with the following characters:")
                for character in characters:
                    display_character_sheet(character)
                # Start the main game script (assuming Fallout_game.py is the main game script)
                os.system('python Fallout_game.py')
                break
        elif choice == '4':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    start_game()
