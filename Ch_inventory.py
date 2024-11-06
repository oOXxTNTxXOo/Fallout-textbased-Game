class Inventory:
    def __init__(self):
        self.items = {
            "clothes": [],
            "food": [],
            "weapons": [],
            "tools": [],
            "miscellaneous": []
        }

    def add_item(self, category, item):
        if category in self.items:
            self.items[category].append(item)
        else:
            print(f"Category {category} does not exist.")

    def remove_item(self, category, item):
        if category in self.items:
            if item in self.items[category]:
                self.items[category].remove(item)
            else:
                print(f"Item {item} not found in category {category}.")
        else:
            print(f"Category {category} does not exist.")

    def view_inventory(self):
        print("Inventory:")
        for category, items in self.items.items():
            print(f"\n{category.capitalize()}:")
            for item in items:
                print(f"- {item}")

def manage_inventory(inventory):
    while True:
        print("\nInventory Management:")
        print("1. View inventory")
        print("2. Add item")
        print("3. Remove item")
        print("4. Exit")
        choice = input("> ").strip().lower()

        if choice == '1':
            inventory.view_inventory()
        elif choice == '2':
            category = input("Enter category (clothes, food, weapons, tools, miscellaneous): ").strip().lower()
            item = input("Enter item name: ").strip()
            inventory.add_item(category, item)
        elif choice == '3':
            category = input("Enter category (clothes, food, weapons, tools, miscellaneous): ").strip().lower()
            item = input("Enter item name: ").strip()
            inventory.remove_item(category, item)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please select a valid option.")
