import pandas as pd

# Function to calculate performance score
def calculate_performance_score(df, weights):
    ps = (df['Runs'] * weights['RS']) + \
         (df['Pick'] == 'Clean Pick') * weights['WCP'] + \
         (df['Throw'] == 'Run Out') * weights['WGT'] + \
         (df['Short Description'] == 'Catch') * weights['C'] + \
         (df['Short Description'] == 'Drop Catch') * weights['DC'] + \
         (df['Short Description'] == 'Run Out') * weights['RO']
    return ps

# Read data from CSV file
data = pd.read_csv('fielding_data.csv')

# Define weights for performance metrics
weights = {
    'WCP': 1,
    'WGT': 1,
    'C': 1,
    'DC': -1,
    'RO': 2,
    'RS': 1  # Adjust the weight for runs saved/conceded based on your requirement
}

# Calculate performance score
data['Performance Score'] = calculate_performance_score(data, weights)

# Add Team Name column
data['Team Name'] = data['Team']

# Group data by player name and team
player_performance = data.groupby(['Team', 'Player Name']).agg({
    'Pick': lambda x: (x == 'Clean Pick').sum(),
    'Throw': lambda x: (x == 'Run Out').sum(),
    'Short Description': lambda x: (x == 'Catch').sum(),
    'Short Description': lambda x: (x == 'Drop Catch').sum(),
    'Short Description': lambda x: (x == 'Run Out').sum(),
    'Runs': 'sum',
    'Performance Score': 'sum'
}).reset_index()

# Sort players by performance score
player_performance = player_performance.sort_values(by='Performance Score', ascending=False)

# Print top performing players
print("Top performing players:")
print(player_performance.head())

# Export data to Excel or CSV for further analysis
player_performance.to_excel('player_performance.xlsx', index=False)

# Create CSV file for top performers
top_performers = player_performance.head(10)  # Selecting top 10 performers
top_performers.to_csv('top_performers.csv', index=False)
