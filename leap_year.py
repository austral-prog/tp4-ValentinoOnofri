def leap_year():
    año = int(input("Ingrese un año: "))
    if (año % 4 == 0) and (año % 100 != 0):
        print(f"El año {año} es bisiesto")
    elif (año % 100 == 0) and (año % 400 == 0):
        print(f"El año {año} es bisiesto")
    else:
        print(f"El año {año} no es bisiesto")
#leap_year()