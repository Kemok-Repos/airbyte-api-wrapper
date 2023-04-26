# Kemok Airbyte API Wrapper

Python API wrapper para Airbyte

Este proyecto está pensado para usarse como dependencia en otros proyectos, por lo que al instanciar la clase principal
`AirbyteWrapper`, se le deben pasar como parámetros el usuario y password de Airbyte a utilizar.

## Instrucciones de uso en otro proyecto
1. Instalar el proyecto como dependencia.
2. Importar la clase `AirbyteWrapper` desde el service y utilizar sus métodos.

## Instrucciones para modificar el código
1. Crear un github codespace o clonar el repositorio.
2. Inicializar el entorno virtual con el comando `poetry shell`. Esto creará una carpeta .venv en el root del proyecto y la activará.
3. Instalar las dependencias con el comando `poetry install`.
4. Si se desea agregar una nueva dependencia, usar el comando `poetry add <dependencia>`.

