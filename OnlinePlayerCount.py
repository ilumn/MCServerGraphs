from mcstatus import *
import datetime
import time
from itertools import count
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

plt.style.use('dark_background')

x = []
y = []

index = count()

queryEnabled = False


def getPlayerCount():
  server = JavaServer.lookup('ip')
  status = server.status()
  return status.players.online


def animate(i):
  x.append(next(index))
  y.append(getPlayerCount())
  print(getPlayerCount())
  plt.cla()
  plt.xlabel("seconds since start")
  plt.ylabel("players")
  plt.plot(x, y)
  time.sleep(1)


ani = FuncAnimation(plt.gcf(), animate, 1000)

plt.tight_layout()
plt.show()
