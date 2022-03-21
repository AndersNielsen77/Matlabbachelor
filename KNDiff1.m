%Distance is the distance between the transmitter and receiver in meters
%lambda is the wavelength of the frequency in meters
%h is the height of the obsctruction above LOS in meters

function Diffraction = KNdiff1(distance,lambda,h)

d1 = distance/2;
d2 = distance/2;

v = h*(sqrt(2*(d1+d2)/(lambda*d1*d2)));


 if v <= -1
    Diffraction=0;
 elseif v <= 0
    Diffraction=20*log10(0.5-0.62*v);
 elseif v <= 1
    Diffraction=20*log10(0.5*exp(-0.95*v));
 elseif v <= 2.4
    Diffraction=20*log10(0.4-sqrt(0.1184-(0.38-0.1*v)^2));
 else
    Diffraction=20*log10(0.225/v);
 end

%v_vector=v:0.01:v+100; exact udregning
%F=((1+1i)/2)*sum(exp((-1i*pi*(v_vector).^2)/2));

%Diffraction=20*log10(abs(F));





end
