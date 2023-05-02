
class Viajero:
    __numero=int
    __dni= ""
    __nombre=""
    __apellido=""
    __millas_acum=int
    
    def __init__ (self,num=None,doc=None,nomb=None,apell=None,millas=None):
        self.__numero=num
        self.__dni=doc
        self.__nombre=nomb
        self.__apellido=apell
        self.__millas_acum=int(millas)

    def getNumero (self):
        return self.__numero    
    
    def getMillas_acum (self):
        return self.__millas_acum

    def __eq__(self, otro):
        return self.__millas_acum == otro


    def __radd__(self, otro):
        self.__millas_acum = otro + self.__millas_acum 
        
        
    
    def __rsub__ (self, otro):
        self.__millas_acum = self.__millas_acum - otro   
    
    
    def __str__(self):
        return "Numero:{}-DNI:{}-Nombre y apellido:{} {}-Cantidad de millas:{}".format(self.__numero, self.__dni, self.__nombre, self.__apellido,self.__millas_acum)    
