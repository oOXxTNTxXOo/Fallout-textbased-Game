from assets import get_valid_items

class CharacterInventory:
    def __init__(self):
        self.inventory = {
            'Clothes': [],
            'Food': [],
            'Weapons': [],
            'Tools': [],
            'Miscellaneous': []
        }

    def view_inventory(self):
        print("\nInventory:")
        for category, items in self.inventory.items():
            print(f"{category}: {', '.join(items) if items else 'None'}")

    def show_category_inventory(self, category):
        items = self.inventory.get(category, [])
        print(f"\nCurrent {category} Inventory: {', '.join(items) if items else 'None'}")

    def add_item(self, category, item):
        valid_categories = self.inventory.keys()
        if category in valid_categories:
            valid_items = get_valid_items(category)
            if item in valid_items:
                self.inventory[category].append(item)
                print(f"Added {item} to {category}.")
                self.show_category_inventory(category)
            else:
                print(f"Invalid item. Valid items for {category} are: {', '.join(valid_items)}")
        else:
            print("Invalid category. Please choose a valid category.")
            print(f"Valid categories are: {', '.join(valid_categories)}")

    def remove_item(self, category, item):
        if category in self.inventory:
            if item in self.inventory[category]:
                self.inventory[category].remove(item)
                print(f"Removed {item} from {category}.")
                self.show_category_inventory(category)
            else:
                print(f"{item} not found in {category}.")
        else:
            print("Invalid category. Please choose a valid category.")

def manage_inventory(inventory):
    try:
        while True:
            print("\nInventory Management:")
            print("1. View Inventory")
            print("2. Add Item")
            print("3. Remove Item")
            print("4. Exit Inventory")
            choice = input("> ").strip()

            if choice == "1":
                inventory.view_inventory()
            elif choice == "2":
                category = input("Enter the category (Clothes, Food, Weapons, Tools, Miscellaneous): ").strip()
                if category in inventory.inventory:
                    inventory.show_category_inventory(category)
                    item = input("Enter the item name: ").strip()
                    inventory.add_item(category, item)
                else:
                    print("Invalid category. Please choose a valid category.")
            elif choice == "3":
                category = input("Enter the category (Clothes, Food, Weapons, Tools, Miscellaneous): ").strip()
                if category in inventory.inventory:
                    inventory.show_category_inventory(category)
                    item = input("Enter the item name: ").strip()
                    inventory.remove_item(category, item)
                else:
                    print("Invalid category. Please choose a valid category.")
            elif choice == "4":
                print("Exiting inventory management.")
                break
            else:
                print("Invalid input. Please choose a valid option.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    character_inventory = CharacterInventory()
    manage_inventory(character_inventory)
