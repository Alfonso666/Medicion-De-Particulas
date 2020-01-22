#Interfaces Graficas
#Lab 2
#By Alfonso Duarte
###############################

import matplotlib.pyplot as plt
#import matplotlib
#matplotlib.use('TkAgg')
import numpy as np
import smtplib

PM2_5 =[];PM10 = []; PM2_5s = []
PM10s = []; sumaPaquete = [];
Promedios = [] 

plt.style.use('bmh')

def Extraccion_paquetes():
	global PM2_5
	global PM10
	f= open("datos.txt")
	for i in f.readlines(): 
		PM2_5.append(i.split(",")[2:4])
		PM10.append(i.split(",")[4:6])
		sumaPaquete.append(i.split(",")[2:9])
	f.close()

def Mediciones_PM2_5s():
	global PM2_5
	global PM2_5s
	for i in PM2_5:
		lsb= int(i[0])
		msb= int(i[1])
		PM2_5s.append(((msb*256)+lsb)/10.0)

def Mediciones_PM10s():
	global PM10
	global PM10s
	for i in PM10:
		lsb= int(i[0])
		msb= int(i[1])
		PM10s.append(((msb*256)+lsb)/10.0)

def Promedio_PM2_5():
	return sum(PM2_5s)/1001
	
def Promedio_PM10():
	return sum(PM10s)/1001

def valida_Paquete():
	cont=1
	for i in sumaPaquete:
		if (int(i[0]) + int(i[1])+ int(i[2])+ int(i[3])+ int(i[4])+ int(i[5]))%256 == int(i[6]):
			print "Paquete " + str(cont) + " validado"
			cont+=1


def Grafica(promedio):
	###################### grafica lineal #######################
	fig=plt.figure()
	fig=plt.gcf()
	fig=fig.set_size_inches(18,12)

	plt.subplot(221)
	plt.plot(PM2_5s,color="green") 
	plt.legend(['PM2.5'])
	plt.title('Grafico lineal PM2.5')
	plt.xlabel('cantidad de mediciones')
	plt.ylabel('mg/m^3')
	plt.grid(True)
	#-#
	plt.subplot(223)
	plt.plot(PM10s) 
	plt.legend(['PM10'])
	plt.title('Grafico lineal PM10')
	plt.xlabel('cantidad de mediciones')
	plt.ylabel('mg/m^3')
	plt.grid(True)


	###################### grafica de Barras #######################
	plt.subplot(122)
	a = plt.bar(range(len(Promedios)),Promedios, color=["b","r"])
	plt.legend(a,['PM2.5','PM10'])
	plt.title('Promedio en PM2.5 y PM10')
	plt.xticks(range(2), ['PM2.5', 'PM10'])
	plt.xlabel('tipo de mediciones')
	plt.ylabel('promedio en mg/m^3')
	plt.grid(True)


	plt.savefig("graficos.png")
	plt.show()
	


if __name__== "__main__":
	Extraccion_paquetes()
	Mediciones_PM2_5s()
	Mediciones_PM10s()
	valida_Paquete()
	print Promedio_PM2_5()
	print Promedio_PM10()
	Promedios.append(Promedio_PM2_5())
	Promedios.append(Promedio_PM10())
	print max(PM2_5s)
	print min(PM2_5s)
	print max(PM10s)
	print min(PM10s)
	Grafica(Promedios)

