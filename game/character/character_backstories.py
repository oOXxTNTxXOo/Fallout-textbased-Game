import random

def generate_random_details(gender, age, race, body_type, height, special_stats):
    try:
        # First part: Introduces the character
        gender_pronoun = "He" if gender == "Male" else "She"
        intro = f"{gender_pronoun} is a {age} years old {race}, standing at {height} feet tall with a {body_type} body type."

        # Second part: Character likes based on SPECIAL stats and race
        likes = []
        if race == "Vault Dweller":
            if special_stats["Strength"] > 10:
                likes.append("enjoys weight training in the vault gym")
            if special_stats["Perception"] > 10:
                likes.append("loves monitoring systems and fine-tuning electronics")
            if special_stats["Endurance"] > 10:
                likes.append("participates in vault marathons and endurance tests")
            if special_stats["Charisma"] > 10:
                likes.append("is a popular vault entertainer and community leader")
            if special_stats["Intelligence"] > 10:
                likes.append("excels in scientific research and experimentation")
            if special_stats["Agility"] > 10:
                likes.append("is an expert in vault maintenance and repairs")
            if special_stats["Luck"] > 10:
                likes.append("enjoys playing and often wins at vault gambling games")

        elif race == "Raider":
            if special_stats["Strength"] > 10:
                likes.append("enjoys raiding settlements and taking spoils")
            if special_stats["Perception"] > 10:
                likes.append("loves scouting for new targets and ambush points")
            if special_stats["Endurance"] > 10:
                likes.append("survives brutal battles and harsh environments")
            if special_stats["Charisma"] > 10:
                likes.append("is a fearsome raider leader who commands respect")
            if special_stats["Intelligence"] > 10:
                likes.append("strategizes raids with tactical precision")
            if special_stats["Agility"] > 10:
                likes.append("is agile in combat, dodging attacks with ease")
            if special_stats["Luck"] > 10:
                likes.append("often escapes dangerous situations unscathed")

        elif race == "Wasteland Survivor":
            if special_stats["Strength"] > 10:
                likes.append("thrives in scavenging and building shelter")
            if special_stats["Perception"] > 10:
                likes.append("has a keen eye for spotting dangers and resources")
            if special_stats["Endurance"] > 10:
                likes.append("endures long treks and scarce supplies")
            if special_stats["Charisma"] > 10:
                likes.append("forms alliances with other survivors")
            if special_stats["Intelligence"] > 10:
                likes.append("crafts ingenious tools and makeshift weapons")
            if special_stats["Agility"] > 10:
                likes.append("navigates the wasteland swiftly and stealthily")
            if special_stats["Luck"] > 10:
                likes.append("often finds valuable items and avoids traps")

        elif race == "Robot":
            if special_stats["Intelligence"] > 10:
                likes.append("enjoys learning new programming languages")
                likes.append("loves tinkering with electronics")
            if special_stats["Strength"] > 10:
                likes.append("is equipped with powerful hydraulics for heavy lifting")
            if special_stats["Endurance"] > 10:
                likes.append("is built with reinforced armor for durability")
            if special_stats["Perception"] > 10:
                likes.append("has advanced sensory modules for precise detection")
            if special_stats["Luck"] > 10:
                likes.append("has a knack for avoiding dangerous situations")
            if special_stats["Charisma"] > 10:
                likes.append("is designed with advanced social interaction protocols")

        elif race == "Ghoul":
            if special_stats["Endurance"] > 10:
                likes.append("is exceptionally resilient to radiation")
            if special_stats["Charisma"] > 10:
                likes.append("has an eerie charm that can influence others")
            if special_stats["Intelligence"] > 10:
                likes.append("has a wealth of knowledge from centuries of experience")
                likes.append("loves collecting pre-war artifacts")
            if special_stats["Luck"] > 10:
                likes.append("survives through sheer luck")

        elif race == "Mutant":
            if special_stats["Strength"] > 10:
                likes.append("enjoys demonstrating immense strength")
                likes.append("loves wrestling and physical contests")
            if special_stats["Endurance"] > 10:
                likes.append("can endure extreme conditions effortlessly")
            if special_stats["Perception"] > 10:
                likes.append("has heightened senses")
            if special_stats["Agility"] > 10:
                likes.append("moves surprisingly swiftly for their size")
            if special_stats["Luck"] > 10:
                likes.append("seems to find themselves in favorable situations")
        
        likes_part = " and ".join(likes) if likes else "has varied interests and hobbies"

        # Third part: Family and past
        family_size = random.randint(1, 10)
        family_description = f"{gender_pronoun} comes from a family of {family_size}."
        backstory = random.choice([
            "Their past is filled with joy and happy memories.",
            "Their past is filled with hardships and sad memories."
        ])

        race_details = ""
        if race == "Vault Dweller":
            if "joy" in backstory:
                race_details = "This vault dweller lived a peaceful life, contributing positively to vault society."
            else:
                race_details = "This vault dweller faced significant challenges and conflicts within the vault, leading to a troubled past."
        elif race == "Raider":
            if "joy" in backstory:
                race_details = "This raider relished in their conquests and the spoils of their raids."
            else:
                race_details = "This raider endured constant struggles for power and survival within their clan."
        elif race == "Wasteland Survivor":
            if "joy" in backstory:
                race_details = "This survivor found happiness in small victories and the companionship of fellow wanderers."
            else:
                race_details = "This survivor's life has been marked by loss and the relentless fights."
        if race == "Robot":
            if "joy" in backstory:
                race_details = "This robot was a beloved member of a human family, serving faithfully for many years."
            else:
                race_details = "This robot faced constant reprogramming and misuse, leaving it with a corrupted memory bank. Often malfunctioned due to poor maintenance."
        elif race == "Ghoul":
            if "joy" in backstory:
                race_details = "Despite the ghoulification, this character retains their humanity and tries to coexist peacefully with others."
            else:
                race_details = "Living with ghoulification has been hard, facing discrimination and often living on the fringes of society."
        elif race == "Mutant":
            if "joy" in backstory:
                race_details = "Living as a mutant is tough, but this character has managed to find a group of like-minded individuals to survive with."
            else:
                race_details = "Mutant life is harsh and filled with conflict, often dealing with prejudice and constant battles for survival."
        else:
            if "joy" in backstory:
                race_details = "As a survivor of the wasteland, this character has adapted to the harsh environment and continues to seek out new adventures."
            else:
                race_details = "The harsh wasteland has shaped their resilience, overcoming numerous adversities and challenges."

        # Combine parts
        background = f"{intro} {gender_pronoun} {likes_part}. {family_description} {backstory} {race_details}"
        return background

    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
special_stats = {
    "Strength": 2,
    "Perception": 3,
    "Endurance": 3,
    "Charisma": 3,
    "Intelligence": 2,
    "Agility": 3,
    "Luck": 11
}
print(generate_random_details("Male", 25, "Vault Dweller", "Athletic", 6, special_stats))
print(generate_random_details("Female", 30, "Robot", "Bulky", 5, special_stats))
print(generate_random_details("Male", 35, "Ghoul", "Lean", 5.5, special_stats))
print(generate_random_details("Female", 40, "Mutant", "Stocky", 7, special_stats))
