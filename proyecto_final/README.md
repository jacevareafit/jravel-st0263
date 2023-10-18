# Proyecto Nro 1


| Materia  | Tópicos especiales en Telemática - ST0263 |
| ------------- | ------------- |
| Integrantes  |  Kevin Alejandro Sossa Chavarria (kasossac@eafit.edu.co) |
|  | Jacobo Rave Londoño (jravel@eafit.edu.co)  |
|   | Daniel Jaramillo Valencia (djaramillv@eafit.edu.co) |
|   | Antonio Carmona Gaviria (acarmonag@eafit.edu.co) |
| Profesor  | Edwin Nelson Montoya Munera (mailto:emontoya@eafit.edu.co) |


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

