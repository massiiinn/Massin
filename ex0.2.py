def contar_vocals(cadena_usuari):
    vocals = "aeiouAEIOU"
    comptador = 0

    for letra in cadena_usuari:
        if letra in vocals:
            comptador += 1
    
    return comptador

cadena_usuari = input("Introdueix una frase:")
numero_vocals = contar_vocals(cadena_usuari)

print("La frase conté",numero_vocals,"vocals")
#Massin

    