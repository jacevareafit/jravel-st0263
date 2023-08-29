# jravel-st0263
Reto 2 Topicos de Telematica
Jacobo Rave Londoño
email: jravel@eafit.edu.co
profesor: Edwin Nelson Montoya
email: emontoya@eafit.brightspace.com

En el reto 2 implementamos 2 microservicios básicos que ofrecen un
servicio a un API Gateway y que se deben comunicar por un RPC y por un MOM. 
Entonces tenemos un cliente que habla con un api gateway que va a dirigir el request a los nodos que abarcan el microservisio. Principalmente lo envia por el protocolo GRPC pero en caso de que haya una falla debe enviarlo por el protocolo AMQP por el servicio de rabbitMQ.

1.1 Se implemento toda la arquitectura en AWS y se establecio comunicacion de cada nodo propuesto en el diseño

1.2 De momento falta implementar los microservicios 

2 Para la arquitectura en AWS en primer lugar se crearon los security groups para cada instancia, donde abrimos los puertos por los que se comunican los protocolos de cada nodo, despues se crearon las instancias que representan cada servicio del reto y por ultimo se asignaron las ips elasticas a cada una.

3. El reto se desarrollo en el proyecto entregado por el profe, los lenguajes usados son python para todo el protocolo AMQP, y node js para el protocolo GRPC, la libreria utilizada para el protocolo AMQP es pika y grpc para GRPC. Se utilizo el servicio de rabbitMQ como mom para este reto


ips elasticas

API-GATEWAY: 18.213.158.32
mom: 54.163.166.84
Servicio1: 3.225.162.204
Servicio2: 3.90.130.81








