from math import ceil
from AES import encriptar_AES, desencriptar_AES


class BMP:
    def __init__(self, archivo):
        self.contenido = open(archivo, "rb").read()

        # Windows BITMAPINFOHEADER, posición del byte del ancho y el alto
        pos_byte_ancho = 18
        pos_byte_alto = 22
        bytes_por_pixel = 4

        # Leer el contenido del ancho y alto de la imagen en píxeles
        self.ancho = int.from_bytes(
            self.contenido[pos_byte_ancho:pos_byte_ancho + 4], byteorder='little')
        self.alto = int.from_bytes(
            self.contenido[pos_byte_alto:pos_byte_alto + 4], byteorder='little')
        self.bytes_ancho = bytes_por_pixel * self.ancho

        # Padding de ancho en bytes
        self.padding = 4 - self.bytes_ancho % 4

        # Leer donde comienza la información de la imagen
        self.comienzo = int.from_bytes(
            self.contenido[10:14], byteorder='little')

    def bytes_imagen(self):
        imagen = self.contenido[self.comienzo:]

        if self.padding != 4:
            imagen_aux = b""
            for x in range(self.alto):
                imagen_aux += imagen[ceil(self.bytes_ancho / 4) * 4 * x:
                                     ceil(self.bytes_ancho / 4) * 4 * x + self.bytes_ancho]
            imagen = imagen_aux
        return imagen


def encriptar_imagen(imagen, clave, modo):
    nombre = arhivo_a_encriptar[:-4] + "_enc_" + modo + arhivo_a_encriptar[-4:]
    nombre = "logo/pixeles_bloque.bmp"
    archivo_nuevo = open(nombre, "wb")

    texto_claro = imagen.bytes_imagen()

    imagen_encriptada, padding_enc = encriptar_AES(texto_claro, clave, modo)
    info_padding = open(
        arhivo_a_encriptar[:-4] + "_enc_" + modo + "_infoPadding.txt", "wb")
    info_padding.write(padding_enc)
    info_padding.close()

    if imagen.padding != 4:
        imagen_aux = b""
        for x in range(imagen.alto):
            imagen_aux += imagen_encriptada[imagen.bytes_ancho * x:
                                            imagen.bytes_ancho * (x + 1)] + b"\x00" * imagen.padding
        imagen_encriptada = imagen_aux

    archivo_nuevo.write(imagen.contenido[:imagen.comienzo] + imagen_encriptada)
    archivo_nuevo.close()


def desencriptar_imagen(imagen, clave, modo):
    nombre = arhivo_a_encriptar[:-4] + "_enc_" + \
        "_des_" + modo + arhivo_a_encriptar[-4:]
    archivo_nuevo = open(nombre, "wb")

    padding_enc = open(
        arhivo_a_encriptar[:-4] + "_enc_" + modo + "_infoPadding.txt", "rb").read()
    texto_cifrado = imagen.bytes_imagen()
    imagen_desencriptada = desencriptar_AES(
        texto_cifrado + padding_enc, clave, modo)

    if imagen.padding != 4:
        imagen_aux = b""
        for x in range(imagen.alto):
            imagen_aux += imagen_desencriptada[imagen.bytes_ancho * x:
                                               imagen.bytes_ancho * (x + 1)] + b"\x00" * imagen.padding
        imagen_desencriptada = imagen_aux

    archivo_nuevo.write(
        imagen.contenido[:imagen.comienzo] + imagen_desencriptada)
    archivo_nuevo.close()


arhivo_a_encriptar = "logo/prueba.bmp"
modo = "ECB"  # ECB o CBC
clave = [0 for x in range(16)]

imagen = BMP(arhivo_a_encriptar)
encriptar_imagen(imagen, clave, modo)

im_enc = BMP(arhivo_a_encriptar[:-4] +
             "_enc_" + modo + arhivo_a_encriptar[-4:])
desencriptar_imagen(im_enc, clave, modo)
