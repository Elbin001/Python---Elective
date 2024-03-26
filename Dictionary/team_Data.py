"""Repeatedly ask the user to enter a team name and how
    many games a team has won or lost. Store this info in a dictionary,
    with team name as keys and values as a list of the form [wins,losses).
    Use the dictionary to do the following.
• Print names of all teams.
• Print name of team with highest wins
• Print name of team with highest losses
• Allow user to enter the team name and print the teams win percentage
"""

win = []
lose = []
games = {}
while(True):
    team_Name = input("\nEnter team name : ")
    if(team_Name == ""):
        break
    wins = int(input("No.of games won : "))
    loses = int(input("No.of games lost : "))
    games[team_Name] = [wins,loses]
    win.append(wins)
    lose.append(loses)

print("\nNames of Teams : ",list(games.keys()))

for i in games:
    if(games[i][0] == max(win)):
        print("\nTeam with highest win : ",i)
    if(games[i][1] == max(lose)):
        print("\nTeam with highest losses : ",i)

team_Name = input("\nEnter the team name to find win percentage : ")
if team_Name in games:
    percent = (games[team_Name][0]/(games[team_Name][0] + games[team_Name][1]))*100
else:
    print("There no such Team.")

print("Win Percentage of ",team_Name," = ",round(percent))
    
