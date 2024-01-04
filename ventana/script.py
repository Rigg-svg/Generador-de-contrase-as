import random, string

def mayus(password):

    CARACTERES = string.ascii_uppercase + 'Ñ'
    tam = len(password)

    for _ in range(random.randint(1,5)):
        if tam <= 15:
            password += random.choice(CARACTERES)
            tam = len(password)
        else:
            return password
    
    return password

def numbers(password):
    NUMBERS = string.digits
    tam = len(password)

    for _ in range(random.randint(1,5)):
        if tam <= 15:
            password += random.choice(NUMBERS)
            tam = len(password)
        else:
            return password
    
    return password

def simbols(password):
    SIMBOLS = string.punctuation
    tam = len(password)

    for _ in range(random.randint(1,5)):
        if tam <= 15:
            password += random.choice(SIMBOLS)
            tam = len(password)
        else:
            return password
    
    return password

def generarContrasena(opcionMayus, opcionSimbols, opcionNumbers) -> str:
    CARACTERES  = string.ascii_lowercase + 'ñ' + ' '
    password = ''
    tam = len(password)

    while tam < 8:
    #ninguna opción marcada
        if opcionMayus is not True and opcionSimbols is not True and opcionNumbers is not True:
            for _ in range(random.randint(8, 16)):
                password += random.choice(CARACTERES)


    #opción mayuscula, simbolos y numeros marcadas
        elif opcionMayus and opcionSimbols and opcionNumbers:
            for _ in range(random.randint(1, 8)):
                password += random.choice(CARACTERES)

            password = mayus(password)
            password = simbols(password)
            password = numbers(password)

    #opcion mayuscula y simbolos marcada
        elif opcionMayus and opcionSimbols:
            for _ in range(random.randint(1, 8)):
                password += random.choice(CARACTERES)

            password = mayus(password)
            password = simbols(password)

    #opcion mayuscula y mumeros marcada
        elif opcionMayus and opcionNumbers:
            for _ in range(random.randint(1, 8)):
                password += random.choice(CARACTERES)

            password = mayus(password)
            password = numbers(password)

    #opcion numeros y simbolos marcada
        elif opcionNumbers and opcionSimbols:
            for _ in range(random.randint(1, 8)):
                password += random.choice(CARACTERES)

            password = numbers(password)
            password = simbols(password)

    #opcion masyuscula marcada
        elif opcionMayus:
            for _ in range(random.randint(1, 8)):
                password += random.choice(CARACTERES)

            password = mayus(password)

    #opcion simbolos marcada
        elif opcionSimbols:
            for _ in range(random.randint(1, 8)):
                password += random.choice(CARACTERES)

            password = simbols(password)

    #opcion numeros marcada
        elif opcionNumbers:
            for _ in range(random.randint(1, 8)):
                password += random.choice(CARACTERES)

            password = numbers(password)

        tam = len(password)

    password = list(password)
    random.shuffle(password)
    password = ''.join(password)

    return password