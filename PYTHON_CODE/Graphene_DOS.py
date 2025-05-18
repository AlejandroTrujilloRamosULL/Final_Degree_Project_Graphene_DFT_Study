# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 16:59:59 2025

@author: aleja
"""

# We import the required packages
import pyprocar
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm
from matplotlib.colors import Normalize

# Closing plot for re-run
plt.close("all")

# Code to plot the density of states
fig_dos, ax = pyprocar.dosplot(code="vasp", dirname="C:\\path\\to\\your\\file",
                           mode="plain", elimit=[-10, 10], dos_limit=[0, 2],
                           orientation="horizontal", title="Graphene DOS")

# Labeling of the figure
ax.set_title("Graphene DOS", fontsize=24)
ax.set_xlabel("Energy [eV]", fontsize=22)
ax.set_ylabel("DOS", fontsize=22)
ax.tick_params(axis="both", which="major", labelsize=18, width=2, length=10)
ax.tick_params(axis="both", which="minor", labelsize=18, width=1, length=5)
ax.grid()

# Get the data from the plot
ax = plt.gca()  # Get the current axes
lines = ax.get_lines()  # Get all the lines (usually one line is the DOS curve)

# Assuming the first line is the DOS curve
x_data, y_data = lines[0].get_data()

# Normalizing data for color mapping
norm = Normalize(vmin=np.min(y_data), vmax=np.max(y_data))  
cmap = cm.plasma

# Fill the area under the DOS curve
ax.fill_between(x_data, y_data, color=cmap(norm(y_data)), alpha=0.7)
