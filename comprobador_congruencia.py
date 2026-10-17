def comprobar_congruencia(a, b, modulo):
    return a % modulo == b % modulo


def main():
    print("AP 22 - Comprobador de congruencia")

    # Pedir los tres datos.
    try:
        a = int(input("Introduce el primer número entero: "))
        b = int(input("Introduce el segundo número entero: "))
        modulo = int(input("Introduce el módulo (entero positivo): "))
    except ValueError:
        print("Error: debes introducir números enteros.")
        return

    # Validar el módulo.
    if modulo <= 0:
        print("Error: el módulo debe ser mayor que cero.")
        return

    # Calcular y mostrar los restos.
    resto_a = a % modulo
    resto_b = b % modulo

    print()
    print(f"{a} % {modulo} = {resto_a}")
    print(f"{b} % {modulo} = {resto_b}")

    # Mostrar el resultado.
    if comprobar_congruencia(a, b, modulo):
        print(f"Sí: {a} y {b} son congruentes módulo {modulo}.")
    else:
        print(f"No: {a} y {b} no son congruentes módulo {modulo}.")


if __name__ == "__main__":
    main()