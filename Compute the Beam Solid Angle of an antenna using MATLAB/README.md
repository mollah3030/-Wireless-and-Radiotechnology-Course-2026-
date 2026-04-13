# Beam Solid Angle of an Antenna Using MATLAB

## Student Information
- **Name:** [Your Name]
- **Student ID:** [Your Student ID]

## Objective
The purpose of this assignment is to compute the beam solid angle of an antenna from its radiation pattern using MATLAB. The program uses spherical coordinates and numerical integration to calculate the beam area in steradians.

## Definition
The beam solid angle of an antenna is given by the integral of the normalized power pattern over the angular region:

**ΩA = ∫∫ Pn(θ,φ) sin(θ) dθ dφ**

where:

- `Pn(θ,φ)` is the normalized power pattern
- `dΩ = sin(θ) dθ dφ`

## Files Included
- `beam_solid_angle.m` – MATLAB code to calculate the beam solid angle
- `README.md` – assignment description and explanation

## MATLAB Program Description
The MATLAB script performs the following steps:

- asks the user to enter the lower and upper bounds of theta in degrees
- asks the user to enter the lower and upper bounds of phi in degrees
- converts theta and phi values from degrees to radians
- generates `THETA` and `PHI` using `meshgrid`
- asks the user to enter the field pattern
- asks the user to enter the power pattern
- calculates the beam solid angle using numerical summation
- prints the beam area in steradians

## Example Input Values
Example 1:

- Lower bound of theta in degree = `0`
- Upper bound of theta in degree = `180`
- Lower bound of phi in degree = `0`
- Upper bound of phi in degree = `360`
- Field pattern `E(THETA,PHI)` = `cos(THETA)`
- Power pattern `P(THETA,PHI)` = `cos(THETA).^2`

Expected result:

**BEAM AREA (steradians) = 4.20**

Example 2:

If the upper bound of theta is changed to `90` degree, then the result should be:

**BEAM AREA = 2.10 Sr**

## Result Snapshot
Add the MATLAB command window result screenshot here before submission.

**[Insert MATLAB result screenshot here]**

## Conclusion
This assignment shows how MATLAB can be used to compute the beam solid angle of an antenna from its radiation pattern. It helps in understanding spherical coordinates, power patterns, and numerical integration in antenna analysis.
