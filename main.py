import sys
import var
import events
import clients
from ventana import *
from ventanaCalendario import *
from windowAviso import *

import datetime



class Main(QtWidgets.QMainWindow):

    def __init__(self):
        super(Main, self).__init__()
        var.ui = Ui_MainWindow()
        var.ui.setupUi(self)
        var.ui.actionSalir.triggered.connect(events.Eventos.Salir)
        var.ui.Salir.clicked.connect(events.Eventos.Salir)
        var.sexo=(var.ui.radioButtonFem_2, var.ui.radioButtonMas_2)
        for i in var.sexo:
            i.toggled.connect(clients.Clientes.selSexo)
        '''
        Eventos cada de texto
        '''
        var.ui.CampoDNI.editingFinished.connect(clients.Clientes.validarDNI)
        var.ui.Aceptar.clicked.connect(clients.Clientes.validarDNI)
        #var.ui.grupoSexo.buttonClicked.connect(clients.Clientes.selSexo)

        var.checkPago = (var.ui.checkEfect_2, var.ui.checkTransfe_2, var.ui.checkTarjeta_2)
        for i in var.checkPago:
            i.stateChanged.connect(events.Eventos.grupoPago)

        clients.Clientes.cargarProv()
        var.ui.comboBox.activated[str].connect(clients.Clientes.selProv)

        #var.ui.comboBox.editingFinished.connect(clients.Clientes.selProv)


        var.ui.Calendario.clicked.connect(clients.Clientes.abrirCalendar)

    def showClients(self):
        try:
            #Prepara el registro
            newcli =[]
            clitab = []
            client = [var.ui.editDni, var.ui.editApel, var.ui.editNome, var .ui.editData, var.ui,editDir]
            k=0
            for i in client:
                newcli.append(i.text())
                k+=1
            newcli.append(vpro)
            #Elimina duplicados
            var.pay = set(var.pay)
            for j in var.pay:
                newcli.append(j)
            newcli.append(sex)
            print(newcli)
            print(clitab)
            row = 0 #disposicion de la fila, problema: coloca el último como primero en cada click
            column = 0 #disposicion de la columna
            var.ui.cliTable.insertRow(row) #Inserta una fila nueva con cada click de botón
            for registro in clitab:
                #la celda tiene una posición fila, columa y cargamos en ella el dato
                cell=QtWidgets.QTableWidgetItem(registro) # carga en cell cada dato de la lista
                var.ui.cliTable.setItem(row,column, cell) # lo escribe
                column +=1
        except Exception as error:
            print('Error: %s' % str(error))


class avisoSalir(QtWidgets.QDialog):
    def __init__(self):
        super(avisoSalir, self).__init__()
        var.avisoSalir = Ui_Form()
        var.avisoSalir.setupUi(self)

class DialogCalendar(QtWidgets.QDialog):
    def __init__(self):
        super(DialogCalendar, self).__init__()
        var.dlgcalendar = Ui_Dialog()
        var.dlgcalendar.setupUi(self)
        #diaactual = datetime.now().day
        #mesactual = datetime.now().month
        #anoactual = datetime.now().year
        #var.dlgcalendar.calendarWidget.setSelectedDate((QtCore.QDate(anoactual, mesactual, diaactual)))
        var.dlgcalendar.calendarWidget.clicked.connect(clients.Clientes.cargarFecha)

if __name__ == '__main__':
    app = QtWidgets.QApplication([])
    window = Main()
    var.avisoSalir = avisoSalir()
    var.dlgcalendar = DialogCalendar()
    window.show()
    sys.exit(app.exec())

