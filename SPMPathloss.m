%% fisk
K1 = [22 28.3];
K2 = 44.9;
K3 = 5.83;
K4 = 0.5;
K5 = -6.55;
TXheight = 25
RXheight = 1.5
AntennaGainTx = 15;
AntennaGainRx = 5;

HTeff = TXheight

Frequency = [1.8*10^9 3.5*10^9];
Wavelength = (3.0*10^8./(Frequency))

Watt = 80;
TransmitterPower = 10*log10(Watt/0.001);
TransmitterPower = [51 40]

Tdistance = 1000;

R =zeros(100,1);
Distance = (1:10:Tdistance);


for W = 1:size(Wavelength,2)
    R =zeros(Tdistance/10,1);
    for D = 1:size(Distance,2)
       %R(D) = 20*log10(4*pi*1/Wavelength(W))+10*2.16*log10(Distance(D)/1)+1.7; % CI
       DiffractionLoss = KNDiff1(Distance(D),Wavelength(W),TXheight+40);
       R(D) = K1(W)+K2*log10(Distance(D))+K3*log10(HTeff)+K4*DiffractionLoss+K5*log10(Distance(D))*log10(HTeff);
    end
    plot(Distance,R)
    hold on
end
legend("1.8Ghz", "3,5Ghz")
xlabel("Distance (m)")
ylabel("db")
title("Pathloss")
figure()
hold off

for W = 1:size(Wavelength,2)
    R =zeros(Tdistance/10,1);
    for D = 1:size(Distance,2)
       %SPMPathLoss = 20*log10(4*pi*1/Wavelength(W))+10*2.16*log10(Distance(D)/1)+1.7; %CI 
       DiffractionLoss = KNDiff1(Distance(D),Wavelength(W),TXheight-20);
       SPMPathLoss = K1(W)+K2*log10(Distance(D))+K3*log10(HTeff)+K4*DiffractionLoss+K5*log10(Distance(D))*log10(HTeff);
       R(D)  = TransmitterPower(W) + AntennaGainTx + AntennaGainRx - SPMPathLoss;
    end
    plot(Distance,R)
    hold on
end
legend("1.8Ghz", "3,5Ghz")
xlabel("Distance (m)")
ylabel("dbm")
title("Signal level")




