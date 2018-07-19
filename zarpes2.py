import sys
import copy
import os
import json

matrices = json.loads(open('matrixZarpes.json').read())
matrixComuna = matrices["adjacency"]
matrix = matrices["distances"]


# guarda la distancia mínima entre rutas ej: (1,(2,3,4)):3 , el valor
# mínimo desde ir de 1 y pasar por 2 3 y 4
g = {}
p = []  # guarda las rutas óptimas
# datos para ruteo

def tsp(vehicle): #el algoritmo tsp recibe una ruta en forma de tupla
	# print("calculando para el vehiculo",vehicle)
	# vehicle=list(vehicle)
	# vehicle.append(1)
	# vehicle=tuple(vehicle)
	# print(vehicle)
	global g
	global p 
	finalSolution=[] #para guardar la solucion final
	for x in vehicle: 

			   
		g[x , ()] = matrix[clientes[x]-1][0]

	VehicleClients=tuple(vehicle)    

		 
	distance=get_minimum(1, VehicleClients)


	solution = p.pop()
	
	
	finalSolution.append(1)

	finalSolution.append(solution[1][0])

	for x in range(len(vehicle) - 1):
		for new_solution in 	p:
			if tuple(solution[1]) == new_solution[0]:
				solution = new_solution
				#print(solution[1][0], end=', ')
				finalSolution.append(solution[1][0])
				break

	# print("solucion final")
	g = {}
	p = []
	return finalSolution,distance


def get_minimum(k, a): #calcula camino mínimo entre el nodo k y el set de nodos a
	


	if (k, a) in g:


		# Already calculated Set g[%d, (%s)]=%d' % (k, str(a), g[k, a]))
		return g[k, a]


	values=[]
	all_min=[]


	for j in a: #j es el valor de cada cliente y a es el valor de cada sub ruta
		
		
		comunaJ=clientes[j]
		comunaK=clientes[k]

		set_a = copy.deepcopy(list(a))  
				 
		set_a.remove(j)

		all_min.append([j, tuple(set_a)])

		result = get_minimum(j, tuple(set_a))

		valor=values.append(matrix[comunaK-1][comunaJ-1] + result)#costo de ir desde k a j + la distancia más corta en ir a j y pasar por el anterior set_a

	g[k, a] = min(values)
	p.append(((k, a), all_min[values.index(g[k, a])]))


	return g[k, a]

class vehicle:

	def __init__(self, code):
		self.code = code
		self.capacity = 8
		self.avaible = True
		self.route = []
		self.distance_route = 0

	def cost_add(self,client):#Revisar esto

		route_aux_2 = copy.copy(self.route)
		route_aux_2.append(client)
		route_aux_2,distance_route_aux_2 = tsp(route_aux_2)
		cost = distance_route_aux_2 - self.distance_route
		if(distance_route_aux_2>15):
			cost=9000
		print("costo:",cost)
		print("se calcula para el vehiculo",self.code)
		print("route_aux_2",route_aux_2,"distancia",distance_route_aux_2)
		print("ruta",self.route,"distancia",self.distance_route)
		print("costo",cost)
		print("-----------------")
	
		return cost

	def add_client(self,client):
		self.route.append(client)
		print("se agrega el mejor cliente que es:",client,"la ruta ahora es",self.route)
		self.capacity = self.capacity - 1
		self.route,self.distance_route = tsp(self.route)
		if (1 in self.route):
			self.route.remove(1)
		print("la mejor ruta es:",self.route)
		print("el costo es:",self.distance_route)
		

	def remove_client(self,client):
		if(client not in self.route):
			print("el cliente no esta en este vehiculo")
		else:
			clients.remove(self.route)
			distance_route = tsp(self.route)[1]


class deposito(): #El deposito cuenta con una capacidad maxima de vehiculos que puede almacenar y el lugar de los vehiculos. 

	def __init__(self, capacity):
		self.capacity = capacity #capacidad maxima de almacenamiento
		self.lugares = [] #Almacena vehiculos en forma de objeto 

	def view_depot(self):  #Muestra vehiculos en el deposito y sus rutas
		for v in self.lugares:
			print("Vehículo ", v.code, ":",v.route)
			

	def add_vehicle(self,v): #Agrega el vehiculo que recibe como input a self.lugares.
		if(len(self.lugares) == 5):
			print("no hay espacio disponible")
		else:			
			self.lugares.append(v)
			print("se agregó el vehículo",v.code)

	def remove_vehicle(self,v): #Elimina el vehiculo que recibe como input de self.lugares
		v2=0
		for vehicle in self.lugares:
			print(vehicle.code,v)
			if(vehicle.code==str(v)):
				v2=vehicle				
		if(v2==0):
			print("el vehiculo no esta en el deposito")
		else:
			self.lugares.remove(v2)

	def add_cliente(self,id_cliente): #Si hay solo un vehiculo en self.lugares entonces lo agrega a el, en caso contrario revisa cual es 
									  # el vehiculo que recibe el menor impacto al agregar el cliente seleccionado y lo agrega ahi.
		# lugares_disponibles=[]
		# for i in self.lugares:
		# 	if (len(i)<= 8):	
		# 		lugares_disponibles.append(i)
		if(self.lugares==[]):
			print("No hay ningún vehículo al cual ingresar el cliente")
		elif(self.lugares[0].route==[]):
			print("agregando cliente al vehículo:",self.lugares[0].code)
			self.lugares[0].add_client(id_cliente)
		else:
			best_vehicle = min(self.lugares, key=lambda x: x.cost_add(id_cliente)) #Falta arreglar esta funcion, ya que revisa todos
			#todos los vehiculos disponibles, incluso los que estan vacios. Ademas se puede agregar a vehiculos que estan llenos
			#falta corregir eso. 
			print("agregando el cliente ",id_cliente,"al vehiculo:",best_vehicle.code)
			if(best_vehicle.cost_add(id_cliente)==9000):
				print("no se puede agregar el cliente a ningun vehiculo ya que excede el maximo de tiempo")
			else:
				best_vehicle.add_client(id_cliente)

if __name__ == '__main__':
	clientes={1:1}
	continuar = 1
	depot = deposito(5)
	while(continuar != 0):

		print("¿Que desea hacer?")
		print("1: Ingresar cliente")
		print("2: Ingresar vehiculo")
		print("3: Quitar vehiculo")
		print("4: Quitar cliente")
		print("5: Ver depósito")
		print("0: Salir")
		opcion = int(input())

		if(opcion == 1):
			print("Ingrese codigo cliente")
			idd = int(input())
			print("Ingrese comuna destino")
			destino = int(input())
			clientes[idd]=destino
			# print(clientes)
			depot.add_cliente(idd)


		if(opcion == 2):
			print("Ingrese id vehículo")
			idd = input()
			v=copy.copy(vehicle(idd))
			depot.add_vehicle(v)

		if(opcion == 3):
			print("Ingrese id vehículo")
			idd = int(input())
			depot.remove_vehicle(idd)

		if(opcion == 4):
			print("¿En que vehículo está el cliente?")
			v = int(input())
			print("¿Cuál es el id del cliente?")
			idd = int(input())
			v.remove_client(idd)
		if(opcion==5):
			depot.view_depot()

		if(opcion == 0):
			print("saliendo")
			break


		
