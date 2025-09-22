import matplotlib.pyplot as plt
import matplotlib.animation as animation
import glob
import csv
import imageio.v2 as imageio
import numpy as np

# Load image frames into memory
frame_files = sorted(glob.glob("rgb/*.png"))
frames = [imageio.imread(f) for f in frame_files]

# Depth npz files (one per frame)
depth_files = sorted(glob.glob("xyz/*.npz"))

# Load point list
points = []
with open("tl_center.csv", newline="") as f:
    reader = csv.reader(f)
    header = next(reader)
    for row in reader:
        r = int(float(row[1]))
        c = int(float(row[2]))
        points.append((r, c))

fig, (ax_rgb, ax_depth) = plt.subplots(1, 2, figsize=(10, 5))

def update(i):
    ax_rgb.clear()
    ax_depth.clear()

    # RGB frame
    ax_rgb.imshow(frames[i])
    r, c = points[i]
    ax_rgb.scatter(r, c, c="red", s=40, marker="x")
    ax_rgb.set_title("RGB Frame")

    # Depth frame
    data = np.load(depth_files[i])
    coords = data["xyz"]
    z = coords[..., 2]  # depth channel

    im = ax_depth.imshow(z, cmap="plasma", vmin=0, vmax=np.nanpercentile(z, 95))
    ax_depth.set_title("Depth Map")

    return im

ani = animation.FuncAnimation(fig, update, frames=len(frames), interval=100)
plt.show()
