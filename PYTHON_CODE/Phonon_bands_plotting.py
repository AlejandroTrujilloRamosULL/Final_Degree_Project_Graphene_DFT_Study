# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 16:49:51 2025

@author: aleja
"""

# Importing the required packages
import numpy as np
import matplotlib.pyplot as plt
import yaml

# Open and extract the data from the band.yaml
with open("C:\\path\\to\\your\\file") as f:
    data = yaml.safe_load(f)
    
# Extract and classify the different data
nqpoint = data["nqpoint"]
npath = data["npath"]
segment_nqpoint = data["segment_nqpoint"]
labels = data["labels"]
points = data["points"]
phonon = data["phonon"]


# Extract the data from phonons to plot
q_position = [q["q-position"] for q in phonon]
distance = [p["distance"] for p in phonon]
bands = [b["band"] for b in phonon]

# Extract the branches to know how many modes and frequencies to plot for
# each x point (distance)
n_branches = len(bands[0])
freqs = [np.zeros(len(bands)) for i in range(n_branches)]
        
for j in range(n_branches):
    for i in range(len(bands)):
        freqs[j][i] = bands[i][j]["frequency"]
        
        
# Close after executing code again
plt.close("all")        
        
# Plotting
for i in range(n_branches):
    plt.plot(distance, freqs[i], color="darkslategray")
plt.xticks([0, distance[100], distance[201], distance[302]], 
           [r"$\Gamma$", "K", "M", r"$\Gamma$"], fontsize=20)
plt.axvline(distance[0], color="black", linewidth=2)
plt.axvline(distance[100], color="black", linewidth=2)
plt.axvline(distance[201], color="black", linewidth=2)
plt.axvline(distance[302], color="black", linewidth=2)
plt.axhline(0, distance[0], 1,  linestyle="dotted", color="darkslategray")
plt.xlabel("High Symmetry Points (BZ)", fontsize=20)
plt.ylabel("Frequency (THz)", fontsize=20)
plt.title("Phonon Bands Diagram", fontstyle="italic", fontsize=22)
plt.xlim(0, np.max(distance))
plt.ylim(None, 50)
plt.tick_params(axis="both", which="major", labelsize=20, width=2, length=10)
plt.grid()
plt.legend()
plt.tight_layout()
        




