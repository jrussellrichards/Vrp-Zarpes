# Vrp-Zarpes

Aplicación de ruteo de vehículos para empresa de transfers.

** Contexto **

La empresa actualmente no cuenta con un sistema óptimo de asignación de pasajeros a sus transfers, quienes se encuentran en el aeropuerto y necesitan llegar a sus destinos. 

Por políticas de la empresa un cliente debe ser asignado a un transfers inmediatamente al comprar el ticket (debe esperar dentro de él). 
Los transfers tienen una capacidad máxima de 8 pasajeros.

Solución:

Se trata cada vehículo como un TSP (Traveling Salesman Problem) y no como un vrp (debido a la restricción de asignación a vehículos inmediatos). 

  Se asigna un tiempo de recorrido igual a cero
  Al llegar un pasajero se añade este ficticiamente a todos los vehículos y se calcula la ruta óptima tratado como un TSP para cada uno de estos, tomando en cuenta todos los clientes correspondientes en cada uno de ellos. 
  Luego se analiza cual es el vehículo que al añadir ese cliente, minimice el tiempo total de recorrido. 
  Se debe además verificar que un cliente no permanezca un tiempo muy largo durante el vehículo (dado por restricciones de la empresa)
  
Tecnología y técnicas utilizada:

-Python
-POO
-Programación dinámica
-Json
