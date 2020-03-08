import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import datetime as dt
import csv

data_names = ['1', '2', '3', '4', '5', '6']
data_values = [9124, 8652, 7592, 7515, 7041, 6487]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 10})

ax = plt.axes()
ax.yaxis.grid(True, zorder = 1)

xs = range(len(data_names))

plt.bar([x + 0.05 for x in xs], [ d * 0.9 for d in data_values],
        width = 0.1, color = 'blue', alpha = 0.7, label = 'Daily',
        zorder = 2)
plt.bar([x + 0.15 for x in xs], data_values,
        width = 0.1, color = 'orange', alpha = 0.7, label = 'Weekly',
        zorder = 2)
plt.bar([x + 0.25 for x in xs], data_values,
        width = 0.1, color = 'green', alpha = 0.7, label = 'Occasionaly',
        zorder = 2)
plt.bar([x + 0.35 for x in xs], data_values,
        width = 0.1, color = 'red', alpha = 0.7, label = 'First Time',
        zorder = 2)
plt.bar([x + 0.45 for x in xs], data_values,
        width = 0.1, color = 'pink', alpha = 0.7, label = 'Yesterday',
        zorder = 2)
plt.xticks(xs, data_names)

fig.autofmt_xdate(rotation = 25)

plt.legend(loc='upper right')
fig.savefig('plot.png')

#########################

data_names = ['Saturday', 'Sunday', 'Monday', 'Tuesday',
              'Wednesday', 'Thursday', 'Friday']
data_values = [1076, 979, 222, 189, 137, 134, 124]

dpi = 80
fig = plt.figure(dpi = dpi, figsize = (512 / dpi, 384 / dpi) )
mpl.rcParams.update({'font.size': 9})

plt.title('Daily')

xs = range(len(data_names))

plt.pie( 
    data_values, autopct='%.1f', radius = 1.1,
    explode = [0.15] + [0 for _ in range(len(data_names) - 1)] )
plt.legend(
    bbox_to_anchor = (-0.16, 0.45, 0.25, 0.25),
    loc = 'lower left', labels = data_names )
fig.savefig('diagram.png')