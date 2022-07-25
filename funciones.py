# El salario del empleado será de $8 por hora
# Las horas extras serán a partir de trabajar mas de 8 horas por día
# El empleado gana $12 por horas extra.
rutaArchivo= 'info.txt'
listaIniciales=[]
listaInicialesUnicas=[]
listaHorasInicio=[]
listaHorasFin=[]
listaMinutosTotales=[]
horasTrabajadas=[]
salarios=[]
salariosEmpleados=[]
factorMinuto = 60
def leerArchivoTxt():
    archivo= open(rutaArchivo)
    return archivo.read()


def llenarListas():
    archivo = open("info.txt", "r")
    next(archivo)
    for linea in archivo:
        listaLinea= linea.split(",")
        if listaLinea[0] not in listaInicialesUnicas:
            listaInicialesUnicas.append(listaLinea[0])
            infoEmpleadoSalario = [listaLinea[0]]
            infoEmpleadoSalario.append(0)
            salariosEmpleados.append(infoEmpleadoSalario)
            infoEmpleadoHoras = [listaLinea[0]]
            infoEmpleadoHoras.append(0)
            horasTrabajadas.append(infoEmpleadoHoras)
        listaIniciales.append(listaLinea[0])
        listaHorasInicio.append(listaLinea[2].strip())
        listaHorasFin.append(listaLinea[3].strip())
    archivo.close()
    obtenerHorasTrabajadas()


def obtenerHorasTrabajadas():
    for i in range(len(listaHorasInicio)):
        horasMinutosInicio=listaHorasInicio[i].split(':')
        horasMinutosFin=listaHorasFin[i].split(':')
        horaInicioAMinutos= int(horasMinutosInicio[0])*factorMinuto
        horaFinAminutos= int(horasMinutosFin[0])*factorMinuto
        minutosInicio= int(horasMinutosInicio[1])
        minutosFin= int(horasMinutosFin[1])
        minutosTotales= (horaFinAminutos + minutosFin) - (horaInicioAMinutos+minutosInicio)
        listaMinutosTotales.append(minutosTotales)
    calcularSalarioPorDia()
    calcularSalarioTotalEmpleado()
    mostrarHorasTrabajadas()
    mostrarSalarios()

def mostrarHorasTrabajadas():
    for i in range(len(listaIniciales)):
        for infoEmpleado in horasTrabajadas:
            if infoEmpleado[0]==listaIniciales[i]:
                infoEmpleado[1]= infoEmpleado[1]+ listaMinutosTotales[i]
    for i in horasTrabajadas:
        residuo= i[1]%factorMinuto
        cociente= i[1]//factorMinuto
        i[1]= str(cociente)+ 'h'+str(residuo)+'m'
    print("EMPLEADO      HORAS TRABAJADAS")
    for info in horasTrabajadas:
        print(info[0] + "          " + info[1])
    print()


def calcularSalarioPorDia():
    pico= 480
    for minutos in listaMinutosTotales:
        if minutos> pico:
            salario= (pico*8)/factorMinuto + ((minutos-pico)*12)/factorMinuto
            salarios.append(salario)
        else:
            salario= (minutos*8)/factorMinuto
            salarios.append(salario)

def calcularSalarioTotalEmpleado():
    for i in range(len(listaIniciales)):
        for infoEmpleado in salariosEmpleados:
            if infoEmpleado[0]==listaIniciales[i]:
                infoEmpleado[1]= infoEmpleado[1]+ salarios[i]

def mostrarSalarios():
    print("EMPLEADO      SALARIO")
    for info in salariosEmpleados:
        print(info[0] + "          $" + "{:.2f}".format(info[1]))



