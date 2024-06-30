import itertools
import pandas as pd
import random

# Function to generate random fielding data for an entire innings
def generate_innings_fielding_data(team1, team2, innings, overs, venue):
    data = []
    players = {
        'MI': ['Rohit Sharma (C)', 'Ishan Kishan (WK)', 'Suryakumar Yadav', 'Tilak Varma', 'Tim David', 'Cameron Green', 'Piyush Chawla', 'Jofra Archer', 'Jason Behrendorff', 'Arshad Khan', 'Riley Meredith'],
        'KKR': ['Shreyas Iyer (C)', 'Nitish Rana', 'Andre Russell', 'Sunil Narine', 'Rinku Singh', 'Venkatesh Iyer', 'Rahmanullah Gurbaz (WK)', 'Shardul Thakur', 'Umesh Yadav', 'Tim Southee', 'Varun Chakravarthy']
    }
    positions = ['Deep Fine Leg', 'Long Off', 'Cover', 'Short Mid Wicket', 'Third Man', 'Point', 'Long On', 'Square Leg', 'Mid Off', 'Short Third Man']
    descriptions = ['Fielding', 'Throw', 'Catch', 'Run Out']
    picks = ['Clean Pick', 'Fumble', 'Drop Catch']
    throws = ['Run Out', 'Other']

    for over, ball in itertools.product(range(overs), range(1, 7)):
        team = team1 if innings == 1 else team2
        player_name = random.choice(players[team])
        position = random.choice(positions)
        description = random.choice(descriptions)
        pick = random.choice(picks) if description == 'Fielding' else ''
        throw = random.choice(throws) if description == 'Throw' else ''
        runs = random.randint(-2, 4)  # Random runs saved or conceded
        data.append([innings, team, player_name, ball, position, description, pick, throw, runs, over + 1, venue])

    return data

# Define match details
team1 = 'MI'
team2 = 'KKR'
innings = 1  # First innings
overs = 20   # Total overs for the innings
venue = 'Wankhede Stadium, Mumbai'

# Generate fielding data for MI innings
mi_data = generate_innings_fielding_data(team1, team2, innings, overs, venue)

# Generate fielding data for KKR innings
kkr_data = generate_innings_fielding_data(team1, team2, innings=2, overs=overs, venue=venue)

# Combine data for both innings
fielding_data = mi_data + kkr_data

# Create DataFrame
df = pd.DataFrame(fielding_data, columns=['Innings', 'Team', 'Player Name', 'Ballcount', 'Position', 'Short Description', 'Pick', 'Throw', 'Runs', 'Overcount', 'Venue'])

# Save DataFrame to CSV
df.to_csv('fielding_data.csv', index=False)
