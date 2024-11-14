print("Welcome to Wasteland Wanderer Character Creation!")

def assign_special_stats():
    while True:
        print("Assign your S.P.E.C.I.A.L stats (each stat starts at 1, total additional points: 21, max points per stat: 20):")
        New_points = 0
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
                        if 0 < int(stats[0][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("P: "):
                    try:
                        Perception_stat = st[3:].strip()
                        stats[1][1] = int(stats[1][1]) + int(st[3:].strip())
                        if 0 < int(stats[1][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("E: "):
                    try:
                        Endurance_stat = st[3:].strip()
                        stats[2][1] = int(stats[2][1]) + int(st[3:].strip())
                        if 0 < int(stats[2][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("C: "):
                    try:
                        Charisma_stat = st[3:].strip()
                        stats[3][1] = int(stats[3][1]) + int(st[3:].strip())
                        if 0 < int(stats[3][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("I: "):
                    try:
                        Intelligence_stat = st[3:].strip()
                        stats[4][1] = int(stats[4][1]) + int(st[3:].strip())
                        if 0 < int(stats[4][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("A: "):
                    try:
                        Agility_stat = st[3:].strip()
                        stats[5][1] = int(stats[5][1]) + int(st[3:].strip())
                        if 0 < int(stats[5][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
                    except ValueError:
                        valid_format = False
                        break
                elif st.startswith("L: "):
                    try:
                        Luck_stat = st[3:].strip()
                        stats[6][1] = int(stats[6][1]) + int(st[3:].strip())
                        if 0 < int(stats[6][1]) < 21:
                            pass
                        else:    
                            valid_format = False
                            break
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
                    New_points = int(New_points) + (int(total_points) - (int(Strength_stat) + int(Perception_stat) + int(Endurance_stat) + int(Charisma_stat) + int(Intelligence_stat) + int(Agility_stat) + int(Luck_stat)))
                    while True:
                        print(stats)
                        YorN = input(f"you still have {New_points} points to spend, would you like to spend them? Y/N:\n").upper()
                        if YorN == "Y":
                            break
                        elif YorN == "N":
                            Va = False
                            break
                        else:
                            print("invalid input use Y/N")
                    if Va == False:
                        break
                elif int(Strength_stat) + int(Perception_stat) + int(Endurance_stat) + int(Charisma_stat) + int(Intelligence_stat) + int(Agility_stat) + int(Luck_stat) > int(total_points):
                    print("too many points distributed. try again")
                else: 
                    print(stats)
                    break
            print("Please provide at least one valid stat.")
        else:
            print("Stats input cannot be empty. Please distribute your stats.")

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