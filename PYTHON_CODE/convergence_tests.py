# -*- coding: utf-8 -*-
"""
Created on Thu Apr 10 18:56:56 2025

@author: aleja
"""

# We import the packages necessary
import numpy as np
import matplotlib.pyplot as plt

# We store the values for the Energies and CPU calculation times for
# different ENCUT and KPOINTS

# We define the number of atoms per unit cell
atoms = 2

# Firstly for ENCUT loops iteration
encut = np.array([350, 400, 450, 500, 550, 600, 650, 700, 750, 800])
energies_encut = np.array([-18.479306 , -18.453343,  -18.440015, -18.435563,
                           -18.436061, -18.440158, -18.445177, -18.449446,
                           -18.451977, -18.453547])
cpu_time_encut = np.array([0.846, 0.489, 0.663, 0.479, 0.572, 0.659, 0.596, 
                           0.612, 0.760, 0.818])

# Secondly for KPOINTS loop iteration
kpoints = np.array([3, 7, 11, 15, 19, 23])
energies_kpoints = np.array([-17.876904, -18.456520, -18.444141, -18.440158,
                             -18.444346, -18.443932])
cpu_time_kpoints = np.array([0.476, 0.575, 0.782, 1.094, 1.459, 1.904])

# We define the function to calculate the energies per atom
energies_encut_atom = np.zeros(len(energies_encut)) 
energies_kpoints_atom = np.zeros(len(energies_kpoints)) 
def en_atom(energies, atoms, energies_atom):
    for i in range(len(energies)):
        energies_atom[i] = energies[i]/atoms
    return energies_atom
        
# We close the plots every time the code executes
plt.close("all")

# Plotting of the convergence tests
fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2, figsize=(16, 8))

ax1.plot(encut, en_atom(energies_encut, atoms, energies_encut_atom), "o--", 
         color="red", label="E (eV/atom) vs. Cutoff data")
ax1.set_xlabel("Cutoff energy [eV]", fontsize=16)
ax1.set_ylabel("E [eV/atom]", fontsize=16)
ax1.tick_params(axis="both", which="major", labelsize=16)
ax1.set_title("(Energy vs. Cutoff) Convergence Test", fontsize=18)
ax1.legend(loc="upper right")
ax1.grid()
plt.tight_layout()

ax2.plot(encut, cpu_time_encut, "o--", color="blue", 
         label="CPU time vs. Cutoff data")
ax2.set_xlabel("Cutoff energy [eV]", fontsize=16)
ax2.set_ylabel("CPU time [s]", fontsize=16)
ax2.tick_params(axis="both", which="major", labelsize=16)
ax2.set_title("(CPU time vs. Cutoff) Convergence Test", fontsize=18)
ax2.legend(loc="upper right")
ax2.grid()
plt.tight_layout()

ax3.plot(kpoints, en_atom(energies_kpoints, atoms, energies_kpoints_atom), "o--", 
         color="red", label="E (eV/atom) vs. Kpoints data")
ax3.set_xlabel("Kpoints [$\AA^{-3}$]", fontsize=16)
ax3.set_ylabel("E [eV/atom]", fontsize=16)
ax3.tick_params(axis="both", which="major", labelsize=16)
ax3.set_title("(Energy vs. Kpoints) Convergence Test", fontsize=18)
ax3.legend(loc="upper right")
ax3.grid()
plt.tight_layout()

ax4.plot(kpoints, cpu_time_kpoints, "o--", color="blue", 
         label="CPU time vs. Kpoints data")
ax4.set_xlabel("Kpoints [$\AA^{-3}$]", fontsize=16)
ax4.set_ylabel("CPU time [s]", fontsize=16)
ax4.tick_params(axis="both", which="major", labelsize=16)
ax4.set_title("(CPU time vs. Kpoints) Convergence Test", fontsize=18)
ax4.legend(loc="upper right")
ax4.grid()
plt.tight_layout()
