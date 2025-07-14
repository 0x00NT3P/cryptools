-----

# CryptoTools: Cifrado y Descifrado AES-256 🔐

¡Hola\! Este es el código correspondiente a la **M2. Tarea 2 - Cifrado y funciones hash** para el **11aEd. Máster Profesional en Seguridad Ofensiva (OSCP)**. 🚀

CryptoTools es una herramienta de línea de comandos que te permite cifrar y descifrar mensajes utilizando el algoritmo AES-256 en modo CBC con padding PKCS7. Está construida con Python, `click` para la interfaz de línea de comandos y `cryptography` para las operaciones criptográficas.

## Características ✨

  * **Cifrado AES-256 CBC:** Protege tus mensajes con un algoritmo de cifrado robusto.
  * **Descifrado AES-256 CBC:** Recupera tus mensajes cifrados de forma segura.
  * **Padding PKCS7:** Asegura que los datos siempre tengan el tamaño de bloque correcto para el cifrado.
  * **Interfaz de línea de comandos intuitiva:** Fácil de usar gracias a `click`.

-----

## Requisitos e Instalación 🛠️

Para usar CryptoTools, primero necesitas asegurarte de tener **Python 3.x** instalado. Luego, te recomendamos crear un **entorno virtual** para manejar las dependencias del proyecto de forma limpia.

### Configuración del Entorno Virtual 🐍

1.  **Crea el entorno virtual:**
    Abre tu terminal o línea de comandos y navega hasta la carpeta de tu proyecto. Ejecuta el siguiente comando:

    ```bash
    python -m venv venv
    ```

    Esto creará una carpeta llamada `venv` que contendrá tu entorno virtual.

2**Activa el entorno virtual:**

      * **En Windows:**
        ```bash
        .\venv\Scripts\activate
        ```
      * **En macOS/Linux:**
        ```bash
        source venv/bin/activate
        ```

    Verás que el nombre de tu entorno (`venv`) aparecerá al inicio de la línea de comandos, indicando que está activado.

3**Instala las dependencias:**
    Con el entorno virtual activado, instala las bibliotecas necesarias usando el archivo `requirements.txt`:

    ```bash
    pip install -r requirements.txt
    ```

    Esto instalará `click` y `cryptography` dentro de tu entorno virtual.

-----

## Uso 🚀

Este programa proporciona dos comandos principales: `encrypt` para cifrar y `decrypt` para descifrar.

### Cifrar un Mensaje 🔒

Para cifrar un mensaje, usa el comando `encrypt`. Necesitarás proporcionar una clave, un vector de inicialización (IV) y el mensaje que quieres cifrar.

```bash
python cryptools.py encrypt --key <TU_CLAVE> --iv <TU_IV> --message "<TU_MENSAJE>"
```

**Ejemplo:**

```bash
python cryptools.py encrypt --key "0123456789abcdef0123456789abcdef" --iv "abcdef9876543210" --message "Hola Mundo Secreto!"
```

  * `--key`: La **clave de cifrado** (debe tener 32 bytes para AES-256).
  * `--iv`: El **vector de inicialización (IV)** (debe tener 16 bytes).
  * `--message`: El **texto** que deseas cifrar.

La salida será el mensaje cifrado en formato hexadecimal.

### Descifrar un Criptograma 🔓

Para descifrar un criptograma, usa el comando `decrypt`. Necesitarás la misma clave y el mismo IV que usaste para cifrar, junto con el criptograma en formato hexadecimal.

```bash
python cryptools.py decrypt --key <TU_CLAVE> --iv <TU_IV> --cryptogram <TU_CRIPTOGRAMA_HEX>
```

**Ejemplo:**

```bash
python cryptools.py decrypt --key "0123456789abcdef0123456789abcdef" --iv "abcdef9876543210" --cryptogram "E8B5C0D7A6F1E0C4B3A291807F6E5D4C3B2A19087766554433221100FFEE1122"
```

  * `--key`: La **clave de descifrado** (debe ser la misma que la usada para cifrar).
  * `--iv`: El **vector de inicialización (IV)** (debe ser el mismo que el usado para cifrar).
  * `--cryptogram`: El **mensaje cifrado** en formato hexadecimal.

La salida será el mensaje original descifrado.

-----

## Consideraciones de Seguridad ⚠️

  * **Manejo de Claves e IVs:** Asegúrate de que tus **claves** y **IVs** sean seguros y se manejen de forma confidencial. **No los expongas en el código** o en ubicaciones fácilmente accesibles. Este ejemplo utiliza el IV fijo para propósitos de prueba, pero en un entorno de producción, los IVs **deben ser generados aleatoriamente** y ser únicos para cada operación de cifrado, y transmitidos junto con el criptograma.
  * **Longitud de la Clave:** Para AES-256, la clave debe tener exactamente **32 bytes** (256 bits).
  * **Longitud del IV:** Para CBC, el IV debe tener exactamente **16 bytes** (128 bits).