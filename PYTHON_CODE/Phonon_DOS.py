# -*- coding: utf-8 -*-
"""
Created on Sun Apr 27 20:32:22 2025

@author: aleja
"""

# Import packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.colors import Normalize
    
# Open the DOS file    
f = open("C:\\path\\to\\your\\file", "r")

# Skip the header line
lines = f.readlines()[1:]

# Extract the data from the dos file and lines
columns = [np.zeros(1) for i in range(len(lines))]
freq = np.zeros(len(lines))
dos = np.zeros(len(lines))

for i in range(len(lines)):
    columns[i] = lines[i].split() 
    freq[i] = columns[i][0]
    dos[i] = columns[i][1]
    
# Close plot
plt.close("all")
    
# Plotting
plt.plot(freq, dos, color="darkslategray")
plt.xlabel("Frequency (THz)", fontsize=20)
plt.ylabel("Density of States", fontsize=20)
plt.xlim(-5, np.max(freq))
plt.ylim(0, None)
plt.title("Phonon DOS", fontstyle="italic", fontsize=22)
plt.tick_params(axis="both", which="major", labelsize=20, width=2, length=10)
plt.legend()
plt.grid(color="gray")
plt.tight_layout()

# Filling the DOS curve area
ax = plt.gca()
line = ax.get_lines()

# Extracting the data from line's first line
x_data, y_data = line[0].get_data()

# Normalizing data for color mapping
norm = Normalize(vmin=np.min(y_data), vmax=np.max(y_data))  
cmap = cm.plasma

# Fill the area under the DOS curve
ax.fill_between(x_data, y_data, color=cmap(norm(y_data)), alpha=0.7)
