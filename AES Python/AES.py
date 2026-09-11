s_box = (
    0x63, 0x7C, 0x77, 0x7B, 0xF2, 0x6B, 0x6F, 0xC5, 0x30, 0x01, 0x67, 0x2B, 0xFE, 0xD7, 0xAB, 0x76,
    0xCA, 0x82, 0xC9, 0x7D, 0xFA, 0x59, 0x47, 0xF0, 0xAD, 0xD4, 0xA2, 0xAF, 0x9C, 0xA4, 0x72, 0xC0,
    0xB7, 0xFD, 0x93, 0x26, 0x36, 0x3F, 0xF7, 0xCC, 0x34, 0xA5, 0xE5, 0xF1, 0x71, 0xD8, 0x31, 0x15,
    0x04, 0xC7, 0x23, 0xC3, 0x18, 0x96, 0x05, 0x9A, 0x07, 0x12, 0x80, 0xE2, 0xEB, 0x27, 0xB2, 0x75,
    0x09, 0x83, 0x2C, 0x1A, 0x1B, 0x6E, 0x5A, 0xA0, 0x52, 0x3B, 0xD6, 0xB3, 0x29, 0xE3, 0x2F, 0x84,
    0x53, 0xD1, 0x00, 0xED, 0x20, 0xFC, 0xB1, 0x5B, 0x6A, 0xCB, 0xBE, 0x39, 0x4A, 0x4C, 0x58, 0xCF,
    0xD0, 0xEF, 0xAA, 0xFB, 0x43, 0x4D, 0x33, 0x85, 0x45, 0xF9, 0x02, 0x7F, 0x50, 0x3C, 0x9F, 0xA8,
    0x51, 0xA3, 0x40, 0x8F, 0x92, 0x9D, 0x38, 0xF5, 0xBC, 0xB6, 0xDA, 0x21, 0x10, 0xFF, 0xF3, 0xD2,
    0xCD, 0x0C, 0x13, 0xEC, 0x5F, 0x97, 0x44, 0x17, 0xC4, 0xA7, 0x7E, 0x3D, 0x64, 0x5D, 0x19, 0x73,
    0x60, 0x81, 0x4F, 0xDC, 0x22, 0x2A, 0x90, 0x88, 0x46, 0xEE, 0xB8, 0x14, 0xDE, 0x5E, 0x0B, 0xDB,
    0xE0, 0x32, 0x3A, 0x0A, 0x49, 0x06, 0x24, 0x5C, 0xC2, 0xD3, 0xAC, 0x62, 0x91, 0x95, 0xE4, 0x79,
    0xE7, 0xC8, 0x37, 0x6D, 0x8D, 0xD5, 0x4E, 0xA9, 0x6C, 0x56, 0xF4, 0xEA, 0x65, 0x7A, 0xAE, 0x08,
    0xBA, 0x78, 0x25, 0x2E, 0x1C, 0xA6, 0xB4, 0xC6, 0xE8, 0xDD, 0x74, 0x1F, 0x4B, 0xBD, 0x8B, 0x8A,
    0x70, 0x3E, 0xB5, 0x66, 0x48, 0x03, 0xF6, 0x0E, 0x61, 0x35, 0x57, 0xB9, 0x86, 0xC1, 0x1D, 0x9E,
    0xE1, 0xF8, 0x98, 0x11, 0x69, 0xD9, 0x8E, 0x94, 0x9B, 0x1E, 0x87, 0xE9, 0xCE, 0x55, 0x28, 0xDF,
    0x8C, 0xA1, 0x89, 0x0D, 0xBF, 0xE6, 0x42, 0x68, 0x41, 0x99, 0x2D, 0x0F, 0xB0, 0x54, 0xBB, 0x16,
)

