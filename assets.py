valid_items = {
    "Clothes": ["Jumpsuit", "Leather Armor", "Combat Armor", "Raider Armor", "Hazmat Suit"],
    "Food": ["Canned Beans", "Cram", "BlamCo Mac & Cheese", "Nuka-Cola", "Brahmin Steak"],
    "Weapons": ["10mm Pistol", "Laser Rifle", "Super Sledge", "Combat Shotgun", "Plasma Grenade"],
    "Tools": ["Lockpick", "Repair Kit", "Geiger Counter", "Stimpak", "RadAway"],
    "Miscellaneous": ["Bottle Caps", "Pre-war Money", "Rad-X", "Mentats", "Holotape"]
}

enemies = [
    {"name": "Radroach", "difficulty": "Easy"},
    {"name": "Molerat", "difficulty": "Easy"},
    {"name": "Feral Ghoul", "difficulty": "Easy"},
    {"name": "Raiders", "difficulty": "Medium"},
    {"name": "Super Mutant", "difficulty": "Medium"},
    {"name": "Mr. Handy", "difficulty": "Medium"},
    {"name": "Radscorpion", "difficulty": "Hard"},
    {"name": "Deathclaw", "difficulty": "Hard"},
    {"name": "Sentry Bot", "difficulty": "Hard"},
    {"name": "Mirelurk", "difficulty": "Medium"},
    {"name": "Yao Guai", "difficulty": "Hard"},
    {"name": "Glowing One", "difficulty": "Hard"},
    {"name": "Assaultron", "difficulty": "Hard"},
    {"name": "Behemoth", "difficulty": "Very Hard"},
    {"name": "Liberty Prime", "difficulty": "Very Hard"},
    {"name": "Brotherhood Paladin", "difficulty": "Medium"},
    {"name": "Enclave Soldier", "difficulty": "Medium"},
    {"name": "Synth", "difficulty": "Medium"},
    {"name": "Cazador", "difficulty": "Hard"},
    {"name": "Nightkin", "difficulty": "Medium"},
    {"name": "Lobotomite", "difficulty": "Medium"},
    {"name": "Tunnelers", "difficulty": "Hard"},
    {"name": "Giant Ant", "difficulty": "Easy"},
    {"name": "Fog Crawler", "difficulty": "Hard"},
    {"name": "Swampfolk", "difficulty": "Medium"},
    {"name": "Zetan Alien", "difficulty": "Hard"},
    {"name": "Mothman", "difficulty": "Very Hard"},
    {"name": "Scorched Beast", "difficulty": "Very Hard"},
    {"name": "Wendigo", "difficulty": "Hard"},
    {"name": "Gulpers", "difficulty": "Medium"}
]

perk_cards = {
    "Strong Back": {"strength": 2, "endurance": 1},
    "Toughness": {"endurance": 3},
    "Bloody Mess": {"combat_ability": 5},
    "Ninja": {"agility": 2, "perception": 2},
    "Lifegiver": {"health": 20},
    "Action Boy/Action Girl": {"agility": 3}
}

def get_valid_items(category):
    return valid_items.get(category, [])

if __name__ == "__main__":
    for category, items in valid_items.items():
        print(f"{category}: {', '.join(items)}")

    print("\nEnemies:")
    for enemy in enemies:
        print(f"{enemy['name']} - Difficulty: {enemy['difficulty']}")

    print("\nPerk Cards:")
    for perk, stats in perk_cards.items():
        print(f"{perk}: {stats}")
