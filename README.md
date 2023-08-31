# jravel-st0263
Reto 2 Topicos de Telematica
Jacobo Rave Londoño
email: jravel@eafit.edu.co
profesor: Edwin Nelson Montoya
email: emontoya@eafit.brightspace.com

En el reto 2 implementamos 2 microservicios básicos list_files y find_files que ofrecen un servicio a un cliente. La idea es practicar la comunicacion Sync y Async por medio de los protocolos RPC y AMQP (implementando un MOM usando el servicio rabbitMQ). 
Entonces tenemos un cliente que envia peticiones a un api gateway que va a dirigir el request a los nodos que abarcan el microservisio. Principalmente lo envia por el protocolo RPC pero en caso de que haya una falla en el servicio debe enviarlo por el protocolo AMQP por el servicio de rabbitMQ.

1.1 Se implemento toda la arquitectura en AWS estableciendo la comunicacion de cada nodo propuesto en el diseño, a su vez se implemento el microservicio list_files y se aseguro el correcto funcionamiento y comunicacion de este con el apigateway por medio ded los tipos de comunicacion propuesto. 

![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/5b21ed21-6155-4684-b547-224a5f159709)


1.2 De momento falta implementar el microservicio find_files, que esta fallando por un error en la logica.

2 Para la arquitectura en AWS en primer lugar se crearon los security groups para cada instancia, donde abrimos los puertos por los que se comunican los protocolos de cada nodo, despues se crearon las instancias que representan cada servicio del reto y por ultimo se asignaron las ips elasticas a cada una.

3. El reto se desarrollo en el proyecto entregado por el profe, los lenguajes usados son python para todo el protocolo AMQP, y node js para el protocolo GRPC, la libreria utilizada para el protocolo AMQP es pika y grpc para GRPC. Se utilizo el servicio de rabbitMQ como mom para este reto

Para compilar el proyecto

1. En la instancia de rabbitMQ ejecutar:
    docker start rabbit-server
2. En la instancia ApiGW, server1 y server2 clonar el repo:
    git clone https://github.com/jacevareafit/jravel-st0263
3. instalar dependiencias:
   sudo apt-get update
4. instancia APIGW entrar a la siguiente ruta ubuntu@ip-172-31-44-93:~/jravel-st0263/Reto2/architecture_code/grpc_client y ejecutar el comando:
   sudo python3 client.py
5. instancia server1 entrar a la siguiente ruta ubuntu@ip-172-31-35-152:~/jravel-st0263/Reto2/architecture_code/grpc_server/src/proto_generated y ejecutar     el comando: sudo python3 server.py
6. instancia server2 entrar a la siguiente ruta ubuntu@ip-172-31-39-104:~/jravel-st0263/Reto2/architecture_code/consumer y ejecutar el comando:
   sudo python3 consumerQueue.py


Para hacer peticiones en postman:
  18.213.158.32/list  ip del APIGW y llamamos al microservicio list

![image](https://github.com/jacevareafit/jravel-st0263/assets/68928490/edd7e497-f6f0-40db-9674-3aa5128c7e9d)


Variables de ambiente:

GRPC_HOST=3.225.162.204:50051
RMQ_HOST=54.163.166.84
RMQ_PORT=5672
RMQ_USER=user
RMQ_PASS=password
RMQ_EXCHANGE=my_exchange
PORT = 80
  

ips elasticas

API-GATEWAY: 18.213.158.32 - 
mom: 54.163.166.84 - 
Servicio1: 3.225.162.204 - 
Servicio2: 3.90.130.81

Demostracion:
https://eafit-my.sharepoint.com/:v:/g/personal/jravel_eafit_edu_co/EW0exQRuFQ5CsXhV0ylO9JIBzKjZSgwGu3pgCIROOUVeHg?nav=eyJyZWZlcnJhbEluZm8iOnsicmVmZXJyYWxBcHAiOiJTdHJlYW1XZWJBcHAiLCJyZWZlcnJhbFZpZXciOiJTaGFyZURpYWxvZyIsInJlZmVycmFsQXBwUGxhdGZvcm0iOiJXZWIiLCJyZWZlcnJhbE1vZGUiOiJ2aWV3In19&e=FPDJVC

Referencias:
Remote procedure call (RPC)
https://www.rabbitmq.com/tutorials/tutorial-six-python.html
Flask
https://flask.palletsprojects.com/en/2.3.x/









