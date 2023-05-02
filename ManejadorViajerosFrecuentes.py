from ClaseViajeroFrecuente import Viajero
import csv

class Manejador:
    def __init__ (self):
        self.__lista=[]

    def agregar (self, unaLista):
        self.__lista.append(unaLista)

    def TestLista (self):
        archivo=open('C:\\Users\\chili\\viajeros.csv')
        reader=csv.reader(archivo,delimiter=",")
        for fila in reader:
            num=int(fila[0])
            doc=fila[1]
            nom=fila[2]
            apell=fila[3]
            mill_acum=int(fila[4])
            unaLista=Viajero(num,doc,nom,apell,mill_acum)
            self.agregar(unaLista)

        archivo.close()

    





    def buscar(self,num):
        indice=0
        valorderetorno=None
        bandera=False
        while not bandera and indice<len(self.__lista):
            if(self.__lista[indice].getNumero()==num):
                bandera=True
                valorderetorno=indice
            else: 
                indice+=1
        return valorderetorno           

    def igualar (self,valor):
        i=0
        for i in range (len(self.__lista)):
            unViajero=self.__lista[i]
            
            if (valor == unViajero):
                print("El viajero numero {} tiene la misma cantidad de millas que el valor ingresado".format(unViajero.getNumero()))
            else:
                print("El viajero numero {} tiene distinta cantidad de millas que el valor ingresado".format(unViajero.getNumero()))
     


    def acumular (self, i):
        unViajero=self.__lista[i]
        print(unViajero)
        millas=int(input("Ingresar millas que desea acumular"))
        millas + unViajero
        print("Total de millas acumuladas (actualizado):{}".format(self.__lista[i].getMillas_acum()))


    def canjear (self,i):
        unViajero=self.__lista[i]
        millas=int(input("Ingresar millas que desea canjear"))
        millas - unViajero
        print("Total de millas acumuladas (actualizado):{}".format(self.__lista[i].getMillas_acum()))

    def __str__(self):
        s=""
        for lista in self.__lista:
            s += str(lista) + '\n'
        return s