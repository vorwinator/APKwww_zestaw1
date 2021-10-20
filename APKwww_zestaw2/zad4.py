def przelicznik(temperature, temperature_type):
    if temperature_type == "F":
        return(temperature * (9/5) + 32)
    elif temperature_type == "R":
        return((temperature + 273.15) * 1.8)
    elif temperature_type == "K":
        return(temperature + 273.15)
    else:
        return("podano niewłaściwy typ temperatury")

print(przelicznik(15, "F"))
print(przelicznik(15, "R"))
print(przelicznik(15, "K"))
print(przelicznik(15, "błąd"))