inv_s_box = (
    0x52, 0x09, 0x6A, 0xD5, 0x30, 0x36, 0xA5, 0x38, 0xBF, 0x40, 0xA3, 0x9E, 0x81, 0xF3, 0xD7, 0xFB,
    0x7C, 0xE3, 0x39, 0x82, 0x9B, 0x2F, 0xFF, 0x87, 0x34, 0x8E, 0x43, 0x44, 0xC4, 0xDE, 0xE9, 0xCB,
    0x54, 0x7B, 0x94, 0x32, 0xA6, 0xC2, 0x23, 0x3D, 0xEE, 0x4C, 0x95, 0x0B, 0x42, 0xFA, 0xC3, 0x4E,
    0x08, 0x2E, 0xA1, 0x66, 0x28, 0xD9, 0x24, 0xB2, 0x76, 0x5B, 0xA2, 0x49, 0x6D, 0x8B, 0xD1, 0x25,
    0x72, 0xF8, 0xF6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xD4, 0xA4, 0x5C, 0xCC, 0x5D, 0x65, 0xB6, 0x92,
    0x6C, 0x70, 0x48, 0x50, 0xFD, 0xED, 0xB9, 0xDA, 0x5E, 0x15, 0x46, 0x57, 0xA7, 0x8D, 0x9D, 0x84,
    0x90, 0xD8, 0xAB, 0x00, 0x8C, 0xBC, 0xD3, 0x0A, 0xF7, 0xE4, 0x58, 0x05, 0xB8, 0xB3, 0x45, 0x06,
    0xD0, 0x2C, 0x1E, 0x8F, 0xCA, 0x3F, 0x0F, 0x02, 0xC1, 0xAF, 0xBD, 0x03, 0x01, 0x13, 0x8A, 0x6B,
    0x3A, 0x91, 0x11, 0x41, 0x4F, 0x67, 0xDC, 0xEA, 0x97, 0xF2, 0xCF, 0xCE, 0xF0, 0xB4, 0xE6, 0x73,
    0x96, 0xAC, 0x74, 0x22, 0xE7, 0xAD, 0x35, 0x85, 0xE2, 0xF9, 0x37, 0xE8, 0x1C, 0x75, 0xDF, 0x6E,
    0x47, 0xF1, 0x1A, 0x71, 0x1D, 0x29, 0xC5, 0x89, 0x6F, 0xB7, 0x62, 0x0E, 0xAA, 0x18, 0xBE, 0x1B,
    0xFC, 0x56, 0x3E, 0x4B, 0xC6, 0xD2, 0x79, 0x20, 0x9A, 0xDB, 0xC0, 0xFE, 0x78, 0xCD, 0x5A, 0xF4,
    0x1F, 0xDD, 0xA8, 0x33, 0x88, 0x07, 0xC7, 0x31, 0xB1, 0x12, 0x10, 0x59, 0x27, 0x80, 0xEC, 0x5F,
    0x60, 0x51, 0x7F, 0xA9, 0x19, 0xB5, 0x4A, 0x0D, 0x2D, 0xE5, 0x7A, 0x9F, 0x93, 0xC9, 0x9C, 0xEF,
    0xA0, 0xE0, 0x3B, 0x4D, 0xAE, 0x2A, 0xF5, 0xB0, 0xC8, 0xEB, 0xBB, 0x3C, 0x83, 0x53, 0x99, 0x61,
    0x17, 0x2B, 0x04, 0x7E, 0xBA, 0x77, 0xD6, 0x26, 0xE1, 0x69, 0x14, 0x63, 0x55, 0x21, 0x0C, 0x7D,
)

IV = b"\xaa"*16


def encriptar_AES(texto_claro, clave, modo="ECB", bool_padding=True):

    numero_de_rondas = 10

    if bool_padding:
        padding = 16 - len(texto_claro) % 16
        texto_claro += bytes([padding]) * padding

    bloques = len(texto_claro) // 16

    if modo == "ECB":
        texto_cifrado = b""
        clave_extendida = KeyExpansion(clave)
        for num_bloque in range(bloques):
            estado = [
                x for x in texto_claro[num_bloque*16:(num_bloque + 1) * 16]]
            addRoundKey(estado, clave)
            for ronda in range(1, numero_de_rondas):
                Round(estado, clave_extendida[ronda * 16:(ronda + 1) * 16])
            finalRound(estado, clave_extendida[-16:])
            texto_cifrado += bytes(estado)
        if bool_padding:
            return texto_cifrado[:-padding], texto_cifrado[-padding:]
        else:
            return texto_cifrado
    elif modo == "CBC":
        texto_cifrado = IV
        clave_extendida = KeyExpansion(clave)
        for num_bloque in range(bloques):
            estado = [texto_claro[i] ^ texto_cifrado[i]
                      for i in range(num_bloque*16, (num_bloque + 1) * 16)]
            addRoundKey(estado, clave)
            for ronda in range(1, numero_de_rondas):
                Round(estado, clave_extendida[ronda * 16:(ronda + 1) * 16])
            finalRound(estado, clave_extendida[-16:])
            texto_cifrado += bytes(estado)
        if bool_padding:
            return texto_cifrado[:-padding], texto_cifrado[-padding:]
        else:
            return texto_cifrado


