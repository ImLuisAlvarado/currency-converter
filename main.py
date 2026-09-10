from convert_bol import convertBobtoMxn
from won_converter import mxn_to_krw
from usd_converter import convert_to_usd
from robux_converter import convertidor_robux
from fuzetea_converter import pesos_a_fuze
from cup_converter import mxn_to_cup

from time import sleep


while True:
    print("Bienvenido al convertidor divisas de MXN a otras monedas")
    
    try:
        opcion = int(input("Seleccione una de las siguientes opciones: " \
        "\n1. Convertir de MXN a BOL " \
        "\n2. Convertir de MXN a WON " \
        "\n3. MXN a ROBUX " \
        "\n4. MXN a CUP " \
        "\n5. MXN a USD" \
        "\n6. MXN a FuzeTeas" \
        "\nIngrese el número de la opción deseada: "))

        if opcion not in [1, 2, 3, 4, 5, 6]:
            raise ValueError("Opción fuera de rango")

    except ValueError:
        print("\nError: Por favor, ingrese un número de opción válido.")
        sleep(2)
        print("\n")
        continue 

# Holaaa soy un comentario
    try:
        mxn = float(input("Ingrese la cantidad en MXN: "))
    except ValueError:
        print("\nError: Por favor, ingrese una cantidad numérica válida.")
        sleep(2)
        print("\n")
        continue

    print("\n")
    if opcion == 1:
        bolivianos = convertBobtoMxn(mxn)
        print(f"{mxn} MXN son {bolivianos} BOB")
        sleep(4)

    elif opcion == 2:
        krw = mxn_to_krw(mxn)
        sleep(4)

    elif opcion == 3:
        robux = convertidor_robux(mxn)
        print(f"{mxn} MXN son {robux} ROBUX")
        sleep(4)

    # Me pregunto si será una limusina
    elif opcion == 4:
        cup = mxn_to_cup(mxn)
        print(f"{mxn} MXN son {cup} CUP")
        sleep(4)

    elif opcion == 5:
        convert_to_usd(mxn)
        sleep(4)

    elif opcion == 6:
        pesos_a_fuze(mxn)
        sleep(6)

    print("\n")