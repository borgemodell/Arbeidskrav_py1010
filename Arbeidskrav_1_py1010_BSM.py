"""

Arbeidskrav 1 py1010 
Børge Modell
2026 09 25

"""

FEB = 5000 # [Forsikring Elbil]
FBB = 7500 # [Forsikring Bensinbil]
TFA = 8.38 * 365 # [Trafikkforsikringsavgift]
DEB = (0.2 * 10000) * 2 # [Drivstoffbruk Elbil]
DBB = 1 * 10000 # [Drivstoffbruk Bensinbil]
BEB = 0.1 * 10000 # [Bomavgift Elbil]
BBB = 0.3 * 10000 # [Bomavgift Bensinbil]
print(FEB, FBB, TFA, DEB, DBB, BEB, BBB)

ÅEB = FEB+TFA+DEB+BEB # [Årskostnad Elbil]
ÅBB = FBB+TFA+DBB+BBB # [Årskostnad Bensinbil]
print("ÅEB =", ÅEB)
print("ÅBB =", ÅBB)

ÅKD = ÅBB - ÅEB # [Årlig kostnadsdifferanse 10000km]
print("ÅKD =", ÅKD)