def desencriptar_AES(texto_cifrado, clave, modo="ECB"):
    numero_de_rondas = 10
    bloques = len(texto_cifrado) // 16

    if modo == "ECB":
        texto_claro = b""
        clave_extendida = KeyExpansion(clave)
        for num_bloque in range(bloques):
            estado = [
                x for x in texto_cifrado[num_bloque*16:(num_bloque + 1) * 16]]
            inv_finalRound(estado, clave_extendida[-16:])
            for ronda in range(1, numero_de_rondas):
                inv_Round(estado, clave_extendida[(
                    ronda + 1) * -16:ronda * -16])
            addRoundKey(estado, clave)
            texto_claro += bytes(estado)
        return texto_claro
    elif modo == "CBC":
        texto_cifrado = IV + texto_cifrado
        texto_claro = b""
        clave_extendida = KeyExpansion(clave)
        for num_bloque in range(bloques):
            estado = [x for x in texto_cifrado[(
                num_bloque + 1) * 16:(num_bloque + 2) * 16]]
            inv_finalRound(estado, clave_extendida[-16:])
            for ronda in range(1, numero_de_rondas):
                inv_Round(estado, clave_extendida[(
                    ronda + 1) * -16:ronda * -16])
            addRoundKey(estado, clave)
            estado = [estado[i] ^ texto_cifrado[num_bloque*16 + i]
                      for i in range(16)]
            texto_claro += bytes(estado)
        return texto_claro


def Round(estado, clave_ronda):
    subBytes(estado)
    shiftRows(estado)
    mixColumns(estado)
    addRoundKey(estado, clave_ronda)


def inv_Round(estado, clave_ronda):
    addRoundKey(estado, clave_ronda)
    inv_mixColumns(estado)
    inv_shiftRows(estado)
    inv_subBytes(estado)


def finalRound(estado, clave_ronda):
    subBytes(estado)
    shiftRows(estado)
    addRoundKey(estado, clave_ronda)


def inv_finalRound(estado, clave_ronda):
    addRoundKey(estado, clave_ronda)
    inv_shiftRows(estado)
    inv_subBytes(estado)


def subBytes(estado):
    for i in range(len(estado)):
        estado[i] = s_box[estado[i]]


def inv_subBytes(estado):
    for i in range(len(estado)):
        estado[i] = inv_s_box[estado[i]]


def shiftRows(estado):
    # Segunda fila
    estado[1], estado[5], estado[9], estado[13] = estado[5], estado[9], estado[13], estado[1]
    # Tercera fila
    estado[2], estado[6], estado[10], estado[14] = estado[10], estado[14], estado[2], estado[6]
    # Cuarta fila
    estado[3], estado[7], estado[11], estado[15] = estado[15], estado[3], estado[7], estado[11]


def inv_shiftRows(estado):
    # Segunda fila
    estado[1], estado[5], estado[9], estado[13] = estado[13], estado[1], estado[5], estado[9]
    # Tercera fila
    estado[2], estado[6], estado[10], estado[14] = estado[10], estado[14], estado[2], estado[6]
    # Cuarta fila
    estado[3], estado[7], estado[11], estado[15] = estado[7], estado[11], estado[15], estado[3]

# Multiplicar por 2 en el cuerpo GF(256), cociente el polinomio x^8 + x^4 + x^3 + x^1 + 1
# Si a_7 = 0, es mover bits a la izq. Si es a_7 = 1, es mover, y luego sumar con 11b
# Sé que es más eficiente tomar una tabla, pero hay que practicar.


