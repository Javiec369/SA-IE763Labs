# Creación de un Entorno Virtual

Es necesario realizar una serie de pasos que nos permitirán tener las librerías requeridas para la ejecución de los programas dentro de un entorno virtual.

1. Crear un directorio para la práctica. Añadir el número de la práctica al final del nombre.

    ```bash
    mkdir Lab_SA
    cd Lab_SA
    ```

2. Una vez dentro de ese directorio, ejecutar el siguiente comando en la terminal para la creación del entorno virtual.

    ```bash
    python -m venv venv
    ```

3. Activar el entorno virtual (desde la terminal) ejecutando:

    - En Windows:

        ```bash
        .\venv\Scripts\activate
        ```

    - En macOS y Linux:

        ```bash
        source venv/bin/activate
        ```

4. Descargar el archivo `requirements.txt` desde el [repositorio](URL_DEL_REPOSITORIO) asignado a la práctica.

5. Guardar el archivo `.txt` en el directorio creado para la práctica y ejecutar el siguiente comando dentro del directorio para realizar la instalación de las librerías.

    ```bash
    pip install -r requirements.txt
    ```

6. Verificar que las librerías han sido instaladas correctamente utilizando el siguiente comando nuevamente en la terminal.

    ```bash
    pip list
    ```
