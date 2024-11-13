print("Welcome to Wasteland Wanderer Character Creation!")
"""while True:
    name_input = input("Enter your character's name in the format (F: name, M: name, L: name, N: name): ").strip()
    if name_input:
        name_parts = name_input.split(", ")
        print(name_input.split(", "))
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
        print("Name input cannot be empty. Please enter a valid name.")"""


def assign_special_stats():
    while True:
        print("Assign your S.P.E.C.I.A.L stats (each stat starts at 1, total additional points: 21, max points per stat: 20):")
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
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("P: "):
                    try:
                        Perception_stat = st[3:].strip()
                        stats[1][1] = int(stats[1][1]) + int(st[3:].strip())
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("E: "):
                    try:
                        Endurance_stat = st[3:].strip()
                        stats[2][1] = int(stats[2][1]) + int(st[3:].strip())
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("C: "):
                    try:
                        Charisma_stat = st[3:].strip()
                        stats[3][1] = int(stats[3][1]) + int(st[3:].strip())
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("I: "):
                    try:
                        Intelligence_stat = st[3:].strip()
                        stats[4][1] = int(stats[4][1]) + int(st[3:].strip())
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("A: "):
                    try:
                        Agility_stat = st[3:].strip()
                        stats[5][1] = int(stats[5][1]) + int(st[3:].strip())
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("L: "):
                    try:
                        Luck_stat = st[3:].strip()
                        stats[6][1] = int(stats[6][1]) + int(st[3:].strip())
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
                    while True:
                        YorN = input(f"you still have points to spend {total_points}, would you like to spend them? Y/N:\n")
                        if YorN == "Y":
                            break
                        elif YorN == "N":
                            #New_points = int(New_points) + int(total_points)
                            Va = False
                            break
                        else:
                            print("invalid input use Y/N")
                    if Va == False:
                        break
                elif int(Strength_stat) + int(Perception_stat) + int(Endurance_stat) + int(Charisma_stat) + int(Intelligence_stat) + int(Agility_stat) + int(Luck_stat) > int(total_points):
                    print("too many points distributed. try again")
                else: 
                    break
            print("Please provide at least one valid stat.")
        else:
            print("Stats input cannot be empty. Please distribute your stats.")
        #fix negatives
        #Fix over 20 stat points

        """ 
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
    except Exception as e:
        print(f"An error occurred: {e}") """

assign_special_stats()