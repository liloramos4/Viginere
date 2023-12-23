LETRAS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def main():
    print("Bienvenido al cifrador y descifrador de mensajes.")
    while True:
        print("|-------------------------|")
        print("|  1 Cifrar mensaje      |")
        print("|  2 Descifrar mensaje   |")
        print("|  3 Salir               |")
        print("|-------------------------|")
        opt = int(input("Ingrese opción: "))
        
        if opt == 1:
            cadena = input('Introduce el mensaje que quieras cifrar: ').lower()
            clave = input('Introduce la clave: ').lower()
            print(cifrar_mensaje(clave, cadena))  # Cambio aquí
        elif opt == 2:
            cadena = input('Introduce el mensaje que quieras descifrar: ').lower()
            clave = input('Introduce la clave: ').lower()
            print(descifrar_mensaje(clave, cadena))  # Cambio aquí
        elif opt == 3:
            break
        else:
            print("Opción no válida. Por favor, seleccione 1, 2 o 3.")

def cifrar_mensaje(clave, mensaje):
    return traductor_mensaje(clave, mensaje, 'encriptar')

def descifrar_mensaje(clave, mensaje):
    return traductor_mensaje(clave, mensaje, 'descifrar')

def traductor_mensaje(clave, mensaje, accion):
    traducido = []
    indice_clave = 0
    clave = clave.upper()

    for symbol in mensaje:
        if symbol.isalpha():  # Ignorar caracteres que no sean letras
            num = LETRAS.find(symbol.upper())
            if num != -1:
                if accion == 'encriptar':
                    num += LETRAS.find(clave[indice_clave])
                elif accion == 'descifrar':
                    num -= LETRAS.find(clave[indice_clave])
                num %= len(LETRAS)
                if symbol.isupper():
                    traducido.append(LETRAS[num])
                elif symbol.islower():
                    traducido.append(LETRAS[num].lower())
                indice_clave += 1
                if indice_clave == len(clave):
                    indice_clave = 0
        else:
            traducido.append(symbol)
    return ''.join(traducido)

if __name__ == '__main__':
    main()
