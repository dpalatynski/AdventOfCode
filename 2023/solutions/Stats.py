import matplotlib.pyplot as plt
import pandas as pd


my_stats = open(r"2023/inputs/Stats.txt").read()

days, time1, time2 = [], [], []
for line in my_stats.split('\n')[2:]:
    daily_stats = [valid for valid in line.split(' ') if valid != '']
    days.append(daily_stats[0])
    time1.append(daily_stats[1])
    time2.append(daily_stats[4])

df = pd.DataFrame({'Day': days[::-1],
                   'Time1': time1[::-1],
                   'Time2': time2[::-1]})
df['Time1'] = pd.to_timedelta(df['Time1'])
df['Time2'] = pd.to_timedelta(df['Time2'])

plt.figure(figsize=(10, 7))
plt.bar(df['Day'], df['Time2'].dt.total_seconds(), color='#ffff66', edgecolor='black', linewidth=0.5, label='Part 2')
plt.bar(df['Day'], df['Time1'].dt.total_seconds(), color='#9999cc', edgecolor='black', linewidth=0.5, label='Part 1')
plt.xticks(df['Day'], fontsize=12)
plt.yticks([3600*i for i in range(7)], [' ', '1h', '2h', '3h', '4h', '5h', '6h'], fontsize=12)
plt.title('Time spent to solve puzzles', fontsize=18)
plt.ylabel('Time', fontsize=15)
plt.xlabel('Day', fontsize=15)
plt.grid(axis='y', color='black', linewidth=0.5)
plt.legend(prop={'size': 15})
plt.savefig("2023/images/time_spent.jpg")
plt.show()
