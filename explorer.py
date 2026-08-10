with open("data.csv") as file:
    nba = file.readlines()

players = []

for line in nba[1:]:
    clean = line.strip()
    part = clean.split(",")
    play_info = {"name":part[0], "team":part[1], "points":float(part[2]), "rebounds":float(part[3]), "assists":float(part[4])}
    players.append(play_info)

def describe(p):
   name = p["name"]
   team = p["team"]
   points = p["points"]
   rebounds = p["rebounds"]
   assists = p["assists"]
   return f"{name} ({team}) - {points} pts, {rebounds} rebs, {assists} ast"

for p in players:
    print(describe(p))

totals = {}

for p in players:
    team = p["team"]
    pts = p["points"]
    if team in totals:
       totals[team] = totals[team] + pts
    else:
        totals[team] = pts

for team, pts in totals.items():
    print(f"{team}: {pts}")

def is_scorer(p,threshold):
    return p["points"] > threshold
    
print(is_scorer(players[0], 50))

counter = 0
for p in players:
    if p["rebounds"] > 7:
        counter += 1

print (f'{counter} total players who have over 7 rebounds')