def xtime(x, n=2):
    if n == 0:
        return 1
    if n == 1:
        return x
    else:
        x = x << 1 if x < 0x80 else x << 1 ^ 0x11b
        x = xtime(x, n-1)
    return x


def mixColumns(estado):
    # Consultar manual sección 4.1.2 en https://link.springer.com/chapter/10.1007/978-3-662-60769-5_4
    for i in range(4):
        j = 4 * i
        t = estado[j] ^ estado[j + 1] ^ estado[j + 2] ^ estado[j + 3]
        u = estado[j]
        estado[j] ^= xtime(estado[j] ^ estado[j + 1]) ^ t
        estado[j + 1] ^= xtime(estado[j + 1] ^ estado[j + 2]) ^ t
        estado[j + 2] ^= xtime(estado[j + 2] ^ estado[j + 3]) ^ t
        estado[j + 3] ^= xtime(estado[j + 3] ^ u) ^ t


def inv_mixColumns(estado):
    # Consultar manual sección 4.1.3 en https://link.springer.com/chapter/10.1007/978-3-662-60769-5_4
    for i in range(4):
        # Preprocessing
        j = 4 * i
        u = xtime(xtime(estado[j] ^ estado[j + 2]))
        v = xtime(xtime(estado[j + 1] ^ estado[j + 3]))
        estado[j] ^= u
        estado[j + 1] ^= v
        estado[j + 2] ^= u
        estado[j + 3] ^= v
        # mixColumns
        t = estado[j] ^ estado[j + 1] ^ estado[j + 2] ^ estado[j + 3]
        u = estado[j]
        estado[j] ^= xtime(estado[j] ^ estado[j + 1]) ^ t
        estado[j + 1] ^= xtime(estado[j + 1] ^ estado[j + 2]) ^ t
        estado[j + 2] ^= xtime(estado[j + 2] ^ estado[j + 3]) ^ t
        estado[j + 3] ^= xtime(estado[j + 3] ^ u) ^ t


def addRoundKey(estado, RoundKey):
    for i in range(len(estado)):
        estado[i] ^= RoundKey[i]


def f_aux_key_expansion(palabra, ronda):
    # Rotación cíclica y S_box
    aux = palabra[0]
    for i in range(0, len(palabra)-1):
        palabra[i] = s_box[palabra[i-3]]
    palabra[3] = s_box[aux]
    # Suma al primer byte 02^(j-1) en el cuerpo
    palabra[0] ^= xtime(2, ronda - 1)
    return palabra


def KeyExpansion(clave):
    clave_extendida = clave
    for n in range(1, 11):
        for i in range(4):
            if not i % 4:
                clave_extendida += [clave_extendida[16*(n-1) + j] ^ f_aux_key_expansion(
                    clave_extendida[16*n - 4:16*n], n)[j] for j in range(4)]
            else:
                clave_extendida += [clave_extendida[16*(n-1) + j + 4*i] ^ clave_extendida[16*(
                    n-1) + j + 4*i + 12] for j in range(4)]
    return clave_extendida


if __name__ == "__main__":
    clave = [x for x in range(16)]
    modo = "ECB"
    IV = b"\xaa"*16
    texto_claro = "FF0000FF00FF00FF0000FFFF606060FF"

    print("Texto claro = ", texto_claro)
    texto_claro = bytes([int(texto_claro[x:x+2], 16)
                        for x in range(0, len(texto_claro), 2)])
    cifrado = encriptar_AES(texto_claro, clave, modo, bool_padding=False)

    claro = desencriptar_AES(cifrado, clave, modo)

    if texto_claro == claro[-16:]:
        print("funciona")
        print([hex(x) for x in cifrado])
        texto_cifrado = "".join(
            [hex(x)[2:] if x >= 16 else "0" + str(hex(x)[2:]) if x > 0 else "00" for x in cifrado])
        print(texto_cifrado)
    else:
        print([hex(x) for x in cifrado])
        print([hex(x) for x in claro])
