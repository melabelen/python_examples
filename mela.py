def campaña (tupla):
  for element in tupla:
    person, sex = element
    prefix = "Estimado" if sex == "m" else "Estimada"
    print(prefix, person, "vote por mi")
      

def imprimirN (tupla,posicion,cantidad):
  i=0
  while(i<cantidad):
    person,sex = tupla[posicion+i]
    prefix = "Estimado" if sex == "m" else "Estimada"
    print (prefix, person , "vote por mi")
    i+=1



tu1 = ("Manu","m")
tu2 = ("Mela","f")
tu3 = ("Fran","m")
tu4 = ("Agus","f")
tu5 = ("Caro","m")
tu = (tu1, tu2,tu3,tu4,tu5)

imprimirN(tu,1,3)
print("-"*80)
print ( "\n", "El otro ejercicio:", "\n" )
campaña (tu)
