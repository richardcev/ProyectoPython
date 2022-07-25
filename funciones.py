# El salario del empleado será de $8 por hora
# Las horas extras serán a partir de trabajar mas de 8 horas por día
# El empleado gana $12 por horas extra.
import os
rutaArchivo= 'info.txt'
listaIniciales=[]
listaInicialesUnicas=[]
listaHorasInicio=[]
listaHorasFin=[]
listaMinutosTotales=[]
salarios=[]
salariosEmpleados=[]
factorMinuto = 60
vcuatroHorasAMinutos= 1440
pico = 480
def leerArchivoTxt():
    archivo= open(rutaArchivo)
    return archivo.read()


def llenarListas():
    archivo = open("info.txt", "r")
    next(archivo)
    for linea in archivo:
        listaLinea= linea.split(",")
        # Encuentro las iniciales de cada empleado
        if listaLinea[0] not in listaInicialesUnicas:
            listaInicialesUnicas.append(listaLinea[0])
            infoEmpleados = [listaLinea[0]]
            infoEmpleados.append(0)
            infoEmpleados.append(0)
            infoEmpleados.append(0)
            salariosEmpleados.append(infoEmpleados)
        listaIniciales.append(listaLinea[0])
        listaHorasInicio.append(listaLinea[2].strip())
        listaHorasFin.append(listaLinea[3].strip())
    archivo.close()
    obtenerHorasTrabajadas()


def obtenerHorasTrabajadas():
    # Transformo las horas a minutos para realizar los calculos del salario
    for i in range(len(listaHorasInicio)):
        horasMinutosInicio=listaHorasInicio[i].split(':')
        horasMinutosFin=listaHorasFin[i].split(':')
        horaInicioAMinutos= int(horasMinutosInicio[0])*factorMinuto
        horaFinAminutos= int(horasMinutosFin[0])*factorMinuto
        minutosInicio= int(horasMinutosInicio[1])
        minutosFin= int(horasMinutosFin[1])
        minutosTotales = (horaFinAminutos + minutosFin) - (horaInicioAMinutos + minutosInicio)
        # Este caso es cuando el horario de entrada es tarde y la salida es al siguiente dia
        if minutosTotales<0:
            horaInicio24Horas= vcuatroHorasAMinutos- horaInicioAMinutos
            minutosTotales= horaInicio24Horas+ minutosInicio+horaFinAminutos+minutosFin
        listaMinutosTotales.append(minutosTotales)
    calcularSalarioPorDia()
    calcularSalarioTotalEmpleado()
    definirHorasTrabajadas()
    mostrarInfoSalarios()

def definirHorasTrabajadas():
    for i in range(len(listaIniciales)):
        for infoEmpleado in salariosEmpleados:
            if infoEmpleado[0]==listaIniciales[i]:
                # Total de horas extras
                if listaMinutosTotales[i] > pico:
                    infoEmpleado[1] = infoEmpleado[1] + pico
                    infoEmpleado[2]= infoEmpleado[2]+ (listaMinutosTotales[i] - pico)
                else:
                    infoEmpleado[1] = infoEmpleado[1] + listaMinutosTotales[i]


def calcularSalarioPorDia():
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
                infoEmpleado[3]= infoEmpleado[3]+ salarios[i]

def mostrarInfoSalarios():
    print("{:<15} {:<15} {:<15} {:<10}".format('Empleado', 'Horas', 'Horas extras', 'Salario($)'))
    for info in salariosEmpleados:
        residuo1= info[1]%factorMinuto
        cociente1= info[1]//factorMinuto
        residuo2= info[2]%factorMinuto
        cociente2= info[2]//factorMinuto
        horasNormales= str(cociente1)+ 'h'+str(residuo1)+'m'
        horasExtras= str(cociente2)+ 'h'+str(residuo2)+'m'
        info[1]= horasNormales
        info[2]=horasExtras
        templeado, thorasnorm, thorasextras, tsalario= info
        print("{:<15} {:<15} {:<15} {:.2f}".format(templeado, thorasnorm, thorasextras, tsalario))


def mostrarRutaArchivo():
    print(os.path.dirname(os.path.abspath(rutaArchivo)))

def cambiarRutaArchivo():
    destination= "nuevoDirectorio\\info.txt"
    try:
        if os.path.exists(destination):
            print("Ya existe el archivo aqui")
        else:
            os.replace(rutaArchivo, destination)
            print(rutaArchivo+ " fue movido")
    except FileNotFoundError:
        print(rutaArchivo+ "no fue encontrado")

