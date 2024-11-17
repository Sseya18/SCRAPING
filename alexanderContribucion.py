def encontrar_nombre_mas_parecido(nombre_objetivo, resultados):
    # Convertir el nombre objetivo a minúsculas
    print("entra")
    lista_nombres=[]
    for resultado in resultados:
        a=resultado.text.split("\n")[0].strip()
        if a=="Estado: con conexión":
            a=resultado.text.split("\n")[1].strip()
        lista_nombres.append(a)
    print(lista_nombres)
    nombre_objetivo = nombre_objetivo.lower()
    partes_objetivo = nombre_objetivo.split()
    primer_nombre_objetivo = partes_objetivo[0]  # Primer nombre
    # Primer apellido (paterno)
    if(len(partes_objetivo)==2):
        apellido_paterno_objetivo = partes_objetivo[1]
    else:
        apellido_paterno_objetivo = partes_objetivo[2]
    mejor_nombre = ""
    mayor_coincidencia = 0
    posicion_mejor_nombre = -1

    for i, nombre in enumerate(lista_nombres):
        # Convertir el nombre actual a minúsculas
        nombre = nombre.lower()
        print(nombre)
        partes_nombre = nombre.split()
        print(partes_nombre)
        if len(partes_nombre) == 2:  # Validar que tenga suficiente información
            coincidencias = 0
            primer_nombre_actual = partes_nombre[0]
            apellido_paterno_actual = partes_nombre[1]
            if primer_nombre_objetivo == primer_nombre_actual:
                coincidencias += 1
            if apellido_paterno_objetivo == apellido_paterno_actual:
                coincidencias += 1
            if coincidencias > mayor_coincidencia:
                mayor_coincidencia = coincidencias
                mejor_nombre = nombre
                posicion_mejor_nombre = i  # Guardar la posición
            continue
        primer_nombre_actual = partes_nombre[0]
        print(primer_nombre_actual)
        apellido_paterno_actual = partes_nombre[2]
        print(apellido_paterno_actual)
        # Contar coincidencias
        coincidencias = 0
        if primer_nombre_objetivo == primer_nombre_actual:
            coincidencias += 1
        if apellido_paterno_objetivo == apellido_paterno_actual:
            coincidencias += 1

        # Actualizar si es el más parecido
        if coincidencias > mayor_coincidencia:
            mayor_coincidencia = coincidencias
            mejor_nombre = nombre
            posicion_mejor_nombre = i  # Guardar la posición


    return mejor_nombre, mayor_coincidencia, posicion_mejor_nombre


def filtrar(resultados):
    lista_nombres=[]
    for resultado in resultados:
        a=resultado.text.split("\n")[0].strip()
        if a=="Estado: con conexión":
            a=resultado.text.split("\n")[1].strip()
        lista_nombres.append(a)
    print(lista_nombres)
    return lista_nombres


def liberar():
    print("hello world")