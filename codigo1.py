print("Bienvenido al programa...")

# Diccionario que recopila los datos del usuario
persona={" Nombre":""," Apellido":""," Edad":0," Peso":0," Altura":0," Dirección":""," Telefono":""}


# Función que, según el valor final del IMC, te devuelve la categoría en la que estás.
def cat_imc( imc ): 
    if imc < 18.5:
        print ("Usted está en la categoria de bajo peso")
    elif imc < 24.9 :
        print ("Usted está en la categoria de peso normal")
    elif imc < 29.9 :
        print ("Usted está en la categoria de sobre peso")
    elif imc < 34.9 :
        print ("Usted está en la categoria de obesidad tipo 1")
    elif imc < 39.9 :
        print ("Usted está en la categoria de obesidad tipo 2")
    elif imc > 40 :
        print ("Usted está en la categoria de obesidad tipo 3")


# Función que imprime los datos del usuario al finalizar el programa.
def imprimir ():
    for dato in persona :
        print (dato , ":" , persona [dato])

for i in persona :
    persona [i] =input(f"Ingrese su{ i }:")

imc=round(float(persona[" Peso"])/(float(persona[" Altura"])**2),2)

persona ["IMC"]=imc

print ( "----------------------------------------------- ---------- " )

imprimir ()
cat_imc(imc)
  
print ( "----------------------------------------------- ---------- " )
