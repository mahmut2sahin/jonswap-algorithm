# constant of gravitational acceleration
g = 9.80665

# input of wind data
u = float(input("Enter Wind Speed in m/s2: "))
fkm = float(input("Enter Fetch Length in km: "))
f = fkm * 1000
thr = float(input("Enter Wind Duration in hours: "))
t = thr * 60 * 60

# defining wind stress factor
ua = 0.71 * (u ** 1.23)

# fetch and duration parameters are found
Fstar = (g * f) / (ua ** 2)
tstar = (g * t) / ua

# Fully developed case
Hstarfully = 0.243
Tstarfully = 8.13

Hfully = round((Hstarfully * (ua ** 2)) / g, 2)
Tfully = round((Tstarfully * ua) / g, 2) / 1.05

# Developing Case
Fcondstar = (tstar / 68.8) ** (3 / 2)

print("Results:")

if Fcondstar < Fstar:
    print("Duration Limited Case")
    Hstar = 0.0016 * (Fcondstar ** (1 / 2))
    Tstar = 0.286 * (Fcondstar ** (1 / 3))

    Hdevelop = round((Hstar * (ua ** 2)) / g, 2)
    Tdevelop = round((Tstar * ua) / g / 1.05, 2)
else:
    print("Fetch Limited Case")
    Hstar = 0.0016 * (Fstar ** (1 / 2))
    Tstar = 0.286 * (Fstar ** (1 / 3))

    Hdevelop = round((Hstar * (ua ** 2)) / g, 2)
    Tdevelop = round((Tstar * ua) / g / 1.05, 2)

# comparison between fas and developing
if Hdevelop < Hfully:
    print(f"Significant Height: {Hdevelop} m")
    print(f"Significant Period: {Tdevelop} sec")
else:
    print("Fully Arisen Sea")
    print(f"Significant Height: {Hfully} m")
    print(f"Significant Period: {Tfully} sec")










    


