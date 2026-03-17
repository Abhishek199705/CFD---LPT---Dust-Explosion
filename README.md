# Simulation of dust explosions in a silo
The project was carried to to find the min ratio of vent opening in silo so that the over pressure in the silo is always below 2 bar. This becomes useful during design of pressure vents.

## Replicating the simulations
The simulation setup has been uploaded under case files. The simulations can be replicated by downloading the OpenFOAM setup files. The closed case is first simulated and then a vent opening is triggered when the pressure reaches a certain threshold (1.3 bar was used).

The coalChemistryFoam CFD-LPT solver was used.
