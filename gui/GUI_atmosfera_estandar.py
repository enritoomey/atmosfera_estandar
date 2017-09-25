__author__ = 'Enriquito'
import sys
import atmosfera_estandar
import layout_atmosfera_estandar as layout
from PySide.QtCore import *
from PySide.QtGui import *

class AtmosferaEstandarDialog(QDialog, layout.Ui_Dialog):

    def __init__(self, altura=None, presion=None, temperatura=None, densidad=None, unit='SI', parent=None):
        super(AtmosferaEstandarDialog, self).__init__(parent)
        self.setupUi(self)
        #TODO: I have to put unit keys before variables names in
        #TODO: atmosfera dict to easyly acces  atmoefera_estandar func
        self.atmosfera = {'SI':{
            'h': 0,
            'deltaT': 0,
            'p': 0,
            't': 0,
            'rho': 0,
            'mu': 0,
            'vson': 0
        }, 'IM': {
            'h': 0,
            'deltaT': 0,
            'p': 0,
            't': 0,
            'rho': 0,
            'mu': 0,
            'vson': 0
        }}

        # Define input unit's label for SI and IM
        self.length_label = {'IM': '[ft]', 'SI': '[m]'}
        self.temp_label = {'IM': '[R]', 'SI': '[K]'}
        self.speed_label = {'IM': '[ft/s]', 'SI': '[m/s]'}
        self.den_label = {'IM': '[slug/ft^2]', 'SI': '[kg/m^3]'}
        self.pressure_label = {'IM': '[slug/m^2]', 'SI': '[Pa]'}

        self.ft2m = 0.3048
        self.lb2kg = 0.453592
        self.slugcuft2kgm3 = 515.379
        self.rankine2kelvin = 5/9.0

        self.units = unit
        if self.units == 'SI':
            self.SI_radioButton.setChecked(True)
        elif self.units == 'IM':
            self.IM_radioButton.setChecked(True)
        else:
            raise
        self.update_units()

        self.R = {'SI': 287.00, 'IM': 1716}
        self.gamma = 1.4

        if altura:
            self.atmosfera[self.units] = altura
            self.actualizar('altura')
        elif presion:
            self.atmosfera[self.units] = presion
            self.actualizar('presion')
        else:
            self.actualizar('altura')
        if temperatura:
            self.lineEdit_t.setText(str(temperatura))
            self.actualizarT(temperatura)
        elif densidad:
            self.lineEdit_rho.setText(str(densidad))
            self.actualizarRho(densidad)

        self.connect(self.IM_radioButton, SIGNAL("clicked()"), self.update_units)
        self.connect(self.SI_radioButton, SIGNAL("clicked()"), self.update_units)

        self.lineEdit_h.editingFinished.connect(lambda: self.actualizar('altura'))
        self.lineEdit_deltaT.editingFinished.connect(lambda: self.actualizar('altura'))
        self.lineEdit_t.editingFinished.connect(lambda: self.actualizarT(float(self.lineEdit_t.text())))
        self.lineEdit_p.editingFinished.connect(lambda: self.actualizar('presion'))
        self.lineEdit_rho.editingFinished.connect(lambda: self.actualizarRho(float(self.lineEdit_rho.text())))
        self.connect(self.acceptButton, SIGNAL("clicked()"), self, SLOT("accept()"))

    def actualizar(self, tipo):
        # TODO: actualizar todos los datos, tanto en SI como en IM
        self.update_values()
        self.call_atmosfera_estandar(tipo)
        self.si2im()
        self.write_lineEdits()

    def actualizarT(self, value):
        temp = value
        self.atmosfera[self.units]['deltaT'] = self.atmosfera[self.units]['deltaT']+temp - self.atmosfera[self.units]['t']
        self.lineEdit_deltaT.setText(str(round(self.atmosfera[self.units]['deltaT'], 2)))
        self.atmosfera[self.units]['t'] = temp
        self.atmosfera[self.units]['rho'] = self.atmosfera[self.units]['p'] / self.atmosfera[self.units]['t']/self.R[self.units]
        self.lineEdit_rho.setText(str(self.atmosfera[self.units]['rho']))

    def actualizarRho(self, value):
        # TODO: Modificar para distintos tipos de unidades
        calculo = 'densidad'
        self.atmosfera[self.units]['rho'] = value
        temp = self.atmosfera[self.units]['p'] / self.atmosfera[self.units]['rho']/self.R[self.units]
        self.atmosfera[self.units]['deltaT'] = self.atmosfera[self.units]['deltaT'] + temp - self.atmosfera[self.units]['t']
        self.lineEdit_deltaT.setText(str(round(self.atmosfera[self.units]['deltaT'], 2)))
        self.atmosfera[self.units]['t'] = temp
        self.lineEdit_t.setText(str(round(temp, 2)))

    def update_units(self):
        if self.IM_radioButton.isChecked():
            self.units = "IM"
        elif self.SI_radioButton.isChecked():
            self.units = "SI"
        else:
            return -1
        self.update_labels()
        self.write_lineEdits()

    def update_labels(self):
        self.unitlabel_h.setText(self.length_label[self.units])
        self.unitlabel_deltaT.setText(self.temp_label[self.units])
        self.unitlabel_p.setText(self.pressure_label[self.units])
        self.unitlabel_t.setText(self.temp_label[self.units])
        self.unitlabel_rho.setText(self.den_label[self.units])
        self.unitlabel_mu.setText(self.length_label[self.units])
        self.unitlabel_Vson.setText(self.speed_label[self.units])

    def write_lineEdits(self):
        self.lineEdit_h.setText(str(self.atmosfera[self.units]['h']))
        self.lineEdit_deltaT.setText(str(self.atmosfera[self.units]['deltaT']))
        self.lineEdit_p.setText(str(self.atmosfera[self.units]['p']))
        self.lineEdit_t.setText(str(self.atmosfera[self.units]['t']))
        self.lineEdit_rho.setText(str(self.atmosfera[self.units]['rho']))
        self.lineEdit_mu.setText(str(self.atmosfera[self.units]['mu']))
        self.lineEdit_Vson.setText(str(self.atmosfera[self.units]['vson']))


    def update_values(self):
        self.read_from_lineEdits()
        if self.units == 'SI':
            self.si2im()
        elif self.units == 'IM':
            self.im2si()
        else:
            raise

    def read_from_lineEdits(self):
        self.atmosfera[self.units]['h'] = float(self.lineEdit_h.text())
        self.atmosfera[self.units]['deltaT'] = float(self.lineEdit_deltaT.text())
        self.atmosfera[self.units]['p'] = float(self.lineEdit_p.text())
        self.atmosfera[self.units]['t'] = float(self.lineEdit_t.text())
        self.atmosfera[self.units]['rho'] = float(self.lineEdit_rho.text())
        self.atmosfera[self.units]['mu'] = float(self.lineEdit_mu.text())
        self.atmosfera[self.units]['vson'] = float(self.lineEdit_Vson.text())


    def si2im(self):
        self.atmosfera['IM']['h'] = self.atmosfera['SI']['h']/self.ft2m
        self.atmosfera['IM']['deltaT'] = self.atmosfera['SI']['deltaT']/self.rankine2kelvin
        self.atmosfera['IM']['p'] = self.atmosfera['SI']['p']/self.lb2kg*self.ft2m
        self.atmosfera['IM']['t'] = self.atmosfera['SI']['t']/self.rankine2kelvin
        self.atmosfera['IM']['rho'] = self.atmosfera['SI']['rho']/self.slugcuft2kgm3
        self.atmosfera['IM']['mu'] = self.atmosfera['SI']['mu']/self.lb2kg*self.ft2m
        self.atmosfera['IM']['vson'] = self.atmosfera['SI']['vson']/self.ft2m

    def im2si(self):
        self.atmosfera['SI']['h'] = self.atmosfera['IM']['h']*self.ft2m
        self.atmosfera['SI']['deltaT'] = self.rankine2kelvin*self.atmosfera['IM']['deltaT']
        self.atmosfera['SI']['p'] = self.atmosfera['IM']['p']*self.lb2kg/self.ft2m
        self.atmosfera['SI']['t'] = self.atmosfera['IM']['t']*self.rankine2kelvin
        self.atmosfera['SI']['rho'] = self.atmosfera['IM']['rho']*self.slugcuft2kgm3
        self.atmosfera['SI']['mu'] = self.atmosfera['IM']['mu']*self.lb2kg/self.ft2m
        self.atmosfera['SI']['vson'] = self.atmosfera['IM']['vson']*self.ft2m

    def call_atmosfera_estandar(self, tipo):
        # atmosfera_estandar solo resuelve en unidades del sistema SI
        if tipo == 'altura':
            input1 = self.atmosfera['SI']['h']
        elif tipo == 'presion':
            input1 = self.atmosfera['SI']['p']
        deltaT = self.atmosfera['SI']['deltaT']
        h, deltaT, p, t, rho, mu, vson = atmosfera_estandar.atmosfera_estandar(tipo, input1, deltaT=deltaT)
        self.atmosfera['SI']['h'] = h
        self.atmosfera['SI']['deltaT'] = deltaT
        self.atmosfera['SI']['p'] = p
        self.atmosfera['SI']['t'] = t
        self.atmosfera['SI']['rho'] = rho
        self.atmosfera['SI']['mu'] = mu
        self.atmosfera['SI']['vson'] = vson


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialogo = AtmosferaEstandarDialog()
    dialogo.show()
    app.exec_()
