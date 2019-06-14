import matplotlib.pyplot as plt
import time
import datetime
x = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

#projection
# throughput = [4169, 8202, 12409, 16487, 20188, 23769, 28011, 31717, 35412, 38368]
# latency = [5384.885529395736, 5665.5087910861785, 6117.6716762818605, 6727.505567440815, 7409.106248798814, 8159.647157835565, 9515.681174459625, 12085.616873773079, 14854.07711131874, 22779.762468494828]
# latency99 = [10290, 11054, 12229, 13978, 15716, 17511, 25575, 32420, 39151, 50503]

#selection1
throughput = [4153, 8150, 12463, 16496, 20539, 23550, 27690, 31681, 36105, 40753]
latency = [5865.069986574802, 6164.281903334394, 6539.633506751896, 6918.272597117714, 7526.0549943612095, 7951.443227756482, 8889.97598472362, 10094.927475390521, 11715.156910426678, 14478.408570322672]

fig, ax1 = plt.subplots()

color = 'tab:red'
ax1.set_xlabel('Number of Games')
ax1.set_ylabel('Average Throughput', color=color)
ax1.plot(x, throughput, color=color)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

color = 'tab:blue'
ax2.set_ylabel('Average Latency', color=color)  # we already handled the x-label with ax1
ax2.plot(x, latency, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.show()
# hero
