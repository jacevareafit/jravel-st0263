# Proyecto Nro 1


| Materia  | Tópicos especiales en Telemática - ST0263 |
| ------------- | ------------- |
| Integrantes  |  Kevin Alejandro Sossa Chavarria (kasossac@eafit.edu.co) |
|  | Jacobo Rave Londoño (jravel@eafit.edu.co)  |
|   | Daniel Jaramillo Valencia (djaramillv@eafit.edu.co) |
|   | Antonio Carmona Gaviria (acarmonag@eafit.edu.co) |
| Profesor  | Edwin Nelson Montoya Munera (emontoya@eafit.edu.co) |


# Objetivo

Diseñar y desarrollar un DFS (Distributed File System) 

# Objetivos cumplidos

- [x] La escritura y lectura de los archivos debe de ser entre el Cli y el DataNode. ()
- [x] Función ‘list’ completa.
- [x] Función ‘search’ completa.
- [x] Función ‘get’ completa.
- [x] Función ‘put’ completa.
- [x] El archivo debe estar en mas de un dataNode

# Informacion de la arquitectura

Tabla de componentes


| Componente | Funcionalidad | Puertos |
| :---         |     :---     |          :--- |
| Cli   | El cli recibe las instrucciones por parte del usuario para invocar las funcionalidades desarrolladas interactuando con los otros componentes      | 23.21.76.201:80    |
| NameNode    | Recibe los request del cli, se encarga de encontrar si un archivo esta en un DataNode y le envia al Cli la ubicacion del Datanode el cual tiene el archivo       |  18.213.158.32:50050     |
| DataNode1    | Guarda los archivos que sube el usuario a traves del Cli, funciona como una persistencia para que el usuario pueda despues acceder a estos      | 3.225.162.204:50051    |
| DataNode2     | Guarda los archivos que sube el usuario a traves del Cli, funciona como una persistencia para que el usuario pueda despues acceder a estos      | 3.90.130.81:50051     |


# Arquitectura

Diseño de arquitectura propuesta para el proyecto1 primer acercamiento

![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/8e5e00ae-e550-4e66-b4b5-99e7d7deebcd)

Diseño de arquitectura propuesto a desarrollar

![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/482c95e5-67f1-43f6-a65b-e03eb79100ad)

# Como usar

Guia de uso:

Instalacion programas necesarios para cada maquina.

#Dependencias para la maquina linux
sudo apt update

### Git
sudo apt-get install git

### gRPC
sudo python -m pip install grpcio
sudo python -m pip install grpcio

### Repo
git clone https://github.com/jacevareafit/jravel-st0263.git

# Ejecución del programa

para inicializar el namenode debemos ingresar a la ruta del nameNode y ejecutar el archivo main.py
  - ./jravel-st0263/proyecto_final/namenode/ python3 main.py
  - ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/1ec95014-b1d3-4f6c-b26f-406fc7cca596)


para inicializar el Datanode debemos ingresar a la ruta del Datanode y ejecutar el archivo main.py
  - ./jravel-st0263/proyecto_final/node/ python3 main.py
  - ![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/e5a9271c-3689-4809-bfdd-f426600bb9b7)


para inicializar el Cli debemos ingresar a la ruta del Cli y ejecutar el archivo main.py
  - ./jravel-st0263/proyecto_final/cli/ python3 main.py
  - A continuacion el Cli desplegara un menu con las funcionalidades desarrolladas.
![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/65886bf9-3033-4425-8544-51292b93406c)

### obtener archivos
![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/8f163cb3-68d6-4b50-84f2-0072b9a7182e)

### Guardar archivo (se debe ingresar la ruta relativa)
![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/baa1acb3-5ae1-4ecd-ae5e-6c0ea0fbc0e3)

### Buscar archivos (se debe ingresar una expresion regular)
![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/41296b86-97e7-4180-980d-9f40f6b1b2c7)

### Listar archivos
![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/6d7249c3-78a4-4b18-8d2a-aa205fd824d1)














