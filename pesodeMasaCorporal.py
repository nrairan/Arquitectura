n=(int(input("Ingresa el numero de personas")))

for i in range(n):
    print("Ingresando datos de persona ",n)
    nombre=(input("Ingresa tu nombre"))
    apellido=(input("Ingresa tu apellido"))
    estatura=(float(input("Ingresa tu estatura en metros")))
    peso=(float(input("Ingresa tu peso en kg")))

    masaCorporal=peso/(estatura**2)
    print(nombre, apellido,", tu estado es: ")

    if masaCorporal>=35.0:
        print("Estado rojo/Obesidad")
    elif masaCorporal>=25.0 and masaCorporal<=34.9:
        print("Estado amarillo/Aceptable")
    elif masaCorporal>=18.5 and masaCorporal<=24.9:
        print("Estado verde/Saludable")
    else:
        if masaCorporal<18.5:
            print("Demasiado delgado")
        else:
            print("Demasiado sobrepeso")


