clc;
close all;
clear all;

tmin = input('The lower bound of theta in degree: ');
tmax = input('The upper bound of theta in degree: ');

pmin = input('The lower bound of phi in degree: ');
pmax = input('The upper bound of phi in degree: ');

theta = (tmin:1:tmax) * pi/180;
phi = (pmin:1:pmax) * pi/180;

dth = theta(2) - theta(1);
dph = phi(2) - phi(1);

[THETA, PHI] = meshgrid(theta, phi);

x_str = input('The field pattern : E(THETA,PHI)= ', 's');
x = eval(x_str);

v = input('The power pattern: P(THETA,PHI)= ', 's');
Pn = x.^2;

Prad = sum(sum(Pn .* sin(THETA) * dth * dph));

fprintf('\n Input Parameters: \n--------------------');
fprintf('\n Theta = %.2f', tmin);
fprintf('\n dth : %f', dth);
fprintf('\n tmax : %.2f', tmax);
fprintf('\n Phi = %.2f', pmin);
fprintf('\n dph : %f', dph);
fprintf('\n pmax : %.2f', pmax);
fprintf('\n POWER PATTERN : %s', v);

fprintf('\n\n Output Parameters: \n--------------------');
fprintf('\n BEAM AREA (steradians) = %3.2f\n', Prad);
