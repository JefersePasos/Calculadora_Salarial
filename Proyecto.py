#Ingresos de datos
#from os import name
def Ingreso_datos():
    name=[]
    Id=[]
    nombre= str(input("Ingrese su nombre: "))
    cedula=str(input("Ingrese su numero de cédula: "))
    bruto = float(input("Ingrese su Salario bruto: "))  
    name.append(nombre)
    Id.append(cedula)
    comisiones = float(input("Ingrese sus Comisiones percibidas: "))
    otros= float(input("Ingrese Otros ingresos: "))
    try:
        asociacion = float(input("Ingrese el Porcentaje de aporte a la asociación: "))
        asociacion = ((asociacion/100)*bruto)
    except ValueError:
        print("Coloque un número entero sin simbolo de porcentaje: ")
        asociacion = float(input("Ingrese el Porcentaje de aporte a la asociación: "))
        asociacion = ((asociacion/100)*bruto)
    salario_total=bruto+comisiones+otros
    return name,bruto,comisiones,otros,asociacion,salario_total,Id

#MENU  
def menu ():
    Ingrese
    name=Ingrese[0]
    Id=Ingrese[6]
    print('')
    print('Bienvenido ',name[0])
    print('Cedula: ',Id[0])
    print('')
    print ("Informes")
    print ("\t1 - Informe de ingresos")
    print ("\t2 - Informe de deducciones")
    print ("\t3 - Informe general (Ingrsos y deducciones)")
    print ("\t4 - Salir")
    opcion = int(input("Ingrese una opción: ")) 
    print('')      
    return opcion

#MENU OPCIONES
def menu_opciones():
    i=1
    while i==1:
        Opcion=menu()
        if Opcion == 1:        
            print ("Informe de ingresos")  
            print('')
            ingresos()      
        elif Opcion == 2:
            print ("Informe de deducciones",)
            print('')
            deducciones()
        elif Opcion == 3:
            print ("Informe general")
            print('')
            general()
        elif Opcion == 4:
            while Opcion==4:
                print('Hata pronto')
                break
            i+=1
        else:
            print('\n\tMarque una Opcion correcta')
            menu_opciones()
        if i ==1:
            menu_opciones()
        else:
            break
        return Opcion

#VER INGRESOS
def ingresos ():
    Ingrese
    bruto=Ingrese[1]
    comisiones=Ingrese[2]
    otros=Ingrese[3]
    print ("Salario bruto:",'₡',bruto)
    print ("Comisiones:",'₡',comisiones)
    print ("Otros ingresos:",'₡',otros)
    return 

#VER DEDUCCIONES
def deducciones():
    Ingrese
    asociacion=Ingrese[4]
    salario=Ingrese[5]
    salario_empleado = []
    salario_empleado.append (salario)
    i=1
    while i==1:
        iva=[]
        if salario <= 840000:
            print ("No requiere deducciones.")
            iva.append('No tiene deducciones')
        elif salario > 840000 and salario <= 1233000:
            porcentaje = (1233000 - 840000)*0.10 
            print('Tu salario con rebajos por IVA es: ',(salario_empleado[0] - porcentaje))
            ivaSalario = salario_empleado[0] - porcentaje
            acumulados=porcentaje
            iva.append(acumulados)
        elif salario > 1233000 and salario <= 2163000:
            acumulado = 39300
            porcentaje = (2163000 - 1233000)*0.15 
            print('Tu salario con rebajos por IVA es: ',(salario_empleado[0] - (porcentaje + acumulado)))
            ivaSalario = salario_empleado[0] - (porcentaje + acumulado)
            acumulados=acumulado+porcentaje
            iva.append(acumulados)
        elif salario > 2163000 and salario <= 4325000:
            acumulado= 39300 + 139500
            porcentaje = (4325000 - 2163000)*0.20 
            print('Tu salario con rebajos por IVA es: ',(salario_empleado[0] - (porcentaje + acumulado)))
            ivaSalario = salario_empleado[0] - (porcentaje + acumulado)
            acumulados=acumulado+porcentaje
            iva.append(acumulados)
        elif salario > 4325000:
            acumulado=39300 + 139500 + 432400
            porcentaje = (5000000 - 4325000)*0.25 
            print('Tu salario con rebajos por IVA es: ',(salario_empleado[0] - (porcentaje + acumulado)))
            ivaSalario = salario_empleado[0] - (porcentaje + acumulado)
            acumulados=acumulado+porcentaje
            iva.append(acumulados)
        i-=1
    print('Deduccion al salario por IVA es de: ',iva[0])
    print('Deduccion por el aporte a la asociacion es de: ',asociacion)
    return iva

#Deducciones generales
def general():
    Ingrese
    name=Ingrese[0]
    bruto=Ingrese[1]
    comisiones=Ingrese[2]
    otros=Ingrese[3]
    asociacion=Ingrese[4]
    Ingresos_Totales=Ingrese[5]
    print('')
    print('Hola',name[0],'estos son tus: ')
    print('\t Ingresos:')
    print('Su salario bruto es: ',bruto)
    print('Sus comisiones resividas son: ',comisiones)
    print('Otros ingresos son: ',otros)
    print('Sus ingresos en totales son: ',Ingresos_Totales)
    print('\n')
    print('\t Deducciones:')
    deducciones()

#PRINCIPAL
i=1
for i in range(1):
    Ingrese=Ingreso_datos()
    menu_opciones()
print('Adios')

