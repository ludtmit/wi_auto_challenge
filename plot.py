import matplotlib.pyplot as plt
import csv
import math
o = []
x = []
dist = []
with open("offset.csv", newline="") as f:
    reader = csv.reader(f)
    for row in reader:
        o.append(float(row[1]))
with open("depth.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        dist.append(float(row[3]))
print(dist[1])
for i, val in enumerate(dist):
    x.append(math.sqrt(float(dist[i])*float(dist[i]) - float(o[i])*float(o[i])))


# Trajectory
ax = plt.gca()

#ax.set_aspect(.1)
plt.plot(o, x, label="Ego trajectory")  # swap axes


plt.scatter(o[0], x[0], c="red", marker="x", s=100, label="Start")
plt.scatter(o[-1], x[-1], c="green", marker="o", s=100, label="End")

plt.scatter(0, 0, c="black", marker="*", s=120, label="Traffic light (origin)")
plt.text(0.2, -0.5, "Origin")

plt.xlabel("Lateral (Y, m)")
plt.ylabel("Forward (X, m)")

plt.grid(True)


plt.xlabel("Forward (X, m)")
plt.ylabel("Lateral (Y, m)")
plt.title("Static Example: Ego Only")
plt.legend()
plt.axis("equal")

plt.show()

