# Aritmética en cuerpos finitos y su aplicación al algoritmo AES

## Memoria

Aquí está el código LaTeX de la memoria. Archivo principal: MAIN.tex

## Presentacion

Aquí está el código LaTeX de la presentación. Archivo principal: main.tex

## AES Python

Aquí está el código en python del ejemplo de los píxeles de colores de la presentación, junto con el último ejemplo que realizo en la presentación (encriptar el logo de la UNED).

### AES.py

Módulo auxiliar que contiene dos funciones principales a llamar:
* encriptar_AES  
  Toma como parámetros:
   * "texto_claro" en formato "byte-string".
   * "clave" en formato "lista de enteros con valores entre 0 y 255".
   * "modo", como el modo de operación: "ECB" o "CBC". "ECB" como valor predeterminado.
   * "bool_padding", para preguntar si se va a usar padding o no. True como valor predeterminado.

  Devuelve:
   * "texto_cifrado" en formato "byte-string".
   * Si bool_padding=True, devuelve una tupla del texto cifrado, separando lo que no es padding de lo que sí lo es.

* desencriptar_AES  
  Toma como parámetros:
   * "texto_cifrado" en formato "byte-string".
   * "clave" en formato "lista de enteros con valores entre 0 y 255".
   * "modo", como el modo de operación: "ECB" o "CBC". "ECB" como valor predeterminado.

  Devuelve:
   * "texto_claro" en formato "byte-string".

### encriptar_imagen.py

Toma imágenes en formato .bmp específicas (solo las tipo Windows BITMAPINFOHEADER. Actualmente, aquellas imágenes que permitan canal alpha: "bytes_por_pixel = 4". En la imagen del logo de la uned lo usé con bytes_por_pixel = 3, sin canal alpha. No voy a complicarme a hacerlo para tomar cualquier tipo de archivo .bmp para este proyecto).

En la clase "BMP", la función "bytes_imagen" toma el contenido visual de la imagen (todos los bytes concernientes a los píxeles).

Tiene dos funciones:
   * "encriptar_imagen" toma una clase tipo BMP, la clave y el modo. Encripta la información concerniente a la imagen usando "encriptar_AES" y crea un nuevo archivo .bmp con dicha información; además, añade la información del padding en un archivo de texto para poder ser descifrado el último bloque.
   * "desencriptar_imagen" toma una clase tipo BMP, la clave y el modo. Descifra la informacíon concerniente a la imagen usando "desencriptar_AES" utilizando la información del padding del archivo de texto. Crea de nuevo un archivo .bmp con la información descifrada.
