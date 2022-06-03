from unicodedata import name
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt


sns.set_style('darkgrid')
matplotlib.rcParams['font.size'] = 14
matplotlib.rcParams['figure.figsize'] = (9, 5)
matplotlib.rcParams['figure.facecolor'] = '#00000000'

# ------------------------------------------------------------------
print(25*'-', 'Matches Data', 25*'-')

ipl_df = pd.read_csv("matches.csv")
print(ipl_df.head(5))

print(ipl_df.shape)

print(ipl_df.info())

print(25*'-', 'Deliveries Data', 25*'-')

deliveries_df = pd.read_csv("deliveries.csv")
print(deliveries_df.head(5))

print(deliveries_df.shape)

print(deliveries_df.info())


print(25*'-', 'Discard Umpire Data from IPL Dataset', 25*'-')

discard_columns = ['umpire1', 'umpire2', 'umpire3']

ipl_df = ipl_df.drop(discard_columns, axis=1)
# axis=0 is rows
# axis=1 is columns

print(ipl_df.info())


print(25*'-', 'No of matches played by teams', 25*'-')

print(ipl_df.team1.value_counts())

print(25*'-', 'No of results generated', 25*'-')

print(ipl_df.result.value_counts())

print(25*'-', 'No of matches hosted by each city', 25*'-')

city_host = ipl_df.city.value_counts()

print(city_host)

# ------------- for graph---------
plt.figure(figsize=(15, 6))
plt.xticks(rotation=90)
plt.title('Number of matches hosted')
count = 0
cities = pd.DataFrame(city_host)
cities['name'] = city_host.index
for i in cities['city']:
    plt.text(count-0.4, i+1, str(i), color='black')
    count += 1
sns.barplot(x=city_host.index, y=city_host)
# plt.show()

print(25*'-', 'No of wickets taken by bowlers in last 12 seasons', 25*'-')

bowling_wickets = deliveries_df[deliveries_df['dismissal_kind'] != 'run out']
bowling_total = bowling_wickets.groupby(by='bowler').apply(
    lambda x: x['dismissal_kind'].dropna()).reset_index(name="Wickets")
bowling_wicket_count = bowling_total.groupby(by="bowler").count().reset_index()
bowling_top = bowling_wicket_count.sort_values(by="Wickets", ascending=False)
print("$$$$$$$$$$$$$$$$$$")
print(bowling_top)
print("$$$$$$$$$$$$$$$$$$")

top_bowlers = bowling_top.loc[:, ['bowler', 'Wickets']][0:10]
print(top_bowlers)

# --------- for graph ---------------

plt.figure(figsize=(12, 6))
plt.scatter(top_bowlers['bowler'], top_bowlers['Wickets'], color='r')
plt.plot(top_bowlers['bowler'], top_bowlers['Wickets'], color='g')
plt.xticks(rotation=60)
plt.xlabel('Top 10 Bowlers')
plt.ylabel('Wickets Taken')
plt.title('Top 10 Bowlers in last 12 seasons')

plt.show()
print(25*'-', 'matches played vs No. of matches Won', 25*'-')
# Q. Find number of
# matches played vs No. of matches Won by each team

matches_played = pd.concat([ipl_df['team1'], ipl_df['team2']])
print(matches_played)
matches_played = matches_played.value_counts().reset_index()
matches_played.columns = ['Team', 'Total Matches']
matches_played['wins'] = ipl_df['winner'].value_counts().reset_index()[
    'winner']

matches_played.set_index("Team", inplace=True)

print(matches_played.reset_index())

# Which player have Won the Man Of THe Match Award the most
print(25*'-', 'MoM Awards', 25*'-')
m_o_m = ipl_df.player_of_match.value_counts()
print(m_o_m)
