close all;
clear all;

Distance = 1
Frequency = [1.8*10^9 3.5*10^9];
AntennaGainTx = 5;
AntennaGainRx = 5;
Watt = 80
ShadowFading = 1.7
OtherLoss = 10
PenetrationLoss = 10
%RainLoss
%SnowLoss
n = 2.16 %n er path loss exponent

TransmitterPower = 10*log10(Watt/0.001)
Wavelength = (3.0*10^8./(Frequency))

PathLossCI = 20*log10(4*pi*1./Wavelength)+10*2.16*log10(Distance/1)+ShadowFading %CI
path2 = 20*log10(4*pi*1000/0.0856549); %base freespace PL



R =zeros(100,1);
Distance = (1:10:1000);
for W = 1:size(Wavelength,2)
    R =zeros(100,1);
    for D = 1:size(Distance,2)
       PathLossCI = 20*log10(4*pi*1/Wavelength(W))+10*2.16*log10(Distance(D)/1)+ShadowFading; %CI
       path2 = 20*log10(4*pi*Distance(D)/Wavelength(W)); %Standard
       R(D)  = TransmitterPower + AntennaGainTx + AntennaGainRx - PathLossCI - OtherLoss-PenetrationLoss;
    end
    plot(Distance,R)
    hold on
end

%%










