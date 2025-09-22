import numpy as np
import csv

# Load car positions
x_list, y_list = [], []
with open("depth.csv", newline="") as f:
    reader = csv.reader(f)
    next(reader)
    for row in reader:
        x_list.append(float(row[1]))
        y_list.append(float(row[2]))

x = np.array(x_list)
y = np.array(y_list)

# Start and end points
x_s, y_s = x[0], y[0]
x_e, y_e = x[-1], y[-1]

# Signed deviation
d_signed = ((y_e - y_s)*x - (x_e - x_s)*y + x_e*y_s - y_e*x_s) / np.sqrt((y_e - y_s)**2 + (x_e - x_s)**2)

# Print left/right info
with open("offset.csv", "w", newline="") as f:
    writer = csv.writer(f)
    for i, d in enumerate(d_signed):
        side = "-" if d > 0 else "" if d < 0 else "on line"
        writer.writerow([i, d])
        print(f"Step {i}: {side} {abs(d):.3f} meters")
