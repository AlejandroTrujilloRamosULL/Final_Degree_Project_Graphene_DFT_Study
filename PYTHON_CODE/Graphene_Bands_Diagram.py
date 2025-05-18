# -*- coding: utf-8 -*-
"""
Created on Sun Apr 13 13:24:00 2025

@author: aleja
"""
# We import the required packages
import pyprocar
import matplotlib.pyplot as plt

# Closing plot for re-run
plt.close("all")

# Code to plot the band diagrams of Graphene , obtain figure and axes
fig_band, ax = pyprocar.bandsplot(code="vasp", dirname="C:\\path\\to\\your\\file",
                   elimit=[-5, 5], mode="plain", interpolation_factor=3, 
                   color="midnightblue")


# We add the labeling of the k-path
ax.axvline(200, color="black")
ax.axvline(400, color="black")
ax.set_xticks([0, 200, 400, 599])
ax.set_xticklabels([r"$\Gamma$", "K", "M", r"$\Gamma$"], fontsize=22)
ax.set_xlabel("High Symmetry Points (BZ)", fontsize=22)
ax.set_ylabel("E - $E_{F}$ [eV]", fontsize=22)
ax.set_title("Graphene Bands Diagram", fontsize=24)
ax.tick_params(axis="y", which="major", labelsize=20, width=2, length=10)
ax.tick_params(axis="y", which="minor", labelsize=20, width=1, length=5)

plt.tight_layout()





