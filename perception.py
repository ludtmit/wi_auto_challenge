import numpy as np
import csv
import glob
import math



with open("bbox_light.csv", newline="") as f, open("tl_center.csv", "w", newline="") as out_f:
    reader = csv.reader(f)
    headers = next(reader)
    writer = csv.writer(out_f)
    writer.writerow(["frame", "x", "y"])
    for row in reader:
        x = (int(row[1]) + int(row[3])) / 2
        y = (int(row[2]) + int(row[4])) / 2
        line = [row[0], x, y]
        writer.writerow(line)

offsets = [(-1, -1), (-1, 0), (-1, 1),
           ( 0, -1), ( 0, 0), ( 0, 1),
           ( 1, -1), ( 1, 0), ( 1, 1)]

file_list = glob.glob("xyz/*.npz")
old_y = None
old_x = None
old_change = None
with open("tl_center.csv", newline="") as center_file, open("depth.csv", "w", newline="") as w_depth:
    reader = csv.reader(center_file)
    headers = next(reader)
    writer = csv.writer(w_depth)
    writer.writerow(["frame", "X", "Y", "raw distance", "deg"])
    old_distance = 39.18671811919346
    for depth_file, row in zip(file_list, reader):
        data = np.load(depth_file)["xyz"]
        center_y = int(float(row[1]))
        center_x = int(float(row[2]))
        

        X, Y, Z, W = data[center_x, center_y]
        if np.isfinite(Z):
            distance = math.sqrt(X*X + Y*Y)
            distance_moved = old_distance - distance
            old_distance = distance
            line = [row[0], X, Y, distance, (X/Y) * distance_moved]
            writer.writerow(line)
            
            
            
