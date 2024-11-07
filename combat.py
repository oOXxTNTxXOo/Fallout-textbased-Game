import random
from assets import valid_items, perk_cards, enemies

class CombatAbilities:
    def __init__(self, weight, player_class, strength, gender, weapons, age, body_type, height):
        self.weight = weight
        self.player_class = player_class
        self.strength = strength
        self.gender = gender
        self.weapons = weapons
        self.age = age
        self.body_type = body_type
        self.height = height

    def calculate_combat_ability(self):
        base_ability = self.strength * 10
        class_modifier = {"Vault Dweller": 5, "Wasteland Survivor": 4, "Raider": 7, "Ghoul": 3, "Robot": 6, "Mutant": 8}
        weapon_modifier = sum([10 for weapon in self.weapons if weapon in valid_items['Weapons']])
        
        gender_modifier = 5 if self.gender == "Male" else 3
        height_modifier = (self.height - 5) * 2  # Assuming height is in feet
        weight_modifier = self.weight / 50
        body_type_modifier = {"Lean": 1, "Average": 2, "Athletic": 4, "Bulky": 3}

        return base_ability + class_modifier.get(self.player_class, 0) + weapon_modifier + gender_modifier + height_modifier + weight_modifier + body_type_modifier.get(self.body_type, 0)

class Health:
    def __init__(self, endurance, player_class, body_type, age, height, weight, clothes):
        self.endurance = endurance
        self.player_class = player_class
        self.body_type = body_type
        self.age = age
        self.height = height
        self.weight = weight
        self.clothes = clothes

    def calculate_health(self):
        base_health = self.endurance * 10
        class_modifier = {"Vault Dweller": 5, "Wasteland Survivor": 4, "Raider": 7, "Ghoul": 3, "Robot": 6, "Mutant": 8}
        clothes_modifier = {"Jumpsuit": 1, "Leather Armor": 3, "Combat Armor": 5, "Raider Armor": 2, "Hazmat Suit": 4}

        height_modifier = (self.height - 5) * 1.5  # Assuming height is in feet
        weight_modifier = self.weight / 40
        body_type_modifier = {"Lean": 1, "Average": 2, "Athletic": 4, "Bulky": 3}
        age_modifier = (30 - self.age) / 10  # Assuming age affects health (younger characters have a slight health boost)

        return base_health + class_modifier.get(self.player_class, 0) + clothes_modifier.get(self.clothes, 0) + height_modifier + weight_modifier + body_type_modifier.get(self.body_type, 0) + age_modifier

class LevelSystem:
    def __init__(self):
        self.level = 1
        self.stat_points = 0
        self.perk_cards = []
        self.exp = 0

    def level_up(self):
        self.level += 1
        if self.level % 10 == 0:
            self.stat_points += 5
        else:
            self.stat_points += 1

        if self.level % 5 == 0:
            self.add_perk_card()

    def add_perk_card(self):
        new_perk = random.choice(list(perk_cards.keys()))
        self.perk_cards.append(new_perk)
        print(f"Congratulations! You received a new perk card: {new_perk}")
        print(f"Perk effect: {perk_cards[new_perk]}")

    def apply_perk_cards(self, character):
        for perk in self.perk_cards:
            effect = perk_cards[perk]
            for stat, value in effect.items():
                setattr(character, stat, getattr(character, stat) + value)

    def gain_exp(self, enemy_difficulty):
        difficulty_exp = {"Easy": 50, "Medium": 100, "Hard": 200, "Very Hard": 500}
        self.exp += difficulty_exp.get(enemy_difficulty, 0)
        while self.exp >= 1000:
            self.exp -= 1000
            self.level_up()

class Combat:
    def __init__(self, luck, perception):
        self.luck = luck
        self.perception = perception

    def dodge_chance(self, character_level, opponent_level):
        base_chance = 5  # Base dodge chance in percent
        level_difference = character_level - opponent_level
        return base_chance + self.luck + (self.perception * 0.5) + (level_difference * 0.5)

# Example Usage
if __name__ == "__main__":
    # Example character setup
    combat_abilities = CombatAbilities(weight=180, player_class="Raider", strength=8, gender="Male", weapons=["Laser Rifle"], age=25, body_type="Athletic", height=6)
    health = Health(endurance=7, player_class="Raider", body_type="Athletic", age=25, height=6, weight=180, clothes="Combat Armor")
    level_system = LevelSystem()
    combat = Combat(luck=5, perception=7)

    print(f"Combat Ability: {combat_abilities.calculate_combat_ability()}")
    print(f"Health: {health.calculate_health()}")
    print(f"Dodge Chance: {combat.dodge_chance(character_level=10, opponent_level=7)}%")

    # Leveling up and gaining perks
    for _ in range(12):
        level_system.level_up()
        print(f"Level: {level_system.level}, Stat Points: {level_system.stat_points}, Perk Cards: {level_system.perk_cards}")

    # Gaining experience from defeating enemies
    enemies_defeated = ["Easy", "Medium", "Hard", "Very Hard"]
    for enemy in enemies_defeated:
        level_system.gain_exp(enemy)
        print(f"EXP: {level_system.exp}, Level: {level_system.level}, Stat Points: {level_system.stat_points}, Perk Cards: {level_system.perk_cards}")
