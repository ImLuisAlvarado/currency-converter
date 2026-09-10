def convertBobtoMxn(mxn):
    cambio = 48.10
    bolivianos = mxn * cambio
    return bolivianos

# Nomas pa ya tu sabe
def convertMxntoBob(bob):
    cambio = 1.36
    mexicanos = bob * cambio
    return mexicanos
try: 
    print("=====================================================")
    peso = float(input("Ingresa la cantidad de peso mexicano: "))

    resultado = convertBobtoMxn(peso)
    print(resultado)
    
except ValueError:
    print("Ingresa valor valido.")