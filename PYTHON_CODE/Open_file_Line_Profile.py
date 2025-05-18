# -*- coding: utf-8 -*-
"""
Created on Wed Apr 16 12:18:22 2025

@author: aleja
"""

# COde for opening text files
# This one is specific to read the ELFCAR file text output from VESTA
# for plotting the ELF (Electron Localization Function) vs. Positions (Angstroms)

# We import the required packages
import numpy as np
import matplotlib.pyplot as plt

# We open the file from the required path, with reading option "r" only
f = open("C:\\path\\to\\your\\file", "r")

# We skip the headers of the file (there are 4 lines of information before 
# the data we want to retrieve)
lines = f.readlines()[4:]
print(lines[0])

# We split the values where for each element lines[i] it gives two values, we 
# want to store each one for plotting separately, the positions and elf values
columns = [np.zeros(1) for i in range(len(lines))]
pos = np.zeros(len(lines))
elf = np.zeros(len(lines))
for i in range(len(lines)):
    columns[i] = lines[i].split()
    pos[i] = columns[i][0]
    elf[i] = columns[i][1]
    
# Close the file
f.close()

# Closing the plot if rerunning the code
plt.close("all")

# Now we plot the two data values
plt.plot(pos, elf, "o-", color="gold", label="ELF vs. Distance data")
plt.xlabel("Distance ($\AA$)", fontsize=26)
plt.text(-0.03, -0.15, "(C atom)", fontsize=20)
plt.text(1.37, -0.15, "(C atom)", fontsize=20)
plt.ylabel("ELF values", fontsize=26)
plt.title("Line Profile (Graphene C-C bond)", fontsize=28)
plt.tick_params(axis="both", which="major", labelsize=24, width=2, length=10)
plt.legend(loc="best")
plt.grid()
plt.tight_layout()

           



