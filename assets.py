valid_items = {
    "Clothes": ["Jumpsuit", "Leather Armor", "Combat Armor", "Raider Armor", "Hazmat Suit"],
    "Food": ["Canned Beans", "Cram", "BlamCo Mac & Cheese", "Nuka-Cola", "Brahmin Steak"],
    "Weapons": ["10mm Pistol", "Laser Rifle", "Super Sledge", "Combat Shotgun", "Plasma Grenade"],
    "Tools": ["Lockpick", "Repair Kit", "Geiger Counter", "Stimpak", "RadAway"],
    "Miscellaneous": ["Bottle Caps", "Pre-war Money", "Rad-X", "Mentats", "Holotape"]
}

def get_valid_items(category):
    return valid_items.get(category, [])

if __name__ == "__main__":
    for category, items in valid_items.items():
        print(f"{category}: {', '.join(items)}")