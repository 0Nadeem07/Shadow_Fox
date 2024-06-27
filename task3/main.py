import pandas as pd

# Sample data (as provided)
data = [
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": "Rilee Russouw", "BallCount": 0.1, "Position": "Short mid wicket", "Pick": "Y", "Throw": None, "Runs": 2, "Overcount": 1, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": "Phil Salt", "BallCount": 0.2, "Position": "Wicket keeper", "Pick": "Y", "Throw": "Y", "Runs": -1, "Overcount": 1, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": "Yash Dhull", "BallCount": 0.3, "Position": "Covers", "Pick": "Y", "Throw": "Y", "Runs": 3, "Overcount": 1, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": "Axar Patel", "BallCount": 0.4, "Position": "Point", "Pick": "Y", "Throw": "Y", "Runs": 0, "Overcount": 1, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": None, "BallCount": 0.5, "Position": None, "Pick": None, "Throw": None, "Runs": 1, "Overcount": 1, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": "Lalit Yadav", "BallCount": 0.6, "Position": "Cover point", "Pick": "Y", "Throw": "Y", "Runs": -2, "Overcount": 1, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": "Aman Khan", "BallCount": 1.1, "Position": "Long off", "Pick": "Y", "Throw": "Y", "Runs": 1, "Overcount": 2, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": None, "BallCount": 1.2, "Position": None, "Pick": None, "Throw": None, "Runs": 2, "Overcount": 2, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": "Kuldeep Yadav", "BallCount": 1.3, "Position": "Short mid wicket", "Pick": "Y", "Throw": None, "Runs": 4, "Overcount": 2, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": None, "BallCount": 1.4, "Position": None, "Pick": None, "Throw": None, "Runs": 2, "Overcount": 2, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": "Kuldeep Yadav", "BallCount": 1.5, "Position": "Point", "Pick": "Y", "Throw": "Y", "Runs": 0, "Overcount": 2, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
    {"Match No.": "IPL2367", "Innings": 1, "Teams": "Delhi Capitals", "Player Name": "Lalit Yadav", "BallCount": 1.6, "Position": "Bowler", "Pick": "Y", "Throw": None, "Runs": -2, "Overcount": 2, "Venue": "Delhi", "Stadium": "Arun Jaitley Stadium"},
]

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Replace empty strings with NaN and convert 'Runs' column to numeric
df.replace("", pd.NA, inplace=True)
df['Runs'] = pd.to_numeric(df['Runs'], errors='coerce')

# Define the weights for each action
weights = {
    'WCP': 1,
    'WGT': 1,
    'WC': 3,
    'WDC': -3,
    'WST': 3,
    'WRO': 3,
    'WMRO': -2,
    'WDH': 2,
}

# Calculate performance metrics //
def calculate_performance(player_data):
    CP = len(player_data[player_data['Pick'] == 'Y'])
    GT = len(player_data[player_data['Throw'] == 'Y'])
    C = len(player_data[player_data['Pick'] == 'Catch'])  
    DC = len(player_data[player_data['Pick'] == 'Drop catch'])  
    ST = len(player_data[player_data['Throw'] == 'Stumping'])  
    RO = len(player_data[player_data['Throw'] == 'Run out'])  
    MRO = len(player_data[player_data['Throw'] == 'Missed run out'])  
    DH = len(player_data[player_data['Pick'] == 'Direct hit'])  
    RS = player_data['Runs'].sum(skipna=True)

    PS = (CP * weights['WCP']) + (GT * weights['WGT']) + (C * weights['WC']) + (DC * weights['WDC']) + (ST * weights['WST']) + (RO * weights['WRO']) + (MRO * weights['WMRO']) + (DH * weights['WDH']) + RS
    return PS

# Group data by player and calculate their performance score
player_performance = []
for player, player_data in df.groupby('Player Name'):
    if player:  # Skip entries with no player name
        PS = calculate_performance(player_data)
        player_performance.append({
            'Player Name': player,
            'Clean Picks': len(player_data[player_data['Pick'] == 'Y']),
            'Good Throws': len(player_data[player_data['Throw'] == 'Y']),
            'Catches': len(player_data[player_data['Pick'] == 'Catch']), 
            'Dropped Catches': len(player_data[player_data['Pick'] == 'Drop catch']),  
            'Stumpings': len(player_data[player_data['Throw'] == 'Stumping']), 
            'Run Outs': len(player_data[player_data['Throw'] == 'Run out']), 
            'Missed Run Outs': len(player_data[player_data['Throw'] == 'Missed run out']), 
            'Direct Hits': len(player_data[player_data['Pick'] == 'Direct hit']),  
            'Runs Saved': player_data['Runs'].sum(skipna=True),
            'Performance Score': PS
        })

# Convert the player performance data into a DataFrame
performance_df = pd.DataFrame(player_performance)

# Save the data to an Excel file
with pd.ExcelWriter('fielding_analy.xlsx') as writer:
    df.to_excel(writer, sheet_name='Fielding Data', index=False)
    performance_df.to_excel(writer, sheet_name='Performance Scores', index=False)

print("Fielding analysis data has been successfully saved to 'fielding_analysis.xlsx'")
