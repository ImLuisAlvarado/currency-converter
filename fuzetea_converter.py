def pesos_a_fuze(pesos):
    precio_fuze = 19
    
    equivalentes = pesos / precio_fuze
    completos = pesos // precio_fuze
    sobra = pesos % precio_fuze
    
    print(f"${pesos} equivalen a {equivalentes:.2f} Fuze Teas")
    print(f"Puedes comprar {int(completos)} Fuze Teas completos")
    print(f"Te sobran ${sobra}")
