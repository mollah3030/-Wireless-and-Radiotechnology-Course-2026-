# 3D Radiation Pattern of an Omni-Directional Antenna Using MATLAB

## Student Information
- **Name:** [Your Name]
- **Student ID:** [Your Student ID]

## Objective
The purpose of this assignment is to plot the 3-dimensional radiation pattern of an omni-directional antenna using MATLAB. The program takes the lower and upper bounds of theta and phi as input values, generates the mesh grid, and displays the 3D pattern based on the entered field pattern.

## Files Included
- `antenna_pattern_3d.m` – MATLAB script for plotting the 3D radiation pattern
- `README.md` – assignment description and instructions

## MATLAB Code Description
The MATLAB script:
- asks the user to enter the lower and upper bounds of theta in degrees
- asks the user to enter the lower and upper bounds of phi in degrees
- assigns the increment values and radian conversion
- creates theta and phi vectors
- converts them into radians
- generates the mesh grid using `meshgrid`
- asks for the field pattern
- takes the absolute value of the field pattern
- converts spherical coordinates into Cartesian coordinates using `sph2cart`
- plots the 3D radiation pattern using `mesh`

## Example Input Values
Use the following values when running the program:

- Lower Range of Theta in Degree = `0`
- Upper Range of Theta in Degree = `360`
- Lower Range of Phi in Degree = `0`
- Upper Range of Phi in Degree = `360`
- Field Pattern `E(THETA,PHI)` = `1`
- Field Pattern `P(THETA,PHI)` = `1`

## Expected Output
The output is a 3D omni-directional pattern that appears like a sphere-shaped mesh plot. The program also prints the input parameters and the selected field pattern in the MATLAB command window.

## Result Snapshot
Add your MATLAB result screenshot here before submission.

**[Insert result screenshot here]**

## Conclusion
This assignment shows how MATLAB can be used to create a 3D radiation pattern by using spherical coordinates, mesh generation, and coordinate conversion. It helps in understanding how an omni-directional antenna pattern can be visualized in three dimensions.
