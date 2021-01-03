
lenguajes=["C","C++","Python","Java"]
posicion = None 

 
print("")  
for i,elemento in enumerate(lenguajes):  
       if elemento =="Python": 
           posicion =i  
           break
if posicion is None: 
    print("No se encontro elemento") 
else : 
    print("El elemento se encontro en la posicion" +" "+ str(i))  

def Imprimir_Lista(lista = None):
    if lista is not None:  
        for e in lista: 
            print(e)  

    else: 
       print("Sin lista")  

valores= [1,2,3,4,]
Imprimir_Lista(valores)


  
