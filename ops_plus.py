# OPS+ formula: (OPS / lgOPS) * 100

# User inputs
player_AB = int(input("Enter player at-bats: "))
player_H = int(input("Enter player hits: "))
player_2B = int(input("Enter player doubles: "))
player_3B = int(input("Enter player triples: "))
player_HR = int(input("Enter player home runs: "))
player_BB = int(input("Enter player walks: "))
player_HBP = int(input("Enter player hit by pitches: "))
player_SF = int(input("Enter player sacrifice flies: "))

league_AB = int(input("Enter league at-bats: "))
league_H = int(input("Enter league hits: "))
league_2B = int(input("Enter league doubles: "))
league_3B = int(input("Enter league triples: "))
league_HR = int(input("Enter league home runs: "))
league_BB = int(input("Enter league walks: "))
league_HBP = int(input("Enter league hit by pitches: "))
league_SF = int(input("Enter league sacrifice flies: "))

# Constants
singles_weight = 1.0
doubles_weight = 2.0
triples_weight = 3.0
home_runs_weight = 4.0
lgOPS_scale = 1.000 # for the 2023 season

# Calculations
player_TB = (player_H - player_2B - player_3B - player_HR) + (doubles_weight * player_2B) + (triples_weight * player_3B) + (home_runs_weight * player_HR)
player_OBP = (player_H + player_BB + player_HBP) / (player_AB + player_BB + player_HBP + player_SF)
player_SLG = player_TB / player_AB
player_OPS = player_OBP + player_SLG

league_TB = (league_H - league_2B - league_3B - league_HR) + (doubles_weight * league_2B) + (triples_weight * league_3B) + (home_runs_weight * league_HR)
league_OBP = (league_H + league_BB + league_HBP) / (league_AB + league_BB + league_HBP + league_SF)
league_SLG = league_TB / league_AB
league_OPS = league_OBP + league_SLG
lgOPS = lgOPS_scale * league_OPS

player_OPS_plus = (player_OPS / lgOPS) * 100

# Output
print("The player's OPS+ for the 2023 season is: ", player_OPS_plus)

