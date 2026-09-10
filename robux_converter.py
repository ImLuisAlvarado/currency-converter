def convertidor_robux(pesos):
    TASA_CAMBIO = 0.25
    return pesos * TASA_CAMBIO

#try: 
    #monto_pesos = float(input("Ingresa la cantidad de pesos (MXN): "))

    #resultado = convertidor_robux(monto_pesos)
    
    #print(f"Te alcanza para aproximadamente: {int(resultado)} Robux!")

#except ValueError:
    #print("Ingresa un valor")