# Instalación de FFmpeg

# Creación de un entorno virtual

Para la correcta ejecución de la práctica se requieren instaladas algunas librerías o paquetes de Python. A continuación, los pasos a seguir para realizar la creación de un entorno virtual que nos permite crear un espacio aislado para un proyecto, con su propio conjunto de dependencias, independientemente de las que se instalen en el sistema global. 

### Para Windows
1. Crear un directorio para la práctica. Añadir el número de la práctica al final del nombre.
   
    ```bash
    mkdir Lab_SA
    cd Lab_SA
    ```

2. Una vez dentro de ese directorio, dar click derecho y abrir una terminal o consola. Posteriormente ejecutar el comando:

    ```bash
    python -m venv venv
    ```

<p align="center">
   <img src="https://github.com/Javiec369/SA_practice-1/assets/87388852/e65a1d3b-22a1-4e62-b51a-acb7cabdcc91" width="470" height="340"/>
</p>

3. Activar el entorno virtual (desde la terminal) ejecutando:

    - En Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - En macOS y Linux:

        ```bash
        source venv/bin/activate
        ```

4. Descargar el archivo `requirements.txt` desde el [repositorio](https://github.com/Javiec369/SA_practice-1/tree/main/Laboratorios%202024-2/Lab_SA1) asignado a la práctica y guardarlo dentro del directorio.

5. Ejecutar el siguiente comando en la terminal para la instalación de las librerías.

    ```bash
    pip install -r requirements.txt
    ```

6. Verificar que las librerías han sido instaladas correctamente.

    ```bash
    pip list
    ```



- Creación del entorno virtual dentro de un directorio o carpeta.



- Instalación de los paquetes/librerías contenidas dentro del archivo `requirements.txt`.

<img src="https://github.com/Javiec369/SA_practice-1/assets/87388852/ec432bcb-ecbe-4fad-a5aa-40b8a4259b39" width="570" height="440"/